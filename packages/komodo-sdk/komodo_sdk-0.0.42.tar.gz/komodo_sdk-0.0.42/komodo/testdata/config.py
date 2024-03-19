import os
from pathlib import Path

from komodo.framework.komodo_config import KomodoConfig


class TestConfig(KomodoConfig):
    PATH = os.path.dirname(__file__)
    TEST_MONGO_URL = "mongodb://root:example@localhost:27017/"

    def data_dir(self) -> Path:
        return Path(self.PATH)

    def get_mongo_uri(self):
        return self.get_secret('MONGO_URL', self.TEST_MONGO_URL)

    def get_serpapi_key(self):
        self.get_secret('SERP_API_KEY')

    @classmethod
    def path(cls, relative_path=""):
        return TestConfig().data_dir() / relative_path


if __name__ == "__main__":
    print(TestConfig.PATH)
    print(TestConfig.path())
