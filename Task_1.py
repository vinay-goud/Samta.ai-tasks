def calculate_area(length,width):
    if length==width:
        return 'This is a square!'
    else:
        return length*width

length=int(input('Enter length'))
width=int(input('Enter width'))
print(calculate_area(length,width))
