
def sum_check(n):
    final_sum = 0
    string = str(n)
    for i in string:
        final_sum += int(i)
    return final_sum




number = 12345
print(sum_check(number))