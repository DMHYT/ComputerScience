def get_int_input():
    try:
        result = int(input("Enter integer: "))
        return result
    except ValueError:
        print("Input data is invalid!")
        return get_int_input()

n = get_int_input()

arr = []

num = 10 ** (n - 1)
while len(str(num)) == n:
    if num % 2 != 0:
        arr.append(num)
    num += 1

print(len(arr))