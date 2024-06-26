name = "maga"
age = "26"

husban = ["maga", "yamuna"]

def person(name, age):
    print(name + " is " + str(age) + " years of old ")

person("yamuna", "24")

def wed(husban):
    data = " weds "
    print(husban[-1] + data + husban[0])

wed(husban)

# couple = {name:"maga", age:"23" }

# def data():
#     king = couple['name']
#     queen = couple['age']

#     print(king + " is " + queen + " years old")


# data(couple)


couple = {"name": "maga", "age": "23"}

def data():
    king = couple['name']
    queen = couple['age']

    print(king + " is " + queen + " years old")

data()


a = "maga"
b = "3"

print(a + b)

def function(a, b):
    sum = a + b
    return sum

result = function(55, 64)

print(result)

def loop(a, b, c):
    for val in range(a, b, c):
        print(val)

loop(119, 3, -1)