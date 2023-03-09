def fibonacci(nterms, x, y):
    if c < dur:
        z = x+y
        x=y
        y=z
        c += 1
        print("{:2} - {:9,}".format(nterms, x))
        fibonacci(dur, x, y)

c=0
nterms =35
x = 0
y = 1
fibonacci(nterms, x, y)