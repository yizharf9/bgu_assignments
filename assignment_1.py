import time 
# Task 1
num = input("choose excercice too activate : ")
if num == '1a':
    # write your answer for question 1a below
    def ex_1a():
        a = int(input("enter parameter a:"))
        b = int(input("enter parameter b:"))
        c = int(input("enter parameter c:"))
        if (a**2 + b**2 == c**2):
            print("yes")
        else:
            print("no")
        # todo - optional code...
        # out = "yes" if a**2 + b**2 == c**2 else "no"
        # print(out)

elif num == '1b':
    # write your answer for question 1b below
    def ex_1b():
        n = int(input("enter desired integer : "))
        for a in range(2,n+1):
                for b in range(a,n+1):
                    for c in range(b,n+1):
                        output = a**2 + b**2 == c**2
                        if output : 
                            [a,b,c] = sorted([a,b,c])
                            print(a,b,c)

elif num == '1c':
    # write your answer for question 1c below
    def ex_3a():
        a = int(input("enter parameter a : "))
        b = int(input("enter parameter b : "))
        pyth = (a**2 + b**2)**0.5
        output = "yes" if pyth == int(pyth) else "no"
        print(output)

elif num == '2a':
    # write your answer for question 2a below
    def ex_2a():
        a0 = int(input("enter parameter a0: "))
        n = int(input("enter parameter n: "))
        d = int(input("enter parameter d: "))
        result = 1
        print("starting at: " + str(a0-a0%d + d))
        
        for i in range(a0 +d -a0%d,n+1,d):
            result *= i
            print("result: " + str(result))
            print("i:"+str(i))
        print (result)

elif num == '2b':
    # write your answer for question 2b below
    def A(x:int,n:int,m:int)->int:
        condition = (
            x <= n-x+1
            and
            (x**2 +(n-x+1)**2 ) %m == 0
        )
        print(x,condition)
        if condition :
            return x**2 +(n-x+1)**2 
        else:
            return 1    

    def ex_2b():
        n = int(input("enter parameter n: "))
        m = int(input("enter parameter m: "))
        result = 1
        for i in range(1,n):
            print(A(i,n,m))
            result *= A(i,n,m)
        print(result)

elif num == '2c':
    # write your answer for question 3 below

    def prime_fact(n): # a function that returns a list of each factor with the number of divisions in a duet
        factors = []
        for i in range(2,int(n**0.5)):
                not_prime = False
                # checking that i is not a multiply of any previous factors
                for [factor,num] in factors:
                    if i%factor==0:
                        not_prime = True
                if not_prime :continue
                # creating a count for the number of factor occurences
                count = 0
                n_temp = n

                while n_temp%i==0 and n_temp!=0 : #dividing by the factor until reaching an indivisabile number
                    count+=1
                    n_temp /= i

                if count!=0 : # disregarding any factor who dont divide at all
                    factors.append([i,count])
        return factors 

    def ex_2c() : 
        n = int(input("choose parameter n : "))
        m = int(input("choose parameter m : "))
        
        factors = prime_fact(n)
        total = 1
        for [p,x] in factors :
            print("prime: "+str(p),"occurences: "+str(x))
            if x%m==0 :
                total *= p**x
            else:
                total *= p*x
            print("total: "+ str(total))
        
        print("total: "+ str(total))

elif num == '3':
    # write your answer for question 3 below
    def ex_3():
        a = int(input("choose parameter a: "))
        b = int(input("choose parameter b: "))

        if b%a==0 :
            # if a==2 : return True
            for i in range(2,a):
                if a%i==0 and b%i==0 :
                    return False
                return True
        
        return False
    res = ex_3()
    print(res)

elif num == '4a':
    # write your answer for question 4a below
    print("ex_4a")
    def ex_4a():
        s = input("enter string as s : ")
        d = int(input("enter integer as d : "))
        result = ''
        for i in range(0,len(s)-len(s)%d,d):
            result += s[i:i+1]
        print(result)
    ex_4a()

elif num == '4b':
    # write your answer for question 4b below
    def ex_4b():
        s1 =" "+ input("enter string input for s1 : ") +" "
        s2 = input("enter string input for s2 : ")
        s3 = input("enter string input for s3 : ")

        res = ''
        index_lst = []

        for i in range(1,len(s1)):
            print(i)
            if (s1[i] in s2) and ((s1[i+1] in s3) or (s1[i-1] in s3)): 
                index_lst.append(i)

        for i in range(len(s1)):
            if i not in index_lst : res = res + s1[i] 

        print(res)
    ex_4b()

elif num == '4c':
    # write your answer for question 4c below
    def exec_a(phrase:str)->str:
        result =''
        for char in phrase:
            if char in ["a","e","i","o","u","A","E","I","O","U"]:
                result += "*"+char+"*"
            else: result+=char
        print("a: "+result)
        return result
    
    def exec_b(phrase:str)->str:
        if len(phrase)%2==1 : phrase = phrase +" "
        result = ''

        for i in range(1,len(phrase),2):
            result += phrase[i-1].lower() + phrase[i].upper()
        
        print("b: "+result)
        return result.strip()

    def exec_c(phrase:str)->str:
        word_lst = []
        temp = 0
        for i in range(len(phrase)):
            if phrase[i] == " ":
                word_lst.append(phrase[temp:i])
                temp = i
            elif i == len(phrase): word_lst.append(phrase[temp:])
        word_lst.sort()
        for word in word_lst:
            


    def ex_4c():
        s = input("enter a string for parameter s: ")
        phrase_lst = []
        temp = 0

        for i in range(len(s)):
            if s[i:i+2] == ", " :
                phrase_lst.append(s[temp:i])
                temp = i
            elif i == len(s)-2:
                phrase_lst.append(s[temp+2:])
        print(phrase_lst)
        
        for i in range(len(phrase_lst)):
            phrase_lst[i] = exec_a(phrase_lst[i])
            phrase_lst[i] = exec_b(phrase_lst[i])

        print(phrase_lst)

    ex_4c()



else:
    print('error')






# start = time.time()
# end = time.time()
# print(end - start)