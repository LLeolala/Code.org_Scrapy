import os

def is_file_live(file_path):
    return os.path.exists("cookies.pkl")