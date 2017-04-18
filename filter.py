#filter
def is_odd(n):
    return n%2==1

l=list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15]))
print(l)