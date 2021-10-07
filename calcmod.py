from math import pi

def area():
    while True:
        try:
            length = int(input("Enter the length: "))
            width = int(input("Enter the width: "))
            break
        except:
            print ('Please enter a number')
            continue

    squarefeet = ('Area = '+str(length*width))
    return squarefeet


def circ():
    while True:
        try:
            radius = int(input("Enter the radius: "))
            break
        except:
            print ('Please enter a number')
            continue
    circumference = ('Circumference = '+str(2*pi*radius))
    return circumference