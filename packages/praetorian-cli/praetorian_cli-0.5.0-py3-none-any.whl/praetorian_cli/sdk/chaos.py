import os
import boto3
import requests

from praetorian_cli.sdk.account import verify_credentials, Account


class Chaos:

    def __init__(self, account: Account):
        self.account = account

    @verify_credentials
    def my(self, params: dict) -> {}:
        resp = requests.get(f"{self.account.api}/my", params=params, headers=self.account.headers)
        if not resp.ok:
            raise Exception(f'[{resp.status_code}] Request failed')
        return resp.json()

    @verify_credentials
    def trigger(self, capability: str, composite: str):
        resp = requests.post(f"{self.account.api}/job/{capability}", json=dict(composite=composite), headers=self.account.headers)
        if not resp.ok:
            raise Exception(f'[{resp.status_code}] Request failed')
        return resp.json()

    @verify_credentials
    def add_risk(self, composite: str, finding: str, status: int = 0, severity: int = 0):
        data = dict(composite=composite, finding=finding, status=status, severity=severity)
        resp = requests.post(f"{self.account.api}/risk", json=data, headers=self.account.headers)
        if not resp.ok:
            raise Exception(f'[{resp.status_code}] Request failed')
        return resp.json()

    @verify_credentials
    def upsert_seed(self, dns: str, status: int) -> {}:
        resp = requests.post(f"{self.account.api}/seed", json={"seed": dns, "status": status}, headers=self.account.headers)
        if not resp.ok:
            raise Exception(f'[{resp.status_code}] Request failed')
        return resp.json()

    @verify_credentials
    def upload(self, name: str):
        with open(name, 'rb') as file:
            resp = requests.put(f"{self.account.api}/file/{name}", data=file, allow_redirects=True, headers=self.account.headers)
            if not resp.ok:
                raise Exception(f'[{resp.status_code}] Request failed')

    @verify_credentials
    def download(self, key: str, download_path: str) -> bool:
        directory = os.path.dirname(download_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        resp = requests.get(f"{self.account.api}/file/{key}", allow_redirects=True, headers=self.account.headers)
        if not resp.ok:
            raise Exception(f'[{resp.status_code}] Request failed')
        with open(download_path, 'wb') as file:
            file.write(resp.content)
