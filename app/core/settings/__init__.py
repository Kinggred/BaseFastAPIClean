from os import environ
from functools import lru_cache

from .database import Database

# TODO: Consider using special variable to
# determine if loading variables is needed
if not environ.get("POSTGRES_HOST"):
    """
    This statement makes sure that environment variables
    are loaded when not using docker.

    POSTGRES_HOST can be replaced with any other variable
    as long as this variable is not set as optional in settings
    """
    from dotenv import load_dotenv

    load_dotenv(".env.local")


# TODO: Add settings for cors and possibly authorization.
class Settings(Database):
    """
    If you want to add settings just append yout module to Settings parents.
    """

    pass


@lru_cache()
def get_settings() -> Settings:
    return Settings()
