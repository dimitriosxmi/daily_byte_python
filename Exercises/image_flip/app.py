"""
WIP (work in progress)
Currently learning about binary trees.
"""
import copy

smaller_image = [
    [0, 1],
    [2, 3],
]

image = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]
larger_image = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]


def render_image(image_to_render, with_separators=False):
    if with_separators:
        print("- - - - -")
    for row in image_to_render:
        print(row)
    if with_separators:
        print("- - - - -")


def rotate_array90(arr_to_rotate, ):
    arr_copy = copy.deepcopy(arr_to_rotate)
    length = len(arr_to_rotate)
    len_range = range(length)

    for arr_row in len_range:
        for arr_column in range(length):
            arr_copy[arr_row][arr_column] = arr_to_rotate[arr_row][length - arr_column - 1]

    arr_result = [list(row) for row in arr_copy]

    for arr_row in len_range:
        for arr_column in len_range:
            arr_result[arr_column][arr_row] = arr_copy[arr_row][arr_column]

    return arr_result


# render_image(smaller_image)
# render_image(rotate_array90(smaller_image), True)
render_image(image)
render_image(rotate_array90(image), True)
# render_image(larger_image)
# render_image(rotate_array90(larger_image), True)
