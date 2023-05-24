from utils.logger import Logger
from utils.constants import config
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html

logger = Logger()

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
    
    openapi_url="/api/v1/openapi.json",
    docs_url=None,
    redoc_url=None
)

api.mount("/public", StaticFiles(directory="public"), name="public")

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.on_event("startup")
async def startup_event():
    logger.log(msg="Application Started!")

@api.on_event("shutdown")
def shutdown_event():
    logger.log(msg="Application Shutdown!")

@api.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(req: Request):
    logger.log("Docs accessed!", host=req.client.host)
    return get_swagger_ui_html(
        openapi_url=api.openapi_url,
        title = api.title + " - Docs UI",
        oauth2_redirect_url=api.swagger_ui_oauth2_redirect_url,
        swagger_favicon_url=config['APP_FAVICON'],  # Path to your favicon file
    )

@api.get(api.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect(req: Request):
    logger.log("Docs UI redirected!", host=req.client.host)
    return get_swagger_ui_oauth2_redirect_html()

# route for the root
@api.get("/", tags=["APP"])
async def read_main(req: Request):
    logger.log("API Home accessed!", host=req.client.host)
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
@api.get("/healthcheck", tags=["APP"])
async def health_check(req: Request):
    logger.log("API health checked!", host=req.client.host)
    return {"heartbeat": "I am alive!"}


# route for the favicon request
@api.get("/favicon.ico", include_in_schema=False, response_class=FileResponse, tags=["APP"])
async def get_favicon(req: Request):
    logger.log("API favicon accessed!", host=req.client.host)
    return FileResponse(config["APP_FAVICON"])
