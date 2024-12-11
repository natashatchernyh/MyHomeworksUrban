food = ["apple", "coconut", "banana"]
print(food[0])
food[0] = "pear"
print(food)
food[1] = "pear"
print(food)
food.append(True)
print(food)
food.extend("string")
print(food)
food.extend(["string", 2.0, 5])
print(food)
food.remove("pear")
print(food)
print("apple" in food)
print("pear" in food)

