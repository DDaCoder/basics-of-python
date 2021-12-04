## Countdown Program ##


# importing a module for Python; in this case, it is the time module
import time

# we set the step number to -1 so that it will countdown 1 in the prograam
for i in range(10, 0, -1):
    # using time.sleep(), we can set the time that we want for our program to pause
    time.sleep(1)
    print("T-minus",i)
    # the reason why we have this if loop is to print a message once the value of i gets to 1
    if i == 1:
        print("Blastoff!")