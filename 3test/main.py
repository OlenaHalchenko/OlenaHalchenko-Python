from array import array
a = array('i', [1, 2, 3, 4, 5, 6, 33, 7, 25, 37, 99, 12, 77, 45, 9, 969, 22, 10, 765])
for i in a:
    if (i % 3 == 0) and not i == 0:
        print(i)
input("Press ENTER to exit")