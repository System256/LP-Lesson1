my_list = [3, 5, 7, 9, 10.5]
print(my_list)
my_list.append('Python')
print(len(my_list))

print(my_list[0])
print(my_list[-1])
print(my_list[1:5])
# del my_list[-1]
my_list.remove('Python')
print(my_list)
my_list.extend('Ann')
print(my_list)
my_list.reverse()
print(my_list)