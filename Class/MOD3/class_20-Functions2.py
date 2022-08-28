#Interactive help:
help(print) # or, on terminal >>>help()

#Docstrings
def count(s, e, p):
    """Sequence starting in 's' and finish in 'e', jumping 'p'
    Args:
        s (start): first value
        e (end): last value
        p (jump): increment
    """
    for value in range(s, e, p):
        print(f'->{value}')
#help(count)

#Optional paramenters:
def sum(a=0, b=0, c=0):
    s = a+b+c
    print(s)
sum(2+5+0) == sum(2+5)
sum() == 0