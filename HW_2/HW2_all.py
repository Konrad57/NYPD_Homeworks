# Exercise 1
def my_sum(lst):
    print(f"my_sum({lst}) == {sum(lst)}")
    return sum(lst)


print("Exercise 1")
my_sum([])
my_sum([1, 22, 3])


# Exercise 2

def sum_2d(lst):  # assuming lst is an empty list or list of lists
    total = 0
    for elt in lst:
        total += sum(elt)

    print(f"sum_2d({lst}) == {total}")
    return total


print("Exercise 2")
sum_2d([])
sum_2d([[], []])
sum_2d([[1, 2, 3], [], [-34, 23423, -23425]])


# Exercise 3

def how_many(lst, what):
    count = 0
    for elt in lst:
        if what == elt:
            count += 1

    print(f"how_many({lst}, {what}) == {count}")


print("Exercise 3")
how_many([], 13)
how_many([1, 234, 123, 23, 1, 234, 1, -43], 1)
how_many(["Mary", "Jenny", "Mary", "Susan"], "Mary")
how_many(["Mary", "Jenny", "Mary", "Susan"], "Emily")
how_many("Mary has a little lamb", "a")


# Exercise 4

def copy(lst):
    lst_copy = []
    for elt in lst:
        lst_copy.append(elt)

    print(f"copy({lst}) == {lst_copy}")
    return lst_copy


print("Exercise 4")
copy([])
copy([1, 2, 3])


# Exercise 5

def reverse(lst):
    reverse_lst = []
    for elt in lst:
        reverse_lst = [elt] + reverse_lst

    print(f"reverse({lst}) == {reverse_lst}")


print("Exercise 5")
reverse([])
reverse([1, 2, 3])


# Exercise 6

def reverse2(lst):
    reverse_lst = []
    for elt in lst[::-1]:
        reverse_lst.append(elt)

    print(f"reverse2({lst}) == {reverse_lst}")
    return reverse_lst


print("Exercise 6")
reverse2([])
reverse2([1, 2, 3])


# Exercise 7

def set_sum(lst1, lst2):
    sum_lst = []
    for elt in lst1:
        sum_lst.append(elt)

    for elt in lst2:
        if elt not in lst1:
            sum_lst.append(elt)

    print(f"set_sum({lst1, lst2}) == {sum_lst}")
    return sum_lst


print("Exercise 7")
set_sum([], [])
set_sum([1, 2, 3], [1, 2, 3])
set_sum([], [1, 2, 3])
set_sum([1, 2, 3], [])
set_sum([1, 3, -2], [-2, -3, 0, 1, 34])


# Exercise 8

def sorted_set_sum(lst1, lst2):
    sum_lst = []
    for elt in lst1:
        sum_lst.append(elt)

    for elt in lst2:
        if elt not in lst1:
            sum_lst.append(elt)

    for i in range(1, len(sum_lst)):
        while i > 0 and sum_lst[i - 1] > sum_lst[i]:
            sum_lst[i], sum_lst[i - 1] = sum_lst[i - 1], sum_lst[i]
            i -= 1

    print(f"sorted_set_sum({lst1, lst2}) == {sum_lst}")
    return sum_lst


print("Exercise 8")
sorted_set_sum([], [])
sorted_set_sum([1, 2, 3], [1, 2, 3])
sorted_set_sum([], [1, 2, 3])
sorted_set_sum([1, 2, 3], [])
sorted_set_sum([1, 3, -2], [-2, -3, 0, 1, 34])
