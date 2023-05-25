import os
from dotenv import dotenv_values, load_dotenv

# testing for github test invironment for test values
if os.getenv("GIT") == "GitHub":
    load_dotenv(".env.secret")
    secret_env_list = os.environ
else:
    secret_env_list = dotenv_values(".env.secret")
shared_env_list = dotenv_values(".env.shared")

config = dict({**secret_env_list, **shared_env_list})

if "DATABASE_URL" not in config.keys():
    config["DATABASE_URL"] = "sqlite:///app/database/mis_dev.db"
