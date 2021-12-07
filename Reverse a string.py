def reverse(string):

    length = len(string)
    slice1 = string[length::-1]
    words = slice1.split()
    words = list(reversed(words))
    return ' '.join(words)


def reverse2(string):
    str_smpl = string
    lst = []
    for word in str_smpl.split(' '):
        letters = [c for c in word if c.isalpha()]
        for c in word:
            if c.isalpha():
                lst.append(letters.pop())
                continue
            else:
                lst.append(c)
        lst.append(' ')
    print("".join(lst))


if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba ghfe'),
    ]

    for text, reversed_text in cases:
        assert reverse2(text) == reversed_text