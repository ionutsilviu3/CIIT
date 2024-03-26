import os
from models.SQLClient import SQLClient
from dotenv import find_dotenv, load_dotenv


class LoginModel:
    def __init__(self):
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self.client = SQLClient(os.getenv("URL"), os.getenv(
            "PORT"), os.getenv("DB"), os.getenv("USER"), os.getenv("PASSWORD"))
        self.user_credentials = {}
        self.client.connect()
    def __del__(self):
        self.client.disconnect()

    def set_credentials(self, user_credentials):
        self.user_credentials = user_credentials
        
    def is_valid(self, user_credentials):
        return self.client.isUserExisting(user_credentials.get('mail'),user_credentials.get('password'))
