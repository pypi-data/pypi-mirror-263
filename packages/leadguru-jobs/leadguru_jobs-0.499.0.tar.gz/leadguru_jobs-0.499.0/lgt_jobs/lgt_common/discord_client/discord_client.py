import loguru
import requests
from requests import Response
from lgt_jobs.lgt_common.discord_client.methods import DiscordMethods


class DiscordClient:
    base_url = 'https://discord.com/api/'
    discord_api_version = 'v9/'
    token: str
    headers: dict

    def __init__(self, token: str = None):
        self.token = token
        self.headers = {"Authorization": self.token}

    def login(self, login: str, password: str, captcha_key: str = None) -> dict:
        payload = {
            'login': login,
            'password': password,
            'captcha_key': captcha_key,
            "undelete": False,
            "login_source": "",
            "gift_code_sku_id": None
        }
        response = requests.post(f"{self.base_url}{self.discord_api_version}{DiscordMethods.LOGIN.value}", json=payload)
        if response.status_code == 400 or response.status_code == 200:
            return response.json()
        return {}

    def get_servers(self) -> list | dict:
        response = requests.get(f"{self.base_url}{DiscordMethods.USER_GUILDS.value}", headers=self.headers)
        return self.__response(response).json()

    def get_dms(self) -> list | dict:
        response = requests.get(f"{self.base_url}{DiscordMethods.USER_DMS.value}", headers=self.headers)
        return self.__response(response).json()

    def get_current_user(self) -> dict:
        response = requests.get(f"{self.base_url}{DiscordMethods.USER.value}", headers=self.headers)
        if response.status_code != 200:
            self.__log_error(response)
        return response.json()

    def get_channels(self, guild_id: str) -> list | dict:
        response = requests.get(f"{self.base_url}{DiscordMethods.guild_channels(guild_id)}", headers=self.headers)
        return self.__response(response).json()

    def get_invite_link(self, channel_id: str) -> Response:
        response = requests.post(f'{self.base_url}{self.discord_api_version}'
                                 f'{DiscordMethods.channels_invites(channel_id)}', headers=self.headers)
        return self.__response(response)

    @staticmethod
    def __log_error(response: Response):
        loguru.logger.warning(f"[DiscordClient WARNING]: {response.url}, {response.status_code}, {response.content}")

    @staticmethod
    def __response(response: Response):
        if response.status_code != 200:
            DiscordClient.__log_error(response)
        return response
