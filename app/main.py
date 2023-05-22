from utils.constants import config
from fastapi import FastAPI

api = FastAPI(
    title=config['APP_NAME'],
    description=config['APP_DESCRIPTION'],
    version=config['APP_VERSION'],
    terms_of_service="http://example.com/terms/",
    contact={
        "name": config["APP_DEVELOPER"],
        "url": config["APP_DEV_WEB"],
        "email": config["APP_DEV_EMAIL"],
    },
    license_info={
        "name": config["APP_LICENSE_NAME"],
        "url": config["APP_LICENSE_URL"],
    },
)

@api.get("/")
async def read_main():
    return {"msg": "Hello World"}

@api.get("/favicon.ico", include_in_schema=False)
async def read_main():
    return {"msg": "no favicon needed"}