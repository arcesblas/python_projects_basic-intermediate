def highest_even(li):
    even = []
    for number in li:
        if number % 2 == 0:
            even.append(number)
            
    print(max(even))
    return max(even)


print(highest_even([10, 2, 3, 4, 8, 11]))
