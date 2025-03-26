def count_sub_string(main_str, sub_str):
    count = 0
    n = len(main_str)-(len(sub_str)+1)
    for i in range(n):
        if(main_str[i:len(sub_str)+i] == sub_str):
            count += 1
    return count
main_string = input()
sub_string = input()
result = count_sub_string(main_string, sub_string)
print(result)