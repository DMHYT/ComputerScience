def get_int_input(hint: str) -> int:
    try:
        result = int(input(hint))
        return result
    except ValueError:
        print("Input data is invalid! Try again...")
        return get_int_input(hint)

k = get_int_input("Enter students count: ")
w = get_int_input("Enter maximum tents weight: ")

tents = [
    ( get_int_input("Enter first tent weight: "), get_int_input("Enter first tent capacity: ") ),
    ( get_int_input("Enter second tent weight: "), get_int_input("Enter second tent capacity: ") ),
    ( get_int_input("Enter third tent weight: "), get_int_input("Enter third tent capacity: ") )
]
tents.sort(key=lambda el: el[1])

k_left = k
used_w = 0
for tent in tents:
    if k_left == 0:
        break
    weight = tent[0]
    cap = tent[1]
    if used_w + weight <= w:
        k_left = max(0, k_left - cap)
        used_w += weight

if k_left == 0:
    print("YES")
else:
    print("NO")
