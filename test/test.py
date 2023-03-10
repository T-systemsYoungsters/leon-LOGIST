nterm = 35
a = 0
b = 1
count = 0
def fibonacci(a,b,count, nterm):
    tmp = a
    a = b
    b += tmp
    count += 1
    print("{:2} -   {:9,}".format(count, a))
    if count < nterm: 
        fibonacci(a,b,count, nterm)

fibonacci(a, b, count, nterm)