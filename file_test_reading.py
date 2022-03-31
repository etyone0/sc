def read_with_split(filename, symbol):
    file = open(filename,'r')
    data = file.read()
    data_split = data.split(symbol)
    for element in data_split:
        print(element)
    file.close()
    return data_split