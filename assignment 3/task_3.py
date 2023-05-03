def linear_sum(x:list, result:int):    
    # base case - the list is size 0,
    # setting the result to 0 means that we found a linear sum
    # else, we return to different starting conditions
    if len(x) == 0 : return result == 0
    a = x[0]
    b = 0

    if len(x)> 1: b = x[1]
    # 
    if (
        a == result or
        a + b == result or
        a - b == result
    ): return True
    # vars representing the reduced problem for the next rec...
    temp = x[0]
    new_x = x[1:]

    if linear_sum(new_x,result-temp):return True
    elif linear_sum(new_x,result+temp):return True
    return linear_sum(new_x,result)

# region - testing
# x = [2,3,6,7,10,15] # = 33
# answer = linear_sum(x,33)
# print(answer)
# endregion


def ordered_subset(str1:str, str2:str):
    # base case - comparing 2 chars
    if str2 == '' : return True
    elif str1 == '' and len(str2) !=0 :return False
    print(str1,str2)
    if str1[0] == str2[0]:
        return ordered_subset(str1[1:],str2[1:]) 
    return ordered_subset(str1[1:],str2)


# region - testing
#        ↓  ↓
str1 = "aetgwae"
str2 = "ewf"
answer = ordered_subset(str1,str2)
print(answer)
# endregion



def k_size_subsets(n, k):
    # Delete the pass command and insert you code below
    pass


def dict_depth(d):
    # Delete the pass command and insert you code below
    pass


def nested_get(d, key):
    # Delete the pass command and insert you code below
    pass


def distance(row1, col1, row2, col2):
    # Delete the pass command and insert you code below
    pass


def add_tower(board, d, row, col):
    # Delete the pass command and insert you code below
    pass


def n_towers(n, d):
    # Delete the pass command and insert you code below
    pass


