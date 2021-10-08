def get_int_input(hint: str) -> int:
    try:
        result = int(input(hint))
        return result
    except ValueError:
        print("Error! You have to input integer! Try again...")
        return get_int_input(hint)

arr = [
    get_int_input("Enter first integer: "),
    get_int_input("Enter second integer: "),
    get_int_input("Enter third integer: ")
]
arr.sort()
print(arr[1])