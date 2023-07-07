import os


def env_files_count(directory: str) -> int:
    env_files = 0

    for file in os.listdir(directory):
        if file.endswith(".env"):
            env_files += 1

    return env_files
