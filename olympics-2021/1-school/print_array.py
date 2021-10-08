def get_int_input(hint: str) -> int:
    try:
        result = int(input(hint))
        return result
    except ValueError:
        print("Error! You have to input integer! Try again...")
        return get_int_input(hint)

length = get_int_input("Enter integer array length: ")

def get_array_input() -> list:
    arr = input("Enter numbers divided by space: ").split(' ')
    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except ValueError:
            print("Error! Your array input is incorrect! Try again...")
            return get_array_input()
    return arr

arr = get_array_input()

stopped: bool = False
for i in range(length):
    if not stopped:
        try:
            print(arr[i])
        except IndexError:
            print("You put less numbers than the array length that you put before! Printing stopped!")
            stopped = True

print("Completed!")