
def sort(list):
    for i in range(5):
        min = i
        for j in range(i,6):
            if list[j] < list[min]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp



list = [6,7,4,90,34,56]
sort(list)
print(list)
