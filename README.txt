## Plik list1.py
```
match_ends
 OK  got: 3 expected: 3
 OK  got: 2 expected: 2
 OK  got: 1 expected: 1
front_x
 OK  got: ['xaa', 'xzz', 'axx', 'bbb', 'ccc'] expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
 OK  got: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'] expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
 OK  got: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
sort_last
 OK  got: [(2, 1), (3, 2), (1, 3)] expected: [(2, 1), (3, 2), (1, 3)]
 OK  got: [(3, 1), (1, 2), (2, 3)] expected: [(3, 1), (1, 2), (2, 3)]
 OK  got: [(2, 2), (1, 3), (3, 4, 5), (1, 7)] expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
```
## Plik list2.py
```
remove_adjacent
 OK  got: [1, 2, 3] expected: [1, 2, 3]
 OK  got: [2, 3] expected: [2, 3]
 OK  got: [] expected: []
linear_merge
 OK  got: ['aa', 'bb', 'cc', 'xx', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
 OK  got: ['aa', 'bb', 'cc', 'xx', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
 OK  got: ['aa', 'aa', 'aa', 'bb', 'bb'] expected: ['aa', 'aa', 'aa', 'bb', 'bb']
```
## Plik string1.py
```
donuts
 OK  got: 'Number of donuts: 4' expected: 'Number of donuts: 4'
 OK  got: 'Number of donuts: 9' expected: 'Number of donuts: 9'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
both_ends
 OK  got: 'spng' expected: 'spng'
 OK  got: 'Helo' expected: 'Helo'
 OK  got: '' expected: ''
 OK  got: 'xyyz' expected: 'xyyz'
fix_start
 OK  got: 'ba**le' expected: 'ba**le'
 OK  got: 'a*rdv*rk' expected: 'a*rdv*rk'
 OK  got: 'goo*le' expected: 'goo*le'
 OK  got: 'donut' expected: 'donut'
mix_up
 OK  got: 'pox mid' expected: 'pox mid'
 OK  got: 'dig donner' expected: 'dig donner'
 OK  got: 'spash gnort' expected: 'spash gnort'
 OK  got: 'fizzy perm' expected: 'fizzy perm'
```
## Plik string2.py
```
verbing
 OK  got: 'hailing' expected: 'hailing'
 OK  got: 'swimingly' expected: 'swimingly'
 OK  got: 'do' expected: 'do'
not_bad
 OK  got: 'This movie is good' expected: 'This movie is good'
 OK  got: 'This dinner is good!' expected: 'This dinner is good!'
 OK  got: 'This tea is not hot' expected: 'This tea is not hot'
 OK  got: "It's bad yet not" expected: "It's bad yet not"
```
## Plik lab1-warmup.py

helloworld()
    "Hello, world!"

board()
      |  |  
    --------
      |  |  
    --------
      |  |  
    
tictactoe()
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
    ========+========+========
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
    ========+========+========
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--
      |  |  H  |  |  H  |  |  
    --+--+--H--+--+--H--+--+--    

multiples()
    0 3 5 6 9 10 12 15 18 20 21 24 25 27 30 33 35 36 39 40 42 45 48 50 51 54 55 57 60 63 65 66 69 70 72 75 78 80 81 84 85 87 90 93 95 96 99 100 102 105 108 110 111 114 115 117 120 123 125 126 129 130 132 135 138 140 141 144 145 147 150 153 155 156 159 160 162 165 168 170 171 174 175 177 180 183 185 186 189 190 192 195 198 200 201 204 205 207 210 213 215 216 219 220 222 225 228 230 231 234 235 237 240 243 245 246 249 250 252 255 258 260 261 264 265 267 270 273 275 276 279 280 282 285 288 290 291 294 295 297 300 303 305 306 309 310 312 315 318 320 321 324 325 327 330 333 335 336 339 340 342 345 348 350 351 354 355 357 360 363 365 366 369 370 372 375 378 380 381 384 385 387 390 393 395 396 399 400 402 405 408 410 411 414 415 417 420 423 425 426 429 430 432 435 438 440 441 444 445 447 450 453 455 456 459 460 462 465 468 470 471 474 475 477 480 483 485 486 489 490 492 495 498 500 501 504 505 507 510 513 515 516 519 520 522 525 528 530 531 534 535 537 540 543 545 546 549 550 552 555 558 560 561 564 565 567 570 573 575 576 579 580 582 585 588 590 591 594 595 597 600 603 605 606 609 610 612 615 618 620 621 624 625 627 630 633 635 636 639 640 642 645 648 650 651 654 655 657 660 663 665 666 669 670 672 675 678 680 681 684 685 687 690 693 695 696 699 700 702 705 708 710 711 714 715 717 720 723 725 726 729 730 732 735 738 740 741 744 745 747 750 753 755 756 759 760 762 765 768 770 771 774 775 777 780 783 785 786 789 790 792 795 798 800 801 804 805 807 810 813 815 816 819 820 822 825 828 830 831 834 835 837 840 843 845 846 849 850 852 855 858 860 861 864 865 867 870 873 875 876 879 880 882 885 888 890 891 894 895 897 900 903 905 906 909 910 912 915 918 920 921 924 925 927 930 933 935 936 939 940 942 945 948 950 951 954 955 957 960 963 965 966 969 970 972 975 978 980 981 984 985 987 990 993 995 996 999 1000 

collatz(8)
    8 -> 4.0 -> 2.0 -> 1.0

ftoc(243)
    117.22222222222223

## Plik lab2-datastructures.py
s = [0] * 3
    s[0] += 1
    print(s)
      Wynik: [1, 0, 0]

    s = [''] * 3
    s[0] += 'a'
    print(s)
      Wynik: ['a', '', '']

    s = [[]] * 3
    s[0] += [1]
    print(s)
      Wynik: [[1], [1], [1]]

## Plik lab3-functions.py

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

Lab4.py
```
>>> gcd(2,2)
2
>>> gcd(2,5)
1
>>> lcm(2,2)
2
>>> lcm(2,8)
8
>>> 
```
Lab4b.py
```
>>> fact(3)
6
>>> fact(7)
5040
>>> 
```
Lab4c.py
```
['PyThOn', 'wOrLD']
>>> 
```
Lab4d.py
```
>>> generate_triangles()
<generator object generate_triangles at 0x02E24900>
>>> triangles_under(5)
0
1
3
```
