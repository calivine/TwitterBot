import random
import time

class Timer:

    def sleep():
        sleep_seed = random.random()
        sleep_time = 60 * 100 * sleep_seed
        print("Sleeping for {:s} minutes\n".format(str(sleep_time//60)))
        time.sleep(sleep_time)
