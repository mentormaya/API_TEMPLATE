from pprint import pprint
from dotenv import dotenv_values

config = dotenv_values(".env")

pprint(config)