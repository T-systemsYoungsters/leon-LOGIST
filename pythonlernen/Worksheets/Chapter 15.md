linear search<br>

1. mindestens 1 mal <br>

2. n-mal <br>

3. n elemente <br>

4. n/2 <br>

5. 
````python
# --- Put your definition for linear_search right below:
def linear_search(list, s):
    i = 0
    while i < len(list) and list[i] != s:
        i += 1
    if i < len(list):
        return i
    else:
        return -1
# --- Now if the function works, all these tests should pass:
````
<br>

binary search <br>

1. mindestens 1 mal <br>

2. ld(n) mal <br>

3. ld(n) mal <br>

4. <br>

5. 
````python
def binary_search(list, s):
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
        
    if found:
        return middle_pos
    else:
        return -1
````
<br>

6. 
````python
def detect_positive(list):
    found = False
    for element in list:
        if element > 0:
            found = True
    return found
````