import httpx

from uprock_sdk import GLOBAL_SETTINGS

GLOBAL_CLIENT = httpx.AsyncClient(base_url=GLOBAL_SETTINGS.API_URL)
