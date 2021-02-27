import threading
import time

def calc_square(nums):
    print("calculate square numbers")
    for n in nums:
        time.sleep(0.2)
        print("square:", n*n)

def calc_cube(nums):
    print("calculate cube of numbers")
    for n in nums:
        time.sleep(0.2)
        print("cube:", n*n*n)

arr = [2,3,8,9]

t = time.time()

# Instead of calling the functions one after each other
# We create threads with tasks with our functions
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

# Start threads
# Executes the two funcs in parallel
t1.start()
t2.start()

# Wait until the threads are done
t1.join()
t2.join()


print("Done in:", time.time()-t)
print("Done with all work!")

def example_times2(num):
    time.sleep(0.5)
    return num * 2

for i in range(10):
    th = threading.Thread(target=example_times2, args=(i,))
    th.start()
    print("Current Threads: %i." % threading.active_count())
