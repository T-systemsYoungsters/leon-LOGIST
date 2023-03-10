1. 

````python
score = 41237
highscore = 1023407
 
print("Score:      {:9,}" .format(score) )
print("High score: {:9,}".format(highscore)) 
````

<br>

2. 
````python
for i in range(1,21):
    inv = 1/i
    print("1/{:<2} = {:.4}".format(i, inv))

````

3. 
````python
nterm = 35
a = 0
b = 1
count = 0
def fibonacci(a,b,count, nterm):
    tmp = a
    a = b
    b += tmp
    count += 1
    print("{:2} -    {:9,}".format(count, a))
    if count < nterm: 
        fibonacci(a,b,count, nterm)

fibonacci(a, b, count, nterm)
````
<br>

4. Also bei mir läuft das ziemlich schnell durch... bessere Hardware? Falls ich was