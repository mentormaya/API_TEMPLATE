from fastapi import FastAPI
from utils.constants import config
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

api = FastAPI(
    title=config["APP_NAME"],
    description=config["APP_DESCRIPTION"],
    version=config["APP_VERSION"],
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

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# route for the root
@api.get("/")
async def read_main():
    return {
        "title": config["APP_NAME"],
        "description": config["APP_DESCRIPTION"],
        "termsOfService": config["TERMS_OF_SERVICES"],
        "contact": {
            "name": config["APP_DEVELOPER"],
            "url": config["APP_DEV_WEB"],
            "email": config["APP_DEV_EMAIL"],
        },
        "license": {
            "name": config["APP_LICENSE_NAME"],
            "url": config["APP_LICENSE_URL"],
        },
        "version": config["APP_VERSION"],
    }


# route for the healthcheck endpoint
@api.get("/healthcheck")
async def health_check():
    return {"heartbeat": "I am alive!"}


# route for the favicon request
@api.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    return {"msg": "no favicon needed"}
