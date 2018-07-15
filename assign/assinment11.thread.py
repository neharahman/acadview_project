'''Create a threading process such that it sleeps for 5 seconds and then prints out a message.'''
import threading as thread_procsse
import time
def threa():
    print(thread_procsse.currentThread().getName(), 'BORN')
    time.sleep(10)
    print('After 10 seconds thread is back')


ob = thread_procsse.Thread(name="10 seconds of sleep", target=threa)
ob.start()


#2
import threading as thread_procsse
import time

# Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between.
def threa1():
    for i in range(1,10):
        print(thread_procsse.currentThread().getName(), i)
        time.sleep(1)


obj = thread_procsse.Thread(name="\nPrinting 1 to 10:", target=threa1)
obj.start()


'''

# Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
# Delay goes like 2sec-4sec-6sec-8sec-10sec
'''
import threading as thread_procsse
import time

def delay_print():
    arr = [1, 2, 3]
    delay = 2
    for i in arr:
        print(thread_procsse.currentThread().getName(), i)
        time.sleep(delay)
        delay += 2

obj1 = thread_procsse.Thread(name="Elements of arr: ", target=delay_print)
obj1.start()

'''# Q4. Call factorial function using thread.'''
import threading as thread_procsse 
def fact(n):
    a = 1
    for i in range(n, 0, -1):
        a *= i
    print(thread_procsse.currentThread().getName(), a)


n = int(input("Enter number to calculate factorial of "))
t = thread_procsse.Thread(name="factorial is: ", target=fact, args=(n,))
t.start()
