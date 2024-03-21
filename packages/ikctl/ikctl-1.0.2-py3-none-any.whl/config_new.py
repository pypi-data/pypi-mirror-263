import pathlib
from os import path
from envyaml import EnvYAML

config = {
    'path_kits':'/'
}

def load_config(directory):
    """ Load Config ikctl """
    print(directory)
    file = open(str(directory) + "/config", "a+", encoding="utf-8")
    file.seek(0) 
    data = file.readlines()
    file.close()
    print(data)

       

def create_folder_and_config_file(folder):
    """Create Folder if not exist"""
    pathlib.Path.mkdir(folder)
    p = pathlib.Path(folder)
    data = "Hola Mundo"
    file = open(str(folder) + "/config", "a+", encoding="utf-8")
    file.seek(0)
    file.writelines(data)
    file.close()
    for f in p.glob("config"):
        print(f)

# Home path
home = pathlib.Path.home()

# Build path join '.ikctl'
path_config_file = home.joinpath('.ikctl')

# Check if exist directory
if path.exists(path_config_file):
    load_config(path_config_file)
else:
    create_folder_and_config_file(path_config_file)
