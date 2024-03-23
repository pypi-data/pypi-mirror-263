import os
import boto3
import configparser

from functools import wraps
from os.path import exists
from pathlib import Path


def verify_credentials(func):
    @wraps(verify_credentials)
    def handler(*args, **kwargs):
        try:
            account = args[0].account
            keychain = account.keychain()

            account.api = keychain.get(account.profile, 'api')
            account.client_id = keychain.get(account.profile, 'client_id')
            account.username = keychain.get(account.profile, 'username', fallback=None)
            account.password = keychain.get(account.profile, 'password', fallback=None)
            if not (account.username and account.password):
                new_credentials = account.write_credentials()
                account.username = new_credentials['username']
                account.password = new_credentials['password']

            account.headers = {
                'Authorization': f'Bearer {account.token()}',
                'Content-Type': 'application/json'
            }
            return func(*args, **kwargs)

        except KeyError as e:
            raise Exception('Keychain missing: %s' % e)
        except StopIteration:
            raise Exception('Could not find "%s" profile in %s' % (args[0].account.profile, args[0].account.keychain_location))
    handler.__wrapped__ = func
    return handler


class Account:

    def __init__(self, profile='United States', keychain_location=os.path.join(Path.home(), '.praetorian', 'keychain.ini')):
        self.profile = profile
        self.keychain_location = keychain_location

    def keychain(self):
        cfg = configparser.ConfigParser()
        cfg.read(self.keychain_location)
        if not cfg.sections():
            exit('[!] No keychain. Please visit research.praetorian.com.')
        return cfg

    def write_credentials(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not exists(self.keychain_location):
            head, _ = os.path.split(Path(self.keychain_location))
            Path(head).mkdir(parents=True, exist_ok=True)
            open(self.keychain_location, 'x').close()

        cfg = configparser.ConfigParser()
        cfg[self.profile] = {
            'username': username,
            'password': password
        }
        combo = self._merge_configs(cfg, self.keychain())
        with open(self.keychain_location, 'w') as f:
            combo.write(f)
        return {
            'username': username,
            'password': password
        }

    def token(self):
        cognito_client = boto3.client('cognito-idp', region_name='us-east-2')
        response = cognito_client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': self.username,
                'PASSWORD': self.password
            },
            ClientId=self.client_id
        )
        return response['AuthenticationResult']['IdToken']

    @staticmethod
    def _merge_configs(cfg_from, cfg_to):
        for section in cfg_from.sections():
            if section not in cfg_to:
                cfg_to[section] = {}
            for key, value in cfg_from[section].items():
                cfg_to[section][key] = value
        return cfg_to
