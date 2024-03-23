def transform_process(my_list):
    my_list.append(4)
    print("Inside function:", my_list)  

my_list = [1, 2, 3]
print("Before function call:", my_list)
transform_process(my_list)
print("After function call:", my_list)

