def fact(n):
    mult = 1
    for i in range(n):
        mult*=i+1
    return mult

def nCk(n:int,k:int)->int:
    return fact(n)/(fact(k)*fact(n-k))

def linear_sum(x:list, result:int) -> bool:    
    # base case - the list is size 0,
    # setting the result to 0 means that we found a linear sum
    # else, we return to different starting conditions
    if len(x) == 0 : return result == 0
    a = x[0]
    b = 0

    if len(x)> 1: b = x[1]
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

def ordered_subset(str1:str, str2:str) -> bool:
    # base case - comparing 2 chars
    # ! second condition - 2 consequtive chars of str2 in str1 returns false 
    if str1[0:2] == str2[0:2] : 
        return False
    # ! first condition - str2 is empty means the prev chars of str2 are in str1 => is a subset...
    if str2 == '' : 
        return True
    # in case that we went through all the chars in str1 and still have some in str2
    # means that not all chars in str2 appear in str1
    elif str1 == '' and len(str2) !=0 : 
        return False
    
    print(str1,str2)

    if str1[0] == str2[0]:
        return ordered_subset(str1[1:],str2[1:]) 
    return ordered_subset(str1[1:],str2)

# region - testing
#        ↓  ↓
# str1 = "aetgwlae"
# str2 = "ewl"
# str1 = "ladbxcfe"
# str2 = "abc"
# answer = ordered_subset(str1,str2)
# print(answer)
# endregion

def n_set(n:int)->str:
    if n == 0 :
        return ''
    else : 
        return n_set(n-1) + str(n)

def rec_sub(k:int,subsets:list[str],subset:str,i:int=0)->None:
    # base case - subset len(k)...
    if len(subset) == k :
        subsets.append(subset)
    # rec step - 
    elif i > k:
        pass
    else:
        rec_sub(k,subsets,subset[:i]+subset[i+1:],i)
        rec_sub(k,subsets,subset,i+1)

def k_size_subsets(n:int, k:int) -> str:
    a = []
    rec_sub(k,a,n_set(n))
    return a

# #? region - testing
# answer = n_set(5) 
# answer = k_size_subsets(5,3)
# # [‘123’, ‘124’, ‘125’, ‘134’, ‘135’, ‘145’, ‘234’, ‘235’, ‘245’, ‘345’]
n,k = 8,4
answer = k_size_subsets(n,k)
print(answer[:10])
print(len(answer)-nCk(n,k))
# # endregion

def recurse_depth(d:dict)->int:
    max = 0
    if type(d) != dict :
        max -= 1
    elif type(d) == dict:
        for key in  d.keys():
            #! recursive call
            res =  recurse_depth(d.get(key,0)) + 1
            if res > max : 
                max = res
    return max    

def dict_depth(d:dict)->int:
    if type(d) != dict :
        return TypeError('not a dictionary')
    return recurse_depth(d)

# #? region - testing
# #? depth = 0
# test0 = {}
# #? depth = 1
# test1 = {1: {1: "a", 2: "b"}, 2: "b"}
# #? depth = 2
# test2 = {1: {1: "a", 2:"b"}, 2: {1: {1: "a", 2: "b"}, 2: "b"}}
# #? depth = 2
# test3 = {1: {1: "a",2: "b"},4: {1:{1: "a",2: "b"},2: "b"},3: {1: "a",2: "b"},2: "b"}
# #? depth = 7
# test4 = {1: {1: "a",2: {1: {1: "a",2: "b"},4: {1:{1: "a",2: "b"},2: "b"},3: {1: "a",2: "b"},2: "b"}},4: {1:{1: {1: {1: "a",2: {1: {1: "a",2: "b"},4: {1:{1: "a",2: "b"},2: "b"},3: {1: "a",2: "b"},2: "b"}},4: {1:{1: "a",2: "b"},2: "b"},3: {1: "a",2: "b"},2: "b"},2: "b"},2: "b"},3: {1: "a",2: "b"},2: "b"}
# #! type error
# test5 = 1
# arr = [test0,test1,test2,test3,test4,test5]
# # for test in arr:
# #   print(dict_depth(test))
# # endregion

def nested_get(d:dict, key:int)->list[str]:
    res = []
    # base case - a dict with the wanted key
    if type(d.get(key,0)) == str : 
        res.append(d.get(key))
    for sub in d.keys():
        if type(d.get(sub,0)) == dict :
            res += nested_get(d[sub],key)
    return res

# #? region
# #? expected : ['b']
# test1 = nested_get({1: "a", 2: "b"}, 2)
# #? expected : []
# test2 = nested_get({1: {1: "a", 2: "b"}, 2: "b"}, 3)
# #? expected : ['a','c']
# test3 = nested_get({1: {1: "a", 2: "b"}, 2: {1: {1: "c", 2: "b"}, 2: "b"}}, 1)
# #? expected : ['a','c']
# test4 = nested_get({1: {1: "a", 2: "b"}, 2: {1: {1: "c", 2: {1: {1: "x", 2: {1: "45", 2: {1: {1: "5", 2: "b"}, 2: {1: {1: "yizhar", 2: "b"}, 2: "b"}}}}, 2: {1: {1: "z", 2: "b"}, 2: "b"}}}, 2: "b"}}, 1)

# test_arr = [test1,test2,test3,test4]
# for test in test_arr:
#     print(test)
# # endregion


def distance(row1, col1, row2, col2):
    return abs(row1-row2) + abs(col1-col2)

def add_tower(board, d, row, col):
    res = True
    for _row,_col in enumerate(board[:row]):
        print("distance :" + str(distance(row,_row,col,_col)))
        if distance(row,_row,col,_col) < d :
            res = False
    return res 

def n_towers(n, d):
    # Delete the pass command and insert you code below
    pass


