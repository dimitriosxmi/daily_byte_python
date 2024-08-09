from Exercises.functions import list_generator, string_generator

my_list = list_generator(10, str_gen_settings=[5, ["penis"]])
print(my_list)

s = string_generator(5, ["abc"])
s_length = len(s)
temp_s = ""
uniques = 0
uniques_count = 0

for char in s:
    # print(char)
    if char not in temp_s:
        temp_s += char
        uniques_count += 1
        if uniques < uniques_count:
            uniques = uniques_count
    else:
        temp_s = char
        uniques_count = 1

print(s)
# print(uniques)
