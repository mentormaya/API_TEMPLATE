from dotenv import dotenv_values

config_list = dotenv_values(".env")

config = dict(config_list)