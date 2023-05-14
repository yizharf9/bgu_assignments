# aux
# 1
def linear_sum(x: list, result: int) -> bool:
    # base case - the list is size 0,
    # setting the result to 0 means that we found a linear sum
    # else, we return to different starting conditions
    if len(x) == 0:
        return result == 0
    a = x[0]
    b = 0

    if len(x) > 1:
        b = x[1]
    if a == result or a + b == result or a - b == result:
        return True
    # vars representing the reduced problem for the next rec...
    temp = x[0]
    new_x = x[1:]

    if linear_sum(new_x, result - temp):
        return True
    elif linear_sum(new_x, result + temp):
        return True
    return linear_sum(new_x, result)


# 2a
def ordered_subset(str1: str, str2: str) -> bool:
    # base case - comparing 2 chars
    # ! second condition - 2 consequtive chars of str2 in str1 returns false
    if str1[0:2] == str2[0:2]:
        return False
    # ! first condition - str2 is empty means the prev chars of str2 are in str1 => is a subset...
    if str2 == "":
        return True
    # in case that we went through all the chars in str1 and still have some in str2
    # means that not all chars in str2 appear in str1
    elif str1 == "" and len(str2) != 0:
        return False

    print(str1, str2)

    if str1[0] == str2[0]:
        return ordered_subset(str1[1:], str2[1:])
    return ordered_subset(str1[1:], str2)


# 2b
def n_set(n: int) -> str:
    if n == 0:
        return ""
    else:
        return n_set(n - 1) + str(n)


def rec_sub(k, subsets, subset, i=0) -> None:
    # base case - subset len(k)...
    if len(subset) == k:
        subsets.append(subset)
    # rec step -
    elif i > k:
        pass
    else:
        rec_sub(k, subsets, subset[:i] + subset[i + 1 :], i)
        rec_sub(k, subsets, subset, i + 1)


def k_size_subsets(n, k):
    a = []
    rec_sub(k, a, n_set(n))
    return a


# 3a
def recurse_depth(d):
    max = 0
    if type(d) != dict:
        max -= 1
    elif type(d) == dict:
        for key in d.keys():
            #! recursive call
            res = recurse_depth(d.get(key, 0)) + 1
            if res > max:
                max = res
    return max


def dict_depth(d):
    if type(d) != dict:
        raise TypeError("expected a dictionary!")
    return recurse_depth(d)


# 3b
def nested_get(d, key):
    res = []
    # base case - a dict with the wanted key
    if type(d.get(key, 0)) == str:
        res.append(d.get(key))
    for sub in d.keys():
        if type(d.get(sub, 0)) == dict:
            res += nested_get(d[sub], key)
    return res


# 4a
def distance(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2)


# 4b
def add_tower(board, d, row, col):
    for _row, _col in enumerate(board[:row]):
        # print("distance :" + str(distance(row,_row,col,_col)))
        if distance(row, col, _row, _col) <= d:
            return False
    board[row] = col
    return True


def rec(board: list[int], d: int, i=0):
    n = len(board)
    if i == n - 1:
        for j in range(n - 1):
            if add_tower(board, d, n - 1, j):
                return True
    for j in range(n):
        if add_tower(board, d, i, j) and rec(board, d, i + 1):
            return True


# 4c
def n_towers(n: int, d: int):
    n_board = n * [0]
    if n > 1 and d >= n:
        return []
    if not rec(n_board, d):
        return []
    return n_board
