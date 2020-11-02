# Two lists with friend names
list1 = ["Michael", "Anna", "Aiden", "John", "Max", "Amy", "Alice", "Mia", "Max", "John", "Aiden",]
list2 = ["Amy", "Max", "Anna", "Michael", "Aiden", "Anna", "Alice", "Anna", "Michael", "Amy", "Mia",]

# Empty list used to count number of friends
count = ["", "", "", "", "", "", "", ""]

# Outputs name and number of friends
i = 0

while i < 8:
    count[i] = list1.count(list1[i]) + list2.count(list1[i])
    print("%s has %s friends." % (list1[i], count[i]))
    i = i + 1
