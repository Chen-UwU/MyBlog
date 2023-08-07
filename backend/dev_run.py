import os
try:
    os.chdir('backend')
except FileNotFoundError:
    os.chdir('../backend')
os.system(r'uvicorn main:app --reload')