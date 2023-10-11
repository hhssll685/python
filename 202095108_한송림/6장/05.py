def print_counter1():
    print("counter = ", counter)


counter = 100
print_counter1()


def print_counter():
    counter = 200
    print("counter = ", counter)


counter = 100
print_counter()


def order(num, pickle, onion):
    print("햄버거{0}개 - 피콜{1}, 양파{2}".format(num, pickle, onion))


order(1, False, True)
