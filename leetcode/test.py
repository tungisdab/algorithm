def wordPattern(pattern, s):
        a = []
        b = []
        x = []
        y = []
        n = 0
        m = 0
        for i in pattern:
            if i not in a:
                a.append(i)
                x.append(n)
                n += 1
            else:
                x.append(a.index(i))
        for i in s.split():
            if i not in b:
                b.append(i)
                y.append(m)
                m += 1
            else:
                y.append(b.index(i))
        if len(x) != len(y):
            return False
        print(*x)
        print(*y)
        return x == y

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))