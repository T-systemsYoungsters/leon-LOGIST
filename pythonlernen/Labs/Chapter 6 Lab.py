#Chapter 6: Back to Looping: Lab 6: Loopy Lab

#6.1

num = 10

for row in range(1,10):
    for column in range(row):
        print(num, end =" ")
        num +=1
    print()
