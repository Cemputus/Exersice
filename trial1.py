#
def degree_converter():
    degree = float(input('Enter the Celsius degrees : '))

    converter(degree)
    fahre = converter(degree)
    print('%.2f degrees Celsius is equal to %.2f degrees Fahrenheit' % (degree, fahre))

def converter(C):
    fahre = (C * 9/5) + 32
    return fahre



degree_converter()