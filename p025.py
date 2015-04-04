
length = 1000
fib = 1
fib_one = 1
fib_two = 0
count = 1
while len(str(fib)) < length:
    fib = fib_one + fib_two
    prev = fib
    fib_two = fib_one
    fib_one = prev
    count += 1

print count
