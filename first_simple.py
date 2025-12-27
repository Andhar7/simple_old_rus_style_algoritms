

def sum_product(a, b):

    sum = a + b
    product = a * b

    print(f"Sum: {sum}, Product: {product}")

    return sum, product

def interchange(a, b):

    # a = 7
    # b = 12

    print(f"Before changed: a: {a}, b: {b}")

    temp = a
    a = b
    b = temp

    print(f"After changed:  a: {a}, b: {b}")

    return a, b

# Write an algorithm to find the largest number from 10 given
# numbers.
def largest_number():
    largest = 0
    counter = 0

    while counter < 10:
        counter = counter + 1

        x = int(input("Enter the number : "))

        if largest > x:
            print(f"Largest {largest} number more then input number x: {x} ")
            pass
        else:
            largest = x

            print(f"We are found the largest number at the end: {largest}")

    print(f"The largest number is: {largest}")
    return largest


if __name__ == "__main__":
    print("*" * 72)
    print("Sum and Product:")
    print(sum_product(2, 3))
    print("*" * 72)

    print("*" * 72)
    print("Interchange:")
    print(interchange(2, 3))
    print("*" * 72)

    print("*" * 72)
    print("Largest number:")
    largest_number()
    print("*" * 72)