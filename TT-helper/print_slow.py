from time import sleep

def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.1)
    print() # go to new line

print_slow("Slow print function")
