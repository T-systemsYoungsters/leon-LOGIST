import random

def min3(a,b,c):
    if a <= b and a<=c:
        return a
    elif b<=a and b<=c:
        return b 
    else:
        return c

print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))
print()
print()

def box(height, width):
    for i in range(height):
        for j in range(width):
            print("*" ,end ="")
        print()


box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across


# Da das array bei 0 anfängt zu zählen ist die erste Stelle die 0, wenn man mit 1 anfangen will kann man einfach eine count variable die bei jedem durchlauf der forschleife um 1 erhöht wird hinzufügen
def find(list, g):
    for i in range(len(list)):
        if g == list[i]:
            print(g," gefunden an der Stelle ", i)
           
my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
 
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

def create_list(size):
    list =[]
    for i in range(size):
        list.append(random.randrange(1,7))
    return list

my_list = create_list(5)
print(my_list)

def count_list(list, number):
    count=0
    for i in range(len(list)):
        if number == list[i]:
            count +=1
    return count

count = count_list([1,2,3,3,3,4,2,1],3)
print(count)

def average_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)

avg = average_list([1,2,3])
print(avg)


list = create_list(10000)
for i in range(1,7):
    print(count_list(list, i))

print(average_list(list))
