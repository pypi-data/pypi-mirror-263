import pyqqq.config as c
import os


def get_api_key() -> str | None:
    if c.PYQQQ_API_KEY:
        return c.PYQQQ_API_KEY

    elif os.path.exists(c.CREDENTIAL_FILE_PATH):
        with open(c.CREDENTIAL_FILE_PATH, "r") as f:
            return f.read().strip()

    return None
