import time

def fibo():
  f = 0
  f0 = 0
  f1 = 1
  while True:
    f=f0 + f1
    f0 = f1
    f1 = f
    yield f
    
    

az = fibo()
for i in fibo():
  print(next(az))
  time.sleep(0.5)