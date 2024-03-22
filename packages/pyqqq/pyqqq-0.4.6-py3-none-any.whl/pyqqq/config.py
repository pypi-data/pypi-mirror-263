import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

class Config:
    PYQQQ_API_URL = "https://qupiato.com/api"

    @property
    def TINY_DB_PATH(self):
        return os.getenv('TINY_DB_PATH', 'db.json')

    @property
    def PYQQQ_API_KEY(self):
        return os.getenv("PYQQQ_API_KEY")

    @property
    def CREDENTIAL_FILE_PATH(self):
        return os.path.expanduser("~/.qred")

    @property
    def GOOGLE_CLOUD_LOGGING_ENABLED(self):
        return os.getenv("GOOGLE_CLOUD_LOGGING_ENABLED", "false") == "true"
