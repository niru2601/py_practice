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

