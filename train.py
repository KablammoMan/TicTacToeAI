import ai
import time
start = time.time()
ai.train(10**6)
end = time.time()
print(f"Took {int((end - start)*100)/100}s")