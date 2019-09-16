import time
import challenge21
import random as rd


def sleep_random():

    time.sleep(rd.randint(0, 20))
    seed = int(time.time())
    time.sleep(rd.randint(0, 10))

    mt = challenge21.MT19937(seed)

    return mt.random()


def crack_time(random):

    seed = int(time.time())
    mt = challenge21.MT19937(seed)

    while mt.random() != random:
        seed -= 1
        mt = challenge21.MT19937(seed)

    return seed


if __name__ == "__main__":

    random = sleep_random()
    print(crack_time(random))
