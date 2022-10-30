name = 'ahmed'
age = 27
salary = 1000.5
isLearn = True

print('my name is ' + name)

if name == 'ahmed':
    print("my age is " + str(age))

print('my salary is ' + str(salary))

if isLearn:
    print('Im Learn python '  + str(isLearn))


# TODO
# Comment

# Data Type
print(type(80))
print(type(88.8))
print(type('ahmed'))
print(type(True))
print(type(['ahmed',27]))
print(type(('ahmed',27)))
print(type({'name':'ahmed', 'age': 27}))

a,b = 12,'hi'
print(a)
print(b)

# help('keywords')

var = 'I-Love-Python-And-Java Android-And-Dart Flutter'
print(var.split('-', 4))
print(len(var.split('-',4)))

myName = ' Khalil Love Assel '
print(myName.center(22, '❤'))
print(myName.count('o'))

print(myName[1:8])

listA = ['ahmed', 'wasfe', 'mandil']
print(' '.join(listA))

resultOld = "My name is: %s and My age is: %d and salary is: %.2f" % (name, age, salary) # Old Way
resultNew = "My name is: {} and My age is: {} and salary is: {:.2f}".format(name, age, salary) # New Way
print(resultOld)
print(resultNew)

myNum = 10
print('My numberIs: {:d}'.format(myNum))
print('My numberIs: {:f}'.format(myNum))
print('My numberIs: {:.2f}'.format(myNum))

x,y,z = 10,20,30
print('Number {2:d} {0:f} {1:.2f}'.format(x,y,z))

userName = 'ahmed'
userAge = 54

print(f'user name is: {userName} and user age is: {userAge}' )

num1, num2 = 120, 15.5

print(float(num1))
print(int(num2))