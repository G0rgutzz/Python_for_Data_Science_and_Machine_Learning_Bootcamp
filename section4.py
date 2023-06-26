import numpy as np

d = {'k1': '1', 'k2': '2', 'k3': '3', 'k4': '4', 'k5': '5', 'k6': [1, 2, 3, 4]}
print(d['k6'])
a = set([1, 2, 3, 1, 2, 3, 4, 5, 6, 2, 3, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 3, 2, 4, 0, 9, 0, 9, 8, 0, 7, 7, 6])
print(a)
b = np.random.randint(1, 10, 200)
print(b)
print(set(b))

c = []
for num in a:
    c.append(num*num)
e = [num*num for num in a]  # those 2 methods are identical
print(c)
print(e)
print(e == c)

# map function


def multiply(arg1):
    return arg1*arg1


f = [1, 2, 3, 4, 5]
print(list(map(multiply, f)))
# lambda expression makes it easier to write functions, type lambda args and values you want to return
lista = list(map(lambda arg1: arg1*arg1, f))  # use it mostly with map
print(lista)

# filter

print(list(filter(lambda arg1: arg1 % 2 == 0, f)))  # filter needs to have boolean value (true or false)
# list gives values where it is true

# tupple unpacking
x = [(1, 2), (3, 4), (5, 6)]
for (k, l) in x:
    print(k)

print(7**4)
s = "Hi there Sam!"
g = s.split()
g[2] = "dad"
print(g)
planet = "Earth"
diameter = 12732
print("The diameter of %s is %s" %(planet, diameter))
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2])
h = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
print(h['k1'][3]['tricky'][3]['target'][3])
z = "user@domain.com"
print(z.split('@')[1])
p = 'is there a dog here?'


def FindDog(p):
    return 'dog' in p.lower().split()


print(FindDog(p))


def countdog(p):
    j = 0
    for i in p.lower().split():
        if i == 'dog':
            j += 1
    return j


print(countdog(p))
r = ['soup', 'salad', 'dog', 'cat', 'great']
lst1 = list(filter(lambda arg1: arg1[0] == 's', r))  # use it mostly with map
print(lst1)


def Ticket(q, birthday):
    if birthday:
        if q <= 65:
            print('no ticket')
        elif q <= 85:
            print('small ticket')
        else:
            print('big ticket')
    else:
        if q <= 60:
            print('no ticket')
        elif q <= 80:
            print('small ticket')
        else:
            print('big ticket')


birthday = True
q = 85
Ticket(q, birthday)
