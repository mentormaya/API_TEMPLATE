import os

def generate_env_sample():
    with open(".env", "r") as env_file:
        with open(".env.sample", "w") as env_sample_file:
            for line in env_file:
                if line.strip() and not line.startswith("#"):
                    key = line.split("=")[0]
                    l = f"{key}=YOUR_{key}_HERE"
                    env_sample_file.write(f"{l}\n")

if __name__ == "__main__":
    generate_env_sample()
