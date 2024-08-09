from Exercises.functions import list_generator

string_list = list_generator(str_gen_settings=[10])

for s in string_list:
    s_length = len(s)
    s_substring = ""
    uniques_count = 0
    counter = 0

    for char in s:
        if char not in s_substring:
            s_substring += char
            counter += 1
            if uniques_count < counter:
                uniques_count = counter
        else:
            s_substring = char
            counter = 1

    print("s: [" + s + "] uniques_count: [" + str(uniques_count) + "]")
