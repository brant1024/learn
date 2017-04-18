#filter
def is_odd(n):
    return n%2==1

l=list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15]))
print(l)


def is_strip(s):
    return s and s.strip()

l= list(filter(is_strip,['sss',' ss ','s s']))
print(l)