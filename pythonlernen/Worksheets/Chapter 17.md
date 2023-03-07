1. 
````python
my_list = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]
tmp = my_list[7]
my_list[7] = my_list[6]
my_list[6] = tmp 
````

2. 
````python
my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]
tmp = my_list[3]
my_list[3] = my_list[0]
my_list[0] = tmp
````

3. Es soll die 70 mit der 32 getauscht werdeb, dabei wird tmp die 70 zugeordnet, danach wird die 32 durch die 70 ersetzt. Das Problem ist, dass die 32 hätte in tmp gespeichert werden sollen, oder man hätte die 70durch die 32 ersetzten sollen. Anschließend wird in die position wo 70 steht tmp gespeichert (Was ja 70 ist)
````python
my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]
temp = my_list[0]
my_list[0] = my_list[1]
my_list[1] = temp

# oder

my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]
temp = my_list[1]
my_list[1] = my_list[0]
my_list[0] = temp
````

4. 
[0, 74, 8, 98, 47, 62, 12, 11, 97, 60]<br>
[0, 8, 74, 98, 47, 62, 12, 11, 97, 60]<br>
[0, 8, 11, 98, 47, 62, 12, 74, 97, 60]<br>
[0, 8, 11, 12, 47, 62, 98, 74, 97, 60]<br>
[0, 8, 11, 12, 47, 62, 98, 74, 97, 60]<br>
[0, 8, 11, 12, 47, 60, 98, 74, 97, 62]<br>
[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]<br>
[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]<br>
[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]<br>
[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]<br>

5. 
[0, 92, 18, 47, 40, 58, 74, 36, 29, 25]<br>
[0, 18, 92, 47, 40, 58, 74, 36, 29, 25]<br>
[0, 18, 25, 47, 40, 58, 74, 36, 29, 92]<br>
[0, 18, 25, 29, 40, 58, 74, 36, 47, 92]<br>
[0, 18, 25, 29, 36, 58, 74, 40, 47, 92]<br>
[0, 18, 25, 29, 36, 40, 74, 58, 47, 92]<br>
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]<br>
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]<br>
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]<br>
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]<br>

6. 
[74, 92, 18, 47, 40, 58, 0, 36, 29, 25]<br>
[18, 74, 92, 47, 40, 58, 0, 36, 29, 25]<br>
[18, 47, 74, 92, 40, 58, 0, 36, 29, 25]<br>
[18, 40, 47, 74, 92, 58, 0, 36, 29, 25]<br>
[18, 40, 47, 58, 74, 92, 0, 36, 29, 25]<br>
[0, 18, 40, 47, 58, 74, 92, 36, 29, 25]<br>
[0, 18, 36, 40, 47, 58, 74, 92, 29, 25]<br>
[0, 18, 29, 36, 40, 47, 58, 74, 92, 25]<br>
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]<br>

7. 
[11, 37, 14, 50, 24, 7, 17, 88, 99, 9]<br>
[11, 14, 37, 50, 24, 7, 17, 88, 99, 9]<br>
[11, 14, 37, 50, 24, 7, 17, 88, 99, 9]<br>
[11, 14, 24, 37, 50, 7, 17, 88, 99, 9]<br>
[7, 11, 14, 24, 37, 50, 17, 88, 99, 9]<br>
[7, 11, 14, 17, 24, 37, 50, 88, 99, 9]<br>
[7, 11, 14, 17, 24, 37, 50, 88, 99, 9]<br>
[7, 11, 14, 17, 24, 37, 50, 88, 99, 9]<br>
[7, 9, 11, 14, 17, 24, 37, 50, 88, 99]<br>

8. min_pos speichert die aktuell kleinste Position(am Anfang die erste) aus dem Array um diese dann mit dem scan_pos vergleichen zu können. Pro durchlauf wird min_pos mit cur_pos getauscht.

9. cur_pos ist die aktuelle Position und geht einmal von links nach rechts durch das Array durch. Ausgehend von der cur_pos wird dann weiter nach rechts geschaut ob ein kleineres Element in dem Array vorhanden ist, in dem man die folgenden Elemente mit min_pos vergleicht. 

10. scan_pos geht pro Schritt weiter mit current pos durch das gesamte restliche Array durch

11. Am Anfang ist key_pos und value der zweite Eintrag in der liste also list[1]. Pro durchlauf geht die key_pos +1 und die key_value ist der passende Eintrag in dem Array. Von key_pos wird dann immer nach links geschaut also richtung Listenbeginn und solange getauscht, bis die Zahlen links von key_pos nur kleiner sind. 

12. scan_pos geht von der key_pos von rechts nach links, bis es am anfang der Liste ist oder auf ein Element trifft, welches kleiner ist als key_value

13. 
````python
import random
 
 
def selection_sort(list):
    """ Sort a list using the selection sort """
    inner_count = 0
    outer_count = 0
    # Loop through the entire array
    for cur_pos in range(len(list)):
        outer_count += 1
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos
 
        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(list)):
            inner_count += 1
            # Is this position smallest?
            if list[scan_pos] < list[min_pos]:
 
                # It is, mark this position as the smallest
                min_pos = scan_pos
 
        # Swap the two values
        temp = list[min_pos]
        list[min_pos] = list[cur_pos]
        list[cur_pos] = temp
 
    print("#### selection sort count ####")
    print(f"Inner Count {inner_count}, Outer Count {outer_count}")
 
def insertion_sort(list):
    """ Sort a list using the insertion sort """
    inner_count = 0
    outer_count = 0
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(list)):
        outer_count += 1
        # Get the value of the element to insert
        key_value = list[key_pos]
 
        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1
 
        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            inner_count += 1
            list[scan_pos + 1] = list[scan_pos]
            scan_pos = scan_pos - 1
 
        # Everything's been moved out of the way, insert
        # the key into the correct location
        list[scan_pos + 1] = key_value
    print("#### insertion sort count ####")
    print(f"Inner Count {inner_count}, Outer Count {outer_count}")
 
# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(list):
    for item in list:
        print("{:3}".format(item), end="")
    print()
 
# Create two lists of the same random numbers
list1 = []
list2 = []
list_size = 100
for i in range(list_size):
    new_number = random.randrange(100)
    list1.append(new_number)
    list2.append(new_number)
 
# Print the original list
print_list(list1)
 
# Use the selection sort and print the result
print("Selection Sort")
selection_sort(list1)
print_list(list1)
# Use the insertion sort and print the result
print("Insertion Sort")
insertion_sort(list2)
print_list(list2)
````