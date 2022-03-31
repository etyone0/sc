from file_test_reading import read_with_split
import matplotlib.pyplot as pld
temp = read_with_split('text.txt', '\n')
temp_int = []
days = []
i = 1
for elem in temp:
    temp_int.append(int(elem))
    days.append(i)
    i = i+1
pld.plot(days, temp_int)
pld.show()