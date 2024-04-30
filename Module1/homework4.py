immutable_var = 1, 2.5, "alpha"
print(immutable_var)

# immutable_var[0] = 3  выдаёт ошибку,т.к. кортеж нельзя поменять после создания
#print(immutable_var[0])

mutable_list = [1, 2.5, "alpha"]
mutable_list[0] = 6
mutable_list[1] = 7.5
mutable_list[2] = "beta"
print(mutable_list)
