from uprock_sdk.settings import GLOBAL_SETTINGS


def init(**kwargs):
    GLOBAL_SETTINGS.update(kwargs)
