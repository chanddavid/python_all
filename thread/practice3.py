import time

start= time.perf_counter()
print("hello")
end=time.perf_counter()
print(f'finished in {round(end-start,2)} second')

