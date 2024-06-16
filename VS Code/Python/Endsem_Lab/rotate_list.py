def circulate_list_right(lst):
    if len(lst) <= 1:
        return lst 
    
    last_element = lst.pop()
    lst.insert(0, last_element)

my_list = [1, 2, 3, 4]

for _ in range(len(my_list)):
    print(my_list)
    circulate_list_right(my_list)
