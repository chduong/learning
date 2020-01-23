# Execution of Code:
import time

start = time.time()

# Some Program

end = time.time()
elapsed_time = end - start
print(elapsed_time)


# For Functions
import profile

def fib(n):
    # from literateprograms.org
    # http://bit.ly/hlOQ5m
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq


profile.run('print(fib_seq(20)); print()')


# For Snippets
import timeit

# using setitem
t = timeit.Timer("print('main statement')", "print('setup')")

print('TIMEIT:')
print(t.timeit(2)) # returns the time it takes for 2 executions

print('REPEAT:')
print(t.repeat(3, 2)) # returns the time it takes to repeat the process 3 times for 2 executions each time.


# For Function Snippets
def someFunction():
    y = 3.1415
    for x in range(100):
        y = y ** 0.7
    return y

if __name__ == '__main__':
    print('TIMEIT:')
    print(timeit.timeit('someFunction()', setup='from __main__ import someFunction', number=1000)) # returns the time it takes for 100000 executions
