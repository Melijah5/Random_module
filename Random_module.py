
# ============================= Random module =============================

import random
def randInt(min = 0,max = 100):
    if max != 100 and min != 0:
        return round(random.random()*(max-min)+min)
    if min != 0:
        return round(random.random()*(100-min)+min)
    if max != 100:
        return round(random.random()*max)
    return round(random.random()*100)
print("Random number between 0 and 100 is % d" % (randInt()))
print("Random number between 50 and 50 is % d" % (randInt(max = 50)))
print("Random number between 50 and 100 is % d" % (randInt(min = 50)))
print("Random number between 50 and 100 is % d" % (randInt(min = 50, max = 500)))