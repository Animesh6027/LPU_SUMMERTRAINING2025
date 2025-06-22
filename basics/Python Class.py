# Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
# Enter "help" below or click "Help" above for more information.
# s1='Hello there !!'
# s1
# 'Hello there !!'
# s1[0]
# 'H'
# s1[7]
# 'h'
# s1[5]
# ' '
# s1[-1]
# '!'
# s1[-5]
# 'r'
# id(s1)
# 2448965622576
# s1='hello'
# s1
# 'hello'
# id(s1)
# 2448929162224
# s1='hi'
# id(s1)
# 140726336417664
# s1='India is my country'
# s1
# 'India is my country'
# s1[0:5]
# 'India'
# s1[5:]
# ' is my country'
# s1[:7]
# 'India i'
# s1[::2]
# 'Idai ycuty'
# s1[::-1]
# 'yrtnuoc ym si aidnI'
# s1[5:15:1]
# ' is my cou'
# s1[5:15:2]
# ' sm o'
# s1{:15:3]
# SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
# s1[:15:3]
# 'Iiimc'
# s1[-14:-2:3]
# '   u'
# s1.upper()
# 'INDIA IS MY COUNTRY'
# s1.lower()
# 'india is my country'
# s1.upper()
# 'INDIA IS MY COUNTRY'
# s1.count()
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     s1.count()
# TypeError: count expected at least 1 argument, got 0
# s1.count('i')
# 2
# s1.count('i',5,14)
# 1
# s1.endswith('y')
# True
# s1.endswith('s m')
# False
# s1.endswith('s', 'm')
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     s1.endswith('s', 'm')
# TypeError: slice indices must be integers or None or have an __index__ method
# s1.endswith('s m')
# False
# s1.find('u')
# 14
# s1.index('m')
# 9
# s1.find('m')
# 9
# s1.isalpha()
# False
# s1.isalnum()
# False
# s1.replace('y', 'Y')
# 'India is mY countrY'
# s1
# 'India is my country'
# s1.startswith('i')
# False
# s1.startswith('I')
# True
# s1.split(sep=',')
# ['India is my country']
# s1.split(",")
# ['India is my country']
# s1.split()
# ['India', 'is', 'my', 'country']
# s1.rfind('i')
# 6
# s1.lfind('i')
# Traceback (most recent call last):
#   File "<pyshell#48>", line 1, in <module>
#     s1.lfind('i')
# AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
# txt1="My name is {fname} and my age is {age).".format(fname="John", age=22)
# Traceback (most recent call last):
#   File "<pyshell#49>", line 1, in <module>
#     txt1="My name is {fname} and my age is {age).".format(fname="John", age=22)
# ValueError: expected '}' before end of string
# txt1="My name is {fname} and my age is {age}.".format(fname="John", age=22)
# txt1
# 'My name is John and my age is 22.'
# text='I have {:<10} brothers'
# print(text.format(2))
# I have 2          brothers
# text='I have {:>10} brothers'
# print(text.format(2))
# I have          2 brothers
# text='I have {:^10} brothers'
# print(text.format(2))
# I have     2      brothers
# h='the population is {:,} billions.'
# print(h.format(80000000000))
# the population is 80,000,000,000 billions.
# g='the temp varies from {:+} to {:+} celcius.'
# print(g.format(-3, 25))
# the temp varies from -3 to +25 celcius.
# s='i have {:,^+10} brothers'
# print(s.format(646485))
# i have ,+646485,, brothers
# s='i have {:^+10,} brothers'
# print(s.format(646485))
# i have  +646,485  brothers
# s='i have {:^+10_} brothers'
# print(s.format(646485))
# i have  +646_485  brothers
# bin='the bin rep of {} is {0:b}.'
# print(bin.format(5))
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     print(bin.format(5))
# ValueError: cannot switch from automatic field numbering to manual field specification
# bin='the bin rep of {0} is {0:b}.'
# print(bin.format(5))
# the bin rep of 5 is 101.
# x = None
# if x is None:
#     print('x is none')

    
# x is none

# occ='student'
# role'btech'
# SyntaxError: invalid syntax
# role='btech'
# print(f'I am a {occ} and I study {role}')
# I am a student and I study btech
# print(f'I am a {occ} and I study {role :>10}')
# I am a student and I study      btech
# print(f'I am a {occ} and I study {20 :>10.5f}')
# I am a student and I study   20.00000
# basiclist=[10,20,30,40,50,60]
# basiclist
# [10, 20, 30, 40, 50, 60]
# type(basiclist)
# <class 'list'>
# basiclist]3]
# SyntaxError: unmatched ']'
# basiclist]\[3]
# SyntaxError: unmatched ']'
# basiclist[3]
# 40
# basiclist[-1]
# 60
# basiclist[-1]=70
# basiclist
# [10, 20, 30, 40, 50, 70]
# basiclist[-4:-1]
# [30, 40, 50]
# basiclist[::2]
# [10, 30, 50]
# basiclist2=['a','hi','hello','hey']
# basiclist2
# ['a', 'hi', 'hello', 'hey']
# basiclist2[2]
# 'hello'
# basiclist2[2][2]
# 'l'
# basiclist.insert(5, 60)
# basiclist
# [10, 20, 30, 40, 50, 60, 70]
# basiclist.append(80)
# basiclist
# [10, 20, 30, 40, 50, 60, 70, 80]
# basiclist3=['hi',32,'hey',True,567]
# basiclist3
# ['hi', 32, 'hey', True, 567]
# basiclist3[2][1]
# 'e'
# basiclist3.reverse()
# basiclist3
# [567, True, 'hey', 32, 'hi']
# len(basiclist3)
# 5
# basiclist3.count(0)
# 0
# basiclist3.count(32)
# 1
# basiclist3.pop()
# 'hi'
# basiclist3
# [567, True, 'hey', 32]
# basiclist.sort()
# basiclist
# [10, 20, 30, 40, 50, 60, 70, 80]
# basiclist.sort(reverse=True)
# basiclist
# [80, 70, 60, 50, 40, 30, 20, 10]
# basiclist.sort(reverse=True)
# basiclist
# [80, 70, 60, 50, 40, 30, 20, 10]
# basiclist
# [80, 70, 60, 50, 40, 30, 20, 10]
# basiclist.sort()
# basiclist
# [10, 20, 30, 40, 50, 60, 70, 80]
# basiclist.reverse()
# basiclist
# [80, 70, 60, 50, 40, 30, 20, 10]
# basiclist.extend(90,100,110)
# Traceback (most recent call last):
#   File "<pyshell#122>", line 1, in <module>
#     basiclist.extend(90,100,110)
# TypeError: list.extend() takes exactly one argument (3 given)
# basiclist.extend([90,100,110])
# basiclist
# [80, 70, 60, 50, 40, 30, 20, 10, 90, 100, 110]
# marks=(88,69,75,84,95)
# marks
# (88, 69, 75, 84, 95)
# type(marks)
# <class 'tuple'>
# marks[1]
# 69
# marks[-3]
# 75
# dummy=(1,2,2,3,3)
# dummy
# (1, 2, 2, 3, 3)
# dummy2=('hi','hello',22,True)
# dummy2
# ('hi', 'hello', 22, True)
# dummy2[1][2]
# 'l'
# marks.count(84)
# 1
# marks.index(2)
# Traceback (most recent call last):
#   File "<pyshell#136>", line 1, in <module>
#     marks.index(2)
# ValueError: tuple.index(x): x not in tuple
# marks.index(84)
# 3
# marklist=list(marks)
# marklist
# [88, 69, 75, 84, 95]
# batup=tuple(basiclist)
# batup
# (80, 70, 60, 50, 40, 30, 20, 10, 90, 100, 110)
# batup.sort()
# Traceback (most recent call last):
#   File "<pyshell#142>", line 1, in <module>
#     batup.sort()
# AttributeError: 'tuple' object has no attribute 'sort'
# id={101,102,103,101,102,104}
# id
# {104, 101, 102, 103}
# type(id)
# <class 'set'>
# set1={1,2,3,"hello")
# SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
# set1={1,2,3,"hello"}
# set1
# {'hello', 1, 2, 3}
# set1={1,2,3,True,'hello'}
# set1
# {'hello', 1, 2, 3}
# set1={1,2,3,False,'hello'}
# set1
# {False, 1, 2, 3, 'hello'}
# id.add{110}
# SyntaxError: invalid syntax
# id.add(110)
# id
# {101, 102, 103, 104, 110}
# id.pop()
# 101
# id
# {102, 103, 104, 110}
# id.union(set1)
# {False, 1, 2, 3, 102, 103, 104, 110, 'hello'}
# >>> id.intersection(set1)
# set()
# >>> set1.add(102)
# >>> set1
# {False, 1, 2, 3, 102, 'hello'}
# >>> id.intersection(set1)
# {102}
# >>> it=id & set1
# >>> it
# {102}
# >>> dict={1:'aba',2:'qbc',3:'abc'}
# >>> dict
# {1: 'aba', 2: 'qbc', 3: 'abc'}
# >>> dict[3]
# 'abc'
# >>> thisdict = {
# ...   "brand": "Ford",
# ...   "model": "Mustang",
# ...   "year": 1964
# ... }
# >>> thisdict
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# >>> thisdict[brand]='Jeep'
# Traceback (most recent call last):
#   File "<pyshell#170>", line 1, in <module>
#     thisdict[brand]='Jeep'
# NameError: name 'brand' is not defined
# >>> thisdict['brand']='Jeep'
# >>> thisdict
# {'brand': 'Jeep', 'model': 'Mustang', 'year': 1964}
# >>> thisdict.get('model')
# 'Mustang'
# >>> thisdict.keys()
# dict_keys(['brand', 'model', 'year'])
# >>> thisdict.items()
# dict_items([('brand', 'Jeep'), ('model', 'Mustang'), ('year', 1964)])
# >>> dict.clear()
# >>> dict
# {}
