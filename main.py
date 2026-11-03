#Binary search


l = [8, 1, 2, 3, 5, 4, 6, 4, 6]

elm = int(input("Enter the element to be searched: "))

l.sort()

low = 0
high = len(l) - 1
flag = 0

while low <= high:
    mid = (low + high) // 2

    if l[mid] == elm:
        flag = 1
        print("Element found")
        break

    elif l[mid] < elm:
        low = mid + 1

    else:
        high = mid - 1

if flag == 0:
    print("Element is not there")
