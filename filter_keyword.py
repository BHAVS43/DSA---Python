def even_nums(elements):
    return elements % 2 == 0
arr = [-1, 0, 43, 56, 46, 27, 92, 90]
new_arr = list(filter(even_nums, arr))
print(new_arr)
