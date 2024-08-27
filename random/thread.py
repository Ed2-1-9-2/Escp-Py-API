from time import sleep
from threading import Thread

def a():
  sleep(5)
  print("a")

def y(y:str):
  sleep(5)
  print(y)

Thread(target=a).start()
Thread(target=y, args=["test"]).start()