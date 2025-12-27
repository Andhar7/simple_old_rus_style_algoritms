

# Develop an algorithm to evaluate S using the relation:
# S=1 + 4 + 9+ 16 + …..+ 100

def relation():

    x = 1
    s = 0

    while x <= 10:
        y = x * x
        print(f"Y : {y}")
        s = s + y
        print(f"S : {s}")
        x = x + 1
        print(f"X : {x}")
        print(f"X : {x} - y: {y}:  is here : {s}")
    return s

def biggest_number():

    a = 100
    b = 44
    c = 96

    s = sorted([a, b, c])
    print(f"A : {s}")
    print(s[-1])

    if a > b and a > c:
        print(f"A is the biggest number {a}")
        return a
    elif b > a and b > c:
        print(f"B is the biggest number {b}")
        return b
    else:
        print(f"C is the biggest number {c}")
        return c



if __name__ == '__main__':

    print(relation())

    print(biggest_number())