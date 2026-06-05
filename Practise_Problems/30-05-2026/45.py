# Use a for loop with range() to print numbers from 10 down to 1 (countdown).


import time  # import time module to use sleep function


for i in range(10,0,-1):
    print(i)
    time.sleep(1) # keeps a 1 sec gap between each print statement to create a countdown effect


    