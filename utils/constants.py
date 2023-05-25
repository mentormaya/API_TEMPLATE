import os
from dotenv import dotenv_values

secret_env_list = dotenv_values(".env.secret")
shared_env_list = dotenv_values(".env.shared")

# for github only
github_env = os.getenv("DATABASE_URL")

config = dict({**secret_env_list, **shared_env_list})
