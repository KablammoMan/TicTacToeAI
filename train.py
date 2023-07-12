import ai
import time
start = time.time()
ai.train(10000)
end = time.time()
print(f"Took {end - start}s")