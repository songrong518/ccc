import time

print(str(time.localtime()))
time.sleep(1)

for i in range(4):
    print(time.strftime("%Y-%Y-%d: %H:%M:%S",time.localtime(time.time())))
    time.sleep(1)