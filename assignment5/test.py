
import numpy as np
from matplotlib import pyplot as plt
def y_i(N,f,init,h):
    if N == 0:
        return init
    else:
        y_i_1 = y_i(N-1,f,init,h)
        t_i_1 = (N-1)*h
        return y_i_1 + h * f(t_i_1,y_i_1)



def euler(f, a: float, b: float, initial_cond: float, N=None, h=None):
    # input checking block
    if N == None and h == None:
        raise ValueError("please fill at least one of the required areas: N, h")
    elif N != None and h != None and (b - a) / N != h:
        raise ValueError(
            f"make sure the parameters h and N are mathcing by value \n expected val for h:{h} , val for h:{(b-a)/N}"
        )
    elif N != None:
        h = (b - a) / N
    elif h != None:
        N = int((b - a) / h)

    # arrays to keep data
    arr_t = np.zeros(N+1)
    arr_y = np.zeros(N+1)

    # setting values of array
    arr_y[0] = initial_cond
    arr_t[0] = 0

    for i in range(N):
        t_i_1 = arr_t[i]
        y_i_1 = arr_y[i]

        arr_t[i] = t_i_1
        if i<N:
            arr_y[i+1] = y_i_1 + h * f(t_i_1,y_i_1) 
            arr_t[i+1] = t_i_1 + h 
        # print(y_i_1,y_i,t_i_1,h)

    return arr_t,arr_y


f = lambda t,y : y - t**2 +1
init =  0.5
a = 0
b = 2
N = 10
h = (b-a)/N

res = euler(f,a,b,init,N)
print(res[0])
print(res[1])

print(.5+0.2*(.5-.2**2+1))
print(init+h*f(0.2,init))
