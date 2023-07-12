import ai
import time
conf = ai.read_conf()
start = time.time()
ai.train(conf["train"])
end = time.time()
print(f"Took {int((end - start)*100)/100}s")