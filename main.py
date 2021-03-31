numbers = '1,100,15,17,3,221,9,5,7,2,8,11'
result = {}
numbers.split(',')
for number in numbers:
    number = int(number)
    result[number]= number ** 3
    print