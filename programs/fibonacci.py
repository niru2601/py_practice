def febo(a):
    febonaci = []
    current_element = 0
    next_element = 1
    for i in range(0,a):
        febonaci.append(current_element)
        check = current_element + next_element
        current_element, next_element = next_element, check
    return febonaci

number_of_terms = 10
print(febo(number_of_terms))

my_list = [10, 23, 45, 67, 12, 89, 34]
print(sum(my_list))