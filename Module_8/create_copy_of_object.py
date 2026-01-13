import copy

# --------------------------------------------------------------------------------------

my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(my_list)

# --------------------------------------------------------------------------------------

my_list = [1, 2, 3]

def square_list(x: list):
    for i, el in enumerate(x):
        x[i] = el ** 2
    return x

new_list = square_list(my_list)
print(new_list, id(new_list))
print(my_list, id(my_list))

# --------------------------------------------------------------------------------------

my_list = [1, 2, 3]

def square_list(x: list):
    return [el ** 2 for el in x]

new_list = square_list(my_list)
print(new_list)
print(my_list)

# --------------------------------------------------------------------------------------

my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list, copy_list)

my_dict = {1: "a"}
copy_dict = {**my_dict}
copy_dict["new_ley"] = "new_value"
print(my_dict, copy_dict)

# --------------------------------------------------------------------------------------

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list)
print(copy_list)

# --------------------------------------------------------------------------------------

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)

# --------------------------------------------------------------------------------------

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.deepcopy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)
