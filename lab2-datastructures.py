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