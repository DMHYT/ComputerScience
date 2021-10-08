# Absolutely non-needed input data 0_0
n = input("Enter integer array length: ")

def get_int_array() -> list:
    result = input("Enter integers divided by space: ").split(' ')
    for i in range(len(result)):
        try:
            result[i] = int(result[i])
        except ValueError:
            print("Invalid input data! Try again!")
            return get_int_array()
    return result

arr = get_int_array()

filtered = []
for item in arr:
    if item not in filtered:
        filtered.append(item)

print(filtered)