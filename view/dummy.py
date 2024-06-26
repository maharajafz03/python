


# def add():
#     def sum():
#         print("hello mother fucker")

# name = add()

# print(name)

def calc_factorial(num):
    if num == 1:
        return 1
    else:
        return(num+calc_factorial(num-1))
    
result = calc_factorial(6)

print(result)