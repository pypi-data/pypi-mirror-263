import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())


TINY_DB_PATH = os.getenv('TINY_DB_PATH', 'db.json')

PYQQQ_API_URL = "https://qupiato.com/api"

PYQQQ_API_KEY = os.getenv("PYQQQ_API_KEY")

CREDENTIAL_FILE_PATH = os.path.expanduser("~/.qred")

GOOGLE_CLOUD_LOGGING_ENABLED = (
    os.getenv("GOOGLE_CLOUD_LOGGING_ENABLED", "false") == "true"
)
