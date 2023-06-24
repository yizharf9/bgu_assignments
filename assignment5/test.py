import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from q1_template import euler,plot_funcs
from q2_template import gaussian
from q3_template import import_to_numpy,import_to_pandas
path = "./nci.data.csv"

df = import_to_pandas(path)
labels = import_to_numpy("./nci_labels.txt")
data = df.to_numpy()
data = data[:,1:]
data.astype("float")

s1,s2= df["s1"],df["s2"]

