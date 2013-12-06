factor_counter = 0
triangle_index = 1
triangle_number = 0
triangle_set = []


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


print 'Finding triangle numbers'
while len(triangle_set) < 100000:
    previous_index = int(triangle_index)
    # generate triangle number
    while triangle_index >= 1:
        triangle_number += triangle_index
        triangle_index -= 1

    # if number is less than 1000, move on
    if triangle_number > 1000:
        triangle_set.append(triangle_number)

    triangle_number = 0
    triangle_index = previous_index + 1
print 'done.'

print 'finding factors'
for triangle_number in triangle_set:
    found_factors = factors(triangle_number)
    #print len(found_factors)
    if len(found_factors) == 500:
        print triangle_number
