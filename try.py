# import random
# def g(f):
#     x=2
#     if f >0:
#         return f ,x
# a =list(range(1,963,6))
# print(a)
# b = []
# c = 'A'
# d=[]
with open('history_gbt.txt','r') as g:
    c = g.readlines()
# print(c)
# print(len(c))
x = 0
for i in c:
    if i == '\n':
        del c[x]
    x = x +1

print(len(c))
# print(c)
a= ''
for i in  range(240):
    a = a+c[i]
# print(a)

with open('c.txt','w') as g:
    g.write(a)

    # for i in range(1,963,6):
    #     if i in a:
    #         continue
    #     else:
    #         for x in range(i):
                # c = g.readlines()
        # c= c[:1]
        # if i not in a:
        # if  (c != 'A') or (c != 'B') or (c != 'C')or (c != 'D'):
                # b.append(i)
            # d.append(c)
# for i in range(1,961,6):
        # print(c[i-1])
        # d.append()
# print(b)
# print(d)

#     d = g.readlines()
#     # g.write('print')
# print(d)
#     # for i in range(3):
#     g.write('hello')
#     g.write('hello')
#     g.write('hello\n')
        # p = g.readline()
        # print(i)
    # print(p.strip())
    
# s =g(7)
# print(s)
# print(type(s))
    # a = random.randint(1,20)
    # print(a)

# li = list(range(1,22,6))
# for i in li:
# a=11
# print(f'I am {a}')