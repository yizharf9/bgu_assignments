# -*- coding: utf-8 -*-
"""
Template for to homework exercise 5, question 1
Fundamentals of CS for EE students 2023
"""

import numpy as np
from matplotlib import pyplot as plt


def euler(f, a: float, b: float, initial_cond: float, N=None, h=None):
    # input checking block
    if N == None and h == None:
        raise ValueError("please fill at least one of the required areas: N, h")
    elif N != None and h != None and (b - a) / N != h:
        raise ValueError(
            f"make sure the parameters h and N are mathcing by value \n expected val for h:{h} , val for h:{(b-a)/N}"
        )
    elif N != None and h == None :
        h = (b - a) / N
    elif h != None and N == None and int((b - a) / h) == (b - a) / h :
        N = int((b - a) / h)
        

    # arrays to keep data
    arr_t = np.zeros(N + 1)
    arr_y = np.zeros(N + 1)

    # setting values of array
    arr_y[0] = initial_cond
    arr_t[0] = 0

    for i in range(N):
        t_i_1 = arr_t[i]
        y_i_1 = arr_y[i]

        arr_t[i] = t_i_1
        if i < N:
            arr_y[i + 1] = y_i_1 + h * f(t_i_1, y_i_1)
            arr_t[i + 1] = t_i_1 + h

    np.reshape(arr_t,(len(arr_t,)))
    np.reshape(arr_y,(len(arr_y,)))
    return arr_t, arr_y

def euler(f, a: float, b: float, initial_cond: float, N=None, h=None):
    # input checking block
    if N == None and h == None:
        raise ValueError("please fill at least one of the required areas: N, h")
    elif N != None and h != None and (b - a) / N != h:
        raise ValueError(
            f"make sure the parameters h and N are mathcing by value \n expected val for h:{h} , val for h:{(b-a)/N}"
        )
    elif N != None and h == None :
        h = (b - a) / N
    elif h != None and N == None and int((b - a) / h) == (b - a) / h :
        N = int((b - a) / h)
        

    # arrays to keep data
    arr_t = np.zeros(N + 1)
    arr_y = np.zeros(N + 1)

    # setting values of array
    arr_y[0] = initial_cond
    arr_t[0] = a

    for i in range(N):
        t_i_1 = arr_t[i]
        y_i_1 = arr_y[i]

        arr_t[i] = t_i_1
        if i < N:
            arr_y[i + 1] = y_i_1 + h * f(t_i_1, y_i_1)
            arr_t[i + 1] = t_i_1 + h

    np.reshape(arr_t,(len(arr_t,)))
    np.reshape(arr_y,(len(arr_y,)))
    return arr_t, arr_y

def plot_funcs(t, y, y_exact):
    plt.figure()  # initialize new figure object
    Y = y_exact(t)
    y = np.array(y)
    t = np.linspace(t[0],t[-1],len(t))
    plt.plot(t,y,linestyle = "dashed",color = "blue")
    plt.plot(t,Y,color = "black")
    
    fig = plt.gcf()  # get current figure, save in variable
    return fig


def plot_error(t, y, y_exact):
    plt.figure()  # initialize new figure object
    arr_error = abs(y-y_exact(t))
    print(arr_error)
    t = np.linspace(t[0],t[-1],len(t))
    plt.plot(t,arr_error)
    fig = plt.gcf()  # get current figure, save in variable
    return fig

if __name__ == "__main__":  
    f = lambda t, y: y - t**2 + 1
    t, y = euler(f, 0, 2, 0.5, N=10)
    y_exact = lambda t: (t + 1) ** 2 - 0.5 * np.exp(t)
    sol_exact = y_exact(t)

    print("t_i \t \t approx \t \t exact \t \t err")
    for t_i, y_i, ye_i in zip(t, y, sol_exact):
        print(f"{t_i:.2f}\t \t {y_i:.2f}\t \t{ye_i:.2f}\t \t {ye_i-y_i:.2f}")

    fig1 = plot_funcs(t, y, y_exact)
    # plt.show() # uncomment to see plot, but add comment back before submitting
    fig2 = plot_error(t, y, y_exact)
    # plt.show() # uncomment to see plot, but add comment back before submitting

    f = lambda t, y: np.cos(2 * t) + np.sin(3 * t)
    t, y = euler(f, 0, 1, 1, h=0.25)
    y_exact = lambda t: 1 / 2 * np.sin(2 * t) - 1 / 3 * np.cos(3 * t) + 4 / 3

    sol_exact = y_exact(t)

    print("t_i \t \t approx \t \t exact \t \t err")
    for t_i, y_i, ye_i in zip(t, y, sol_exact):
        print(f"{t_i:.2f}\t \t {y_i:.2f}\t \t{ye_i:.2f}\t \t {ye_i-y_i:.2f}")

    fig3 = plot_funcs(t, y, y_exact=y_exact)
    # plt.show() # uncomment to see plot, but add comment back before submitting
    fig4 = plot_error(t, y, y_exact)
    # plt.show() # uncomment to see plot, but add comment back before submitting
