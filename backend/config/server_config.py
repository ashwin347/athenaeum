import os
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = os.path.curdir
print(BASE_DIR)
static_files = StaticFiles(directory="static_files")
templates = Jinja2Templates(directory="static_files/html")