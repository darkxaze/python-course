import time
from multiprocessing import Process

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello,{user_input}'
    print(greet)
    print(f'ask_user,{time.time()-start}')

def complex_calculation():
    start = time.time()
    print('started calculating...')
    [x**2 for x in range(200000)]
    print(f'complex_calculation,{time.time()-start}')

start = time.time()
ask_user()
complex_calculation()
print(f'single thread total timer: {time.time()-start}')

process = Process(target=complex_calculation)
process.start()
start = time.time()

ask_user()
process.join()

print(f'Two thread total time: {time.time() - start}')