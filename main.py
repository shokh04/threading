import threading
import time

fruits = list(('apple', 'orange', 'banana'))
fruits_rezerv = list()

def fruits_func():
    for fruit in fruits:
        print(fruit)
        time.sleep(1)



def fruits_append():
    for fruit in fruits:
        fruits_rezerv.append(fruit)
        print(fruits_rezerv)
        time.sleep(3)



t1 = threading.Thread(target=fruits_func)
t2 = threading.Thread(target=fruits_append)

t1.start()
t2.start()

t1.join()
t2.join()