import secrets
from typing import Any, Dict, List, Optional, Union
import os
from dotenv import load_dotenv,find_dotenv
from pydantic import  BaseSettings
from os import getenv


load_dotenv(find_dotenv())

class Settings(BaseSettings):
    POSTGRES_SERVER: getenv('POSTGRES_SERVER')
    POSTGRES_USER: getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: getenv('POSTGRES_PASSWORD')
    POSTGRES_DB: getenv('POSTGRES_DB')
    
    