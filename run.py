import os
import threading
print(os.path.dirname(os.path.abspath(__file__)))

def run_backend():
    try:
        os.chdir('backend')
    except FileNotFoundError:
        os.chdir('../backend')
    os.system(r'uvicorn main:app --reload')

def run_frontend():
    os.chdir(os.path.dirname(os.path.abspath(__file__))+'/frontend')
    os.system('npm run dev')
    
backend = threading.Thread(target=run_backend, name='backend')
frontend = threading.Thread(target=run_frontend, name='frontend')

backend.start()
frontend.start()
print('开始运行')

backend.join()
frontend.join()
print('运行结束')
