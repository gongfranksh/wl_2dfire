import os


def make_dir(daily_file_folder):
    path = daily_file_folder.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

