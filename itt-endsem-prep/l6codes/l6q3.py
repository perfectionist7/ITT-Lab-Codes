def sort(list):
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[j] > list[i]:
                list[i], list[j] = list[j], list[i]
    return list


list1 = ["vishay", "rohit", "ayush", "bhavnish"]
print(sort(list1))
