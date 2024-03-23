import configparser
import os
from pathlib import Path

from praetorian_cli.sdk.account import Account
from praetorian_cli.sdk.chaos import Chaos


class BaseTest:

    def setup_chaos(self):
        keychain_location = os.path.join(Path.home(), '.praetorian', 'keychain.ini')
        config = configparser.ConfigParser()
        config.read(keychain_location)
        return Chaos(Account(keychain_location=keychain_location)), config['United States']['username']
