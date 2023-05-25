import os
from dotenv import dotenv_values

secret_env_list = dotenv_values(".env.secret")
shared_env_list = dotenv_values(".env.shared")

# for github only
github_env = os.getenv("DATABASE_URL")


config = dict({**secret_env_list, **shared_env_list})

if "DATABASE_URL" not in config.keys():
    config["DATABASE_URL"] = "sqlite:///app/database/mis_dev.db"
