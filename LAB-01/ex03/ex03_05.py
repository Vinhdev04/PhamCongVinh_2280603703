def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


input_str = input("Enter list: ")
word_list = input_str.split()
word_count = dem_so_lan_xuat_hien(word_list)
print("Count of each word:", word_count)