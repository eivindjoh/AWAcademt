def digits(num):
    num_list = []
    sorted_num = sorted(str(num))
    reversed_num = sorted_num[::-1]
    num_list.append(int(''.join(sorted_num)))
    num_list.append(int(''.join(reversed_num)))
    output = max(num_list) - min(num_list)
    return output


