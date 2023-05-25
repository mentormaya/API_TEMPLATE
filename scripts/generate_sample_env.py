import os
import time
import subprocess


def generate_env_sample():
    """_summary_: This is the function to extract the variables from the .env file
    and generate a sample env file named '.env.sample'
    that include all the varibales key without any value and placeholder instead
    """
    with open(".env.secret", "r") as env_file:
        with open(".env.secret.sample", "w") as env_sample_file:
            for line in env_file:
                if line.strip() and not line.startswith("#"):
                    key = line.split("=")[0]
                    l = f"{key}=YOUR_{key}_HERE"
                    env_sample_file.write(f"{l}\n")
                else:
                    env_sample_file.write(f"{line}")


def add_generated_file_to_commit_stage():
    """_summary_: This function add the generated env file to the commit stage to be able to be commited with commit preformed later."""
    subprocess.run(["git", "add", "."])


if __name__ == "__main__":
    generate_env_sample()
    time.sleep(1)
    add_generated_file_to_commit_stage()
