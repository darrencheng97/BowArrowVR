# for letter in "Darren Cheng":
#     print(letter)

# for num in [2,3,4,5,6]:
#     print(num)

# Tutorial: Based on pow() function concept, define a manual pow function to calculate the result of 2^5

def power(base_num, power_num):
    result = base_num
    for i in range(power_num-1):
        result *= base_num
    return result

print(power(2,5))