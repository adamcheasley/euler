factor_counter = 0
triangle_index = 1
triangle_number = 0

while factor_counter < 500:
    previous_index = int(triangle_index)
    # generate triangle number
    while triangle_index >= 1:
        triangle_number += triangle_index
        triangle_index -= 1

    print triangle_number
    triangle_number = 0
    triangle_index = previous_index + 1

# if number is less than 1000, move on
