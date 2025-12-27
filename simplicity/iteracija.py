

def iteracija():

    a = [11, 22, 33, 55, 88, 96, 108, 121] 

    for i in a:
        print(i, end = ' ')
    return i


def find_number_use_enumerate(arr, num):

    for i, value in enumerate(arr, 0):
        if value == num:
            print(f"We found at index {i} on value: {value}")
            break

def find_a_number_use_range(arr, num):

    for i in range(len(arr)):
        if arr[i] == num:
            print(f"We found number {num} at index {i} in array: {arr[i]}")
            break
        else:
            print("Number not found")

def awesome_rus_style(arr, num):

    if num in arr:
        print(f"We found number {num} at index {arr.index(num)} in array: {arr}")
        return arr.index(num), num
    else:
        print("Number not found")

        return None

def rus_style_filter(arr, num):

    num = list(filter(lambda x: x == num, arr))

    if num:
        print(f"We found number {num} at index {arr.index(*num)} in array: {arr}")
        return arr.index(*num), *num
    else:
        print("Number not found")
        return None

# find index
def rus_style_index(arr, num):
    print(f"We found number {num} at index {arr.index(num)} in array: {arr}")
    return arr.index(num)




if __name__ == "__main__":
    arr = [11, 22, 33, 55, 88, 96, 108, 121]
    num = 33
    iteracija()
    print(f"*" * 72)
    find_number_use_enumerate(arr, num)

    print(f"*" * 72)
    find_a_number_use_range(arr, num)

    print(f"*" * 72)
    print(f"Awesome style")
    print(f"Awesome rus style: {awesome_rus_style(arr, num)}")

    print(f"*" * 72)
    print(f"Rus style filter: {rus_style_filter(arr, num)}")

    print(f"*" * 72)
    print(f"Rus style index: {rus_style_index(arr, num)}")