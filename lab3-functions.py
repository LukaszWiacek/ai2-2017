def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))
"""print_two()
#print_two() missing 2 required positional arguments: 'a' and 'b'
#>>> print_two(4, 1)
Arguments: 4 and 1
>>> print_two(41)
print_two() missing 1 required positional argument: 'b'
>>> print_two(a=4, 1)
print_two() got multiple values for argument 'a'
>>> print_two(4, 1, 1)
print_two() takes 2 positional arguments but 3 were given
>>> print_two(a=4, b=1)
Arguments: 4 and 1
>>> print_two(b=1, a=4)
Arguments: 4 and 1
>>> print_two(1, a=1)
print_two() got multiple values for argument 'a'
>>> print_two(4, 1, b=1)
print_two() got multiple values for argument 'b'
"""
def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
"""
>>> keyword_args(5)
a: 5
b: 1
c: X
d: None
>>> keyword_args(5, 8)
a: 5
b: 8
c: X
d: None
>>> keyword_args(5, 2, c=4)
a: 5
b: 2
c: 4
d: None
>>> keyword_args(5, 0, 1)
a: 5
b: 0
c: 1
d: None
>>> keyword_args(5, 2, d=8, c=4)
a: 5
b: 2
c: 4
d: 8
>>> keyword_args(5, 2, 0, 1, "")
keyword_args() takes from 1 to 4 positional arguments but 5 were given
>>> keyword_args(c=7, 1)
SyntaxError: non-keyword arg after keyword arg
>>> keyword_args(c=7, a=1)
a: 1
b: 1
c: 7
d: None
>>> keyword_args(5, 2, [], 5)
a: 5
b: 2
c: []
d: 5
>>> keyword_args(1, 7, e=6)
keyword_args() got an unexpected keyword argument 'e'
>>> keyword_args(1, c=7)
a: 1
b: 1
c: 7
d: None
>>> keyword_args(5, 2, b=4)
Keyword_args() got multiple values for argument 'b'

""" 
def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
"""
>>> variadic(2, 3, 5, 7)
Positional: (2, 3, 5, 7)
Keyword: {}
>>> variadic(1, 1, n=1)
Positional: (1, 1)
Keyword: {'n': 1}
>>> variadic(n=1, 2, 3)
non-keyword arg after keyword arg
>>> variadic()
Positional: ()
Keyword: {}
>>> variadic(cs="Computer Science", pd="Product Design")
Positional: ()
Keyword: {'pd': 'Product Design', 'cs': 'Computer Science'}
>>> variadic(cs="Computer Science", cs="CompSci", cs="CS")
SyntaxError: keyword argument repeated
>>> variadic(5, 8, k=1, swap=2)
Positional: (5, 8)
Keyword: {'k': 1, 'swap': 2}
>>> variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
Positional: (8, 3, 4, 5)
Keyword: {'k': 1, 'b': 'x', 'a': 5}
>>> variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
invalid syntax
>>> variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
invalid syntax
>>> variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})
Positional: ({'b': 'x', 'a': 5}, 'b', 'a')
Keyword: {'a': 5, 'b': 'x'}
"""
def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)

"""
all_together(2) - brak argumentu y
>>> all_together(2, 5, 7, 8, indent=False)
x: 2
y: 5
z: 7
nums: (8,)
indent: False
spaces: 4
options: {}
>>> all_together(2, 5, 7, 6, indent=None)
x: 2
y: 5
z: 7
nums: (6,)
indent: None
spaces: 4
options: {}
>>> all_together() - brak argumentu x y.
>>> all_together(indent=True, 3, 4, 5) - Nie poprawna kolejnośc argumentów
all_together(**{'indent': False}, scope='maximum') - Niepoprawna składnia
>>> all_together(dict(x=0, y=1), *range(10))
x: {'y': 1, 'x': 0}
y: 0
z: 1
nums: (2, 3, 4, 5, 6, 7, 8, 9)
indent: True
spaces: 4
options: {}
all_together(**dict(x=0, y=1), *range(10)) - Niepoprawna składnia
>>> all_together(*range(10), **dict(x=0, y=1)) - Wiele wartości do argumentu y
>>> all_together([1, 2], {3:4})
x: [1, 2]
y: {3: 4}
z: 1
nums: ()
indent: True
spaces: 4
options: {}
>>> all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'}) - wiele wartości do argumentu x
>>> all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
x: 8
y: 9
z: 10
nums: (2, 4, 6)
indent: True
spaces: 0
options: {'b': 'x', 'a': [4, 5]}
all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'}) - Niepoprawna składnia.

"""
def speak_excitedly(Str):
    pass

