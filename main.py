
def sq(*args):
    print(args[2])

    sum_ = 0
    for n in args:
        sum_ += n
    return sum_


print(sq(1, 2, 3, 4))
