import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))



# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def linear_search(list, s, count):
    i = 0
    while i < len(list) and list[i] != s:
        i += 1
    if not (i<len(dictionary_list)):
          print(f"Wort nicht gefunden: {s}, line {count}")
    
def binary_search(list, s, count):
    lower_bound = 0
    upper_bound = len(list)-1
    found = False
    
    while lower_bound < upper_bound and not found:
        middle_pos = ((lower_bound+upper_bound) // 2)
        if list[middle_pos] < s:
            lower_bound = middle_pos+1
        elif list[middle_pos] > s:
            upper_bound = middle_pos
        else:
            found = True
        
    if not found:
        print(f"Wort wurde nicht gefunden: {s}, line{count}")

dictionary = open("dictionary.txt")

dictionary_list = []

for line in dictionary:
    line = line.strip()
    dictionary_list.append(line)

dictionary.close()

print("--- Linear Search ---")
alice_in_wonderland_1 = open("AliceInWonderLand200.txt")
line_count = 0
for line in alice_in_wonderland_1:
    words = split_line(line)
    line_count += 1
    for word in words:
        linear_search(dictionary_list, word.upper(), line_count)
alice_in_wonderland_1.close()


print("--- Binary Search ---")
alice_in_wonderland_1 = open("AliceInWonderLand200.txt")

line_count = 0
for line in alice_in_wonderland_1:
    words = split_line(line)
    line_count += 1
    for word in words:
        binary_search(dictionary_list, word.upper(), line_count)
alice_in_wonderland_1.close()

print("###Alice In Wonderland full version###")
print("--- Binary Search ---")

alice_in_wonderland_2 = open("AliceInWonderLand.txt")
line_count = 0
for line in alice_in_wonderland_2:
    words = split_line(line)
    line_count += 1
    for word in words:
        binary_search(dictionary_list, word.upper(), line_count)
alice_in_wonderland_2.close()