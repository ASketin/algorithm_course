

def compute_inversion(integer_list: list):
    """
    Function compute the number_of_inversions in 1D-list
    :param integer_list: array of integers
    :return: number_of_inversions
    """
    current_size = len(integer_list)
    if current_size == 1 or current_size == 0:
        return 0, integer_list
    inv1, left = compute_inversion(integer_list[:current_size//2])
    inv2, right = compute_inversion(integer_list[current_size//2:])

    i = 0
    j = 0
    k = 0
    inv3 = inv1 + inv2
    while k < len(integer_list):

        if i == len(left):
            integer_list[k:] = right[j:]
            return inv3, integer_list

        if j == len(right):
            integer_list[k:] = left[i:]
            return inv3, integer_list

        if left[i] < right[j]:
            integer_list[k] = left[i]
            i += 1

        else:
            integer_list[k] = right[j]
            j += 1
            inv3 += len(left) - i

        k += 1

    return inv3, integer_list
