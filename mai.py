
import random
import time

def decor(name):

    def function(fun):
        def wrapper(*args, **kwargs):
            start = time.time()
            fun(*args, **kwargs)
            result = time.time() - start
            res = str(result)
            print(result)
            with open("timess.csv", "a") as f:
                # f.write("Oper" + "," + "Time" + "," + "\n")
                f.write(name + "," + res + "," + "\n")
            return fun
        return wrapper
    return function


def add():
    res = random.randint(10, 100)
    print("my number generated is:   " + str(res))
    with open("profits.csv", "a") as f:
        # f.write("profit" + "," + "\n")
        f.write(str(res) + "," + "\n")

add()












