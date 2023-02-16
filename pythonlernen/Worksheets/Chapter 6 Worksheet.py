# Chapter 6: Back to Looping : Chapter 06 Worksheet

#1 Guess: 0,2,4,6,8 ->richitg
"""
x = 0
while x < 10:
    print(x)
    x = x + 2
"""

#2 1,2,4,8,16,32 -> richtig
"""
x = 1
while x < 64:
    print(x)
    x = x * 2
"""

#3 da x =0 ist und immer nur addiert wird

#4 5,4,3,2, 1, 0 da x immer um eins niedriger wird und "1" für blast off steht und nicht die Zahl 1

#5
"""
x = float(input("Enter a number greater than zero: "))
while x <= 0:
    print("Too small. Enter a number greater than zero: ")
    x = float(input("Enter a number greater than zero: "))
"""

#6
"""
x = 10
 
while x > 0:
    print(x)
    x -= 1
 
print("Blast-off")
"""

#7 das i+=1 ist unnötig, da das die for schleife automatisch macht
"""
i = 0
for i in range(10):
    print(i)
"""

#8 In Sample 1 wird x 10 mal erhöht und dann nochmal 10 mal erhöt also x=20
    # In Sample 2 wird x 10 mal erhöt und jedesmal wenn es in dieser schleife um 1 erhöht wird nochmal um 10
    #also
"""
# Sample 1
x = 0
for i in range(10):
    x += 1
for j in range(10):
    x += 1
print(x)
 
# Sample 2
x = 0
for i in range(10):
    x +=1                   #0+1, 11+1, 22+1...
    for j in range(10):
        x += 1              #1+10, 12+10, 23+10...
print(x)
"""
