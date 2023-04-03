# Task 1
num = input()
if num == '1a':
    # write your answer for question 1a below
    def ex_1a():
        a = int(input())
        b = int(input())
        c = int(input())
        if (a**2 + b**2 == c**2):
            print("yes")
        else:
            print("no")
        # todo - optional code...
        # out = "yes" if a**2 + b**2 == c**2 else "no"
        # print(out)
    ex_1a()

elif num == '1b':
    # write your answer for question 1b below
    def ex_1b():
        n = int(input())
        for a in range(2,n+1):
                for b in range(a,n+1):
                    for c in range(b,n+1):
                        output = a**2 + b**2 == c**2
                        if output : 
                            [a,b,c] = sorted([a,b,c])
                            print(a,b,c)
    ex_1b()

elif num == '1c':
    # write your answer for question 1c below
    def ex_1c():
        a = int(input("enter parameter a : "))
        b = int(input("enter parameter b : "))
        pyth = (a**2 + b**2)**0.5
        output = "yes" if pyth == int(pyth) else "no"
        print(output)
    ex_1c()

elif num == '2a':
    # write your answer for question 2a below
    def ex_2a():
        a0 = int(input())
        n = int(input())
        d = int(input())
        result = 1
        # print("starting at: " + str(a0-a0%d + d))
        
        for i in range(a0 +d -a0%d,n+1,d):
            result *= i
            # print("result: " + str(result))
            # print("i:"+str(i))
        print (result)
    ex_2a()

elif num == '2b':
    # write your answer for question 2b below
    def A(x:int,n:int,m:int)->int:
        condition = (
            x <= n-x+1
            and
            (x**2 +(n-x+1)**2 ) %m == 0
        )
        # print(x,condition)
        if condition :
            return x**2 +(n-x+1)**2 
        else:
            return 1    

    def ex_2b():
        n = int(input())
        m = int(input())
        result = 1
        for i in range(1,n):
            # print(A(i,n,m))
            result *= A(i,n,m)
        print(result)
    ex_2b()

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
        n = int(input())
        m = int(input())
        
        factors = prime_fact(n)
        total = 1
        for [p,x] in factors :
            # print("prime: "+str(p),"occurences: "+str(x))
            if x%m==0 :
                total *= p**x
            else:
                total *= p*x
            # print("total: "+ str(total))
        
        print("total: "+ str(total))
    ex_2c()

elif num == '3':
    # write your answer for question 3 below
    def ex_3():
        a = int(input())
        b = int(input())

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
    def ex_4a():
        s = input()
        d = int(input())
        result = ''
        for i in range(0,len(s)-len(s)%d,d):
            result += s[i:i+1]
        print(result)
    ex_4a()

elif num == '4b':
    # write your answer for question 4b below
    def ex_4b():
        s1 =" "+ input() +" "
        s2 = input()
        s3 = input()

        res = ''
        index_lst = []

        for i in range(1,len(s1)):
            # print(i)
            if (s1[i] in s2) and ((s1[i+1] in s3) or (s1[i-1] in s3)): 
                index_lst.append(i)

        for i in range(len(s1)):
            if i not in index_lst : res = res + s1[i] 

        print(res)
    ex_4b()

elif num == '4c':
    # write your answer for question 4b below
    def exec_a(phrase:str)->str:
        unique_chars = ["a","e","i","o","u","A","E","I","O","U"]
        result = ''
        for i in range(len(phrase)):
            char = phrase[i]
            if char in unique_chars:
                result += "*"+char+"*"
            else:
                result+=char
        # print("a: "+ result)
        return result

    def exec_b(phrase:str)->str:
        words = phrase.split()
        result =''
        for i in range(len(words)):
            if i%2==1:
                result +=" "+words[i].upper()
            else:
                result +=" "+words[i].lower()
        # print("b: " +result.lstrip())
        return result.lstrip()

    def exec_c(phrase:str)->str:
        words = phrase.split()
        words.sort(reverse=True)
        result = ''
        for word in words:
            result += " "+ word
        # print("c: "+ result.lstrip())
        return result.lstrip()

    def exec_4c():
        phrase = input("enter phrase for parameter s: ")
        test = phrase.split(", ")
        output = ''
        phrase_lst = []

        for sub in test:
            sub = exec_a(sub)
            sub = exec_b(sub)
            sub = exec_c(sub)
            # print("")
            phrase_lst.append((len(sub),sub))
        phrase_lst.sort(key=list[0])

        for phrase in phrase_lst:
            output+=  phrase[1] + ", " 

        # print(phrase_lst)
        print(output.lstrip()[:-2])
        return output.lstrip()[:-2]
    exec_4c()

else:
    print('error')