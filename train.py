import ai
import time
conf = ai.read_conf()
poss = ai.read_poss()
ai.train(conf["train"], poss, conf)
print(f"Finished Training!")
