# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Template for HW5 question 3, Fundamentals of CS for EE, 2023
In this exercise we analyze gene expression data from samples of tissue taken
from cancer tumors of different types using K-means clustering and hierarchical
clustering.

The data were acquired by microarray experiments conducted by the National
Cancer Institute. The data set for this exercise is taken from the website
https://hastie.su.domains/ElemStatLearn/

Each sample has a label decribing the type of tumor it was taken from. The
labels for each sample are available in a separate text file. We will not use
these labels for the clustering procedure itself, but we will use them to see
which categories the samples fall in and to get a sense of how successful the
different clustering techniques are.
"""
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as shc
from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
from typing import Dict, List, Union


def import_to_pandas(filepath):
    """
    Import csv to pandas dataframe
    """
    df = pd.read_csv(filepath)
    return df


def import_to_numpy(filepath, dtype=str):
    """
    Import csv to numpy array
    """
    arr = np.loadtxt(filepath, dtype=dtype)
    return arr


def clean_data(data: np.ndarray):
    # Task 1: remove the first column with the labels for the genes.
    data = data[:, 1:]
    #
    # The original data frame contained a mixture of string types and float
    # types.
    # In a numpy array the data type of all the entries must be identical.
    # What is the data type of our numpy array?
    #
    # Task 2: complete the print statement that will return the data type:
    print(f"Current data type:{data.dtype}")
    #
    # Task 3: Convert the array to floats so we can work with it.
    data = data.astype("float")
    # print the data type again so we can be sure that the conversion worked:
    print(f"Converted data type:{data.dtype}")
    #
    # In order to use k-means and hierarchical clustering, we need to provide
    # an array where each row is an observation and each column is a
    # measurement. Currently, the columns are the observations (each sample is
    # a different observation), and the rows are the measurements
    # (gene expression levels). To fix this, we need to transpose the array.
    #
    # Task 4: fill in the command to transpose the array:
    data = data.T
    return data


def get_unique_categories(array: np.ndarray) -> int:
    """
    Prints the names of the unique values in an array.
    Prints the number of unique values (categories) in an array.
    Returns the number of unique values (categories).
    """
    array = np.unique(array)
    print(array)
    print(len(array))
    return len(array)


def by_clust_num(
    predictions: np.ndarray, actual: Union[List, np.ndarray]
) -> Dict[int, List]:
    # num_clusters = len(np.unique(predictions)) #! this is how its supposed to be!!!
    dic = {i: [] for i in np.unique(predictions)}
    for i, label in enumerate(actual):
        dic[predictions[i]].append(label)
    return dic


def by_label(
    actual: Union[List, np.ndarray],
    predictions: np.ndarray,
    num_clusters=1,
    zero_index=True,
) -> Dict[str, List[int]]:
    
    labels = np.unique(actual)
    dic = {label: [0]*num_clusters for label in labels}
    addition = 1 if not zero_index else 0

    for i, actual_label in enumerate(actual):
        index = predictions[i] - addition
        dic[actual_label][index] += 1

    return dic
    """
    Parameters
    ----------
    actual: TYPE List
        DESCRIPTION. List of actual (ground truth) labels of observations.
    predictions : TYPE List[int]
        DESCRIPTION. List of cluster numbers assigned to observations by
        clustering algorithm prediction.
    num_clusters: Type int.
        DESCRIPTION. The number of clusters. Default 1.
    zero_index: Type Bool.
        DESCRIPTION. Indicates whether the cluster numbers start at 0
        (default = True) or at 1 (False).

    Returns
    -------
    by_clust: TYPE Dict[int, List]
        DESCRIPTION. A dictionary where the keys are the observation labels
        and the values are a list of length num_clusters.
        The value in the i^th position is the number of observations
        classified to the i^th cluster.
    """


def rescale_data(data: np.ndarray):
    # aquiring the standard deviation from each gene
    m = data.shape[0]
    # std_deviation = np.array([np.std(data, 0)] * m)
    std_deviation = np.std(data, 0)
    # columns_min = np.array([data.mean(0)] * m)
    new_data = np.array(data / (std_deviation))
    return new_data


def plot_dendrogram(Z, labels=None, title=None, ylabel=None, xlabel=None):
    plt.figure()  # initialize new figure object
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    shc.dendrogram(Z, leaf_rotation=90, labels=labels)
    fig = plt.gcf()  # get current figure, save in variable
    return fig


# Write a function that receives a linkage matrix Z and a number of clusters
# (num_clusters)
# and returns a threshold: the height of the horizontal line that slices the
# dendrogram and produces the number of clusters.
# The threshold should be exactly halfway between the height of the split of
# the dendrogram into num_clusters and the split into num_clusters + 1 .
def threshold(Z, num_clusters=2):
    """
    Parameters
    ----------
    Z : TYPE np.ndarray
        DESCRIPTION. Linkage matrix produced by hierarchical clustering.
    num_clusters : TYPE int
        DESCRIPTION. The number of clusters to divide the data into.
        The default is 2.

    Returns
    -------
    TYPE float
        DESCRIPTION. The height of the horizontal line that slices the
        dendrogram representing the hierarchical clustering exactly halfway
        between num_clusters and num_clusters + 1.

    """
    merge_heights = Z[:, 2]
    avg = (merge_heights[-num_clusters] + merge_heights[-(num_clusters - 1)]) / 2
    return avg


def n_most_frequent(list:list, n):
    """
    Return a list of n most frequent values in list, sorted from highest
    frequency to lowest.
    """
    freq_dic = {}
    for cancer in list:
        if freq_dic.get(cancer,0) == 0:
            freq_dic[cancer] = 0 
        freq_dic[cancer] +=1 
    sorted_dic = sorted((freq_dic.items()),key=lambda x: x[1],reverse=True)
    top_n = [x[0] for x in  sorted_dic[:n]]
    return top_n


def clustering_success_check(Z, labels, n):
    """
    Parameters
    ----------
    Z : TYPE np.ndarray
        DESCRIPTION. Linkage matrix.
    labels : TYPE np.ndarray
        DESCRIPTION. Labels of observations.
    n : TYPE int
        DESCRIPTION. n most frequent observations in data set to for which to
                    check success of clustering into n clusters.

    Returns
    -------
    success : TYPE List[Bool]
        DESCRIPTION. A list recording the success of clustering for the n most
                        frequent types of observations. Success = True,
                        Failure = False.
    """
    n_most_freq = n_most_frequent(labels,n)
    predictions = shc.fcluster(Z=Z,t=threshold(Z,n),criterion="distance")
    predictions = [(labels[i],predictions[i]) for i in range(len(labels))]
    successes = []
    for one in n_most_freq:
        successes.append(success(one,predictions))
    return successes

def success(label,predictions):
    possible_clusters = set()
    for prediction in predictions:
        if prediction[0] == label:
            possible_clusters.add(prediction[1])
    if len(possible_clusters)>1:
        # print(possible_clusters)
        # print(f"Clustering unsuccessful for {label}")
        return False
    return True


def main():
    # use pandas to read the National Cancer Institute gene expression data
    # into a dataframe object:
    path_to_file = "nci.data.csv"
    df = import_to_pandas(path_to_file)
    # Read the labels for each sample into a numpy array:
    path_to_labels = "nci_labels.txt"
    labels = import_to_numpy(path_to_labels)
    data = df.to_numpy()
    #
    # Tasks 1 - 4: complete the function to return cleaned data.
    data = clean_data(data)  # TODO
    #
    # First, let's count the number of different types of tumors according to
    # the labels. This will be the number of clusters we'll use to categorize
    # the data.
    # Task 5: fill in the function.
    num_clusters = get_unique_categories(labels)
    #
    # Task 6: Initialize a kmeans object and use it to categorize the data.
    # Provide the following arguments to initialize the Kmeans object:
    # n_clusters = the number of different tumor types (num_clusters)
    # random_state=10 (This is important to ensure that your results match the
    # automated tests in the VPL.)
    kmeans = KMeans(n_clusters=num_clusters, random_state=10).fit(data)
    #
    # Task 7: Use of the method 'predict' in the Kmeans class to  get the
    # cluster number for each observation.
    predictions = kmeans.predict(X=data)
    print(predictions)
    #
    # An ideal clustering would put each tumor type in exactly one cluster. To
    # see how well the clustering works, define a dictionary where the keys are
    # the ID numbers of the clusters (integers from 0 to the number of
    # clusters) and the values are the cancer types that land in the cluster.
    # For example, if cluster number 3 contains 2 cancers of type MELANOMA and
    # one of type LEUKEMIA, then
    # by_clust_km[3]=['MELANOMA', 'MELANOMA', 'LEUKEMIA']
    #
    # Task 8: complete the function to fill in the dictionary:
    by_clust_km = by_clust_num(predictions, labels)
    #
    # Alternatively, we might want to view the results by cancer type: for each cancer
    # type, we'll want to see which clusters it lands in. For this, define a dictionary
    # where the keys are the types of cancer and the values are a list whose length
    # is the number of clusters and whose entries are the number of types the cancer
    # appear in each cluster.
    # For example, if 4 samples of type 'MELANOMA' land in cluster number 0, and 2 samples
    # of type 'MELANOMA' land in cluster number 4, then
    # by_cancer_km['MELANOMA'] = [4, 0, 0, 0, 2, 0, 0 ...]
    #
    # Task 9: Compelete the function to fill in the dictionary:
    by_cancer_km = by_label(labels, predictions, num_clusters=num_clusters)
    # by_cancer_km = np.array([sum(val) for val in by_cancer_km.values()])
    #
    # One of the problems with the data we are working with is that each gene can
    # produce measurements in a different range of numbers. For example, the values
    # for gene1 might fall in the interval [0,1] and the values for gene2 might fall
    # in the interval [0, 1000]. This can lead to poor performance when attempting
    # to cluster the data.
    # A common practice to improve the performance of k-means is to rescale (normalize)
    # the data. Divide the measurements for each gene by their standard deviation across all
    # samples so that they all fall into a comparable range.
    #
    # Task 10: complete the assignment to rescale the data:
    data_rescale = rescale_data(data)
    df = pd.DataFrame(data_rescale)
    # print(df)  # ?

    #
    # Task 11:
    # Repeat the clustering on the rescaled data, and enter the results in a
    # dictionary by cluster number and in a dictionary by tumor type, as in the
    # previous step.
    kmeans_rs = KMeans(n_clusters=num_clusters, random_state=10).fit(data_rescale)
    predictions_rs = kmeans_rs.predict(X=data_rescale)

    by_clust_km_rs = by_clust_num(predictions_rs, labels)  # TODO
    by_cancer_km_rs = by_label(
        labels, predictions_rs, num_clusters=num_clusters
    )  # TODO
    #
    # Use hierarchical clustering to divide the samples into
    # nested categories.
    # https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
    # Use scipy.cluster.hierarchy module, with the method 'linkage'
    # (with argments method='ward', metric = 'euclidean')
    # to obtain the linkage matrix.
    # Use the unscaled data (not the rescaled data) for this section.
    #
    # Task 12: fill in the command to assign the linkage matrix to the variable
    # clusters below:
    clusters = shc.linkage(data, metric="euclidean", method="ward")
    #
    # Use the method 'dendrogram' to
    # plot the results. Include the labels of the cancer types at the leaf of the tree.
    # To see the results clearly, it is recommended to use font size 5 for the labels
    # and to rotate them so that they are at 90 degrees to the x axis.
    fig1 = plot_dendrogram(
        clusters,
        labels=labels,
        title="Hierarchical Clustering of Gene Expression \n From NCI Samples",
        xlabel="observations",
        ylabel="distance",
    )

    # plt.show() # uncomment to see plot, but add comment back before submitting
    #
    # Use the linkage matrix to find the threshold. i.e., the height of the
    # horizontal line that slices the dendrogram tree into a given number of clusters.
    # Reminder: the heights of each merge are given in the 3rd column of the linkage
    # matrix. Thus, the height of the top of the tree (when the final two clusters merge into
    # one big cluster, or, conversely, when one big cluster splits in two)is in the
    # last row of the linkage matrix. The height of the split into
    # three clusters is in the row before the last, etc.
    #
    # Task 13: complete the function:
    thresh = threshold(clusters, num_clusters)
    #
    # Task 14: Add a horizontal line to the dendrogram graph at the height that
    # will result in the same number of clusters used previously in the kmeans
    # clustering.
    # You should use the matplotlib command axhline() for this.
    # To see the result clearly, use a line width of 0.5.
    # Store the result in the variable fig2 below.
    #
    fig2 = plot_dendrogram(
        clusters,
        labels=labels,
        title="Hierarchical Clustering of Gene Expression \n From NCI Samples",
        xlabel="observations",
        ylabel="distance",
    )
    plt.axhline(thresh).set_linewidth(0.5)
    # plt.show() # uncomment to see plot, but add comment back before submitting
    #
    # Task 15: Use 'fcluster' to attach the cluster ID number
    # (integers from 1 to the number of clusters) to each observation.
    # Use the argument criterion='distance'.
    x = shc.fcluster(Z=clusters, t=thresh, criterion="distance")
    predictions_hc = np.array([i - 1 for i in x])
    #
    # (Note that unlike the method 'predict' in the Kmeans class,  'fcluster'
    # returns cluster numbers starting from 1, not from 0.)
    # Store the results in two dictionaries, as you did for the results of
    # kmeans: one with cluster numbers as keys and one with tumor labels as
    # keys.
    by_clust_hc = by_clust_num(predictions_hc, labels)
    by_cancer_hc = by_label(
        labels, predictions_hc, num_clusters=num_clusters, zero_index=False
    )
    # Task 16: We can see that our data contains more samples from some cancer
    # types than others. Return a list with the names of the 5 most common
    # cancer types in the data, sorted from highest frequency to lowest
    # frequency.
    freq_cancers = n_most_frequent(labels, 5)  # TODO : complete function
    #
    # Suppose we only care about the 5 most frequent types of cancer, and we
    # want each type to be classified into exactly one of 5 clusters.
    # Will using hierarchical clustering with a threshold of 5 clusters work?
    #
    # Task 17: Write a function that iterates over a list of the N most
    # frequent cancers, prints 'Clustering unsuccessful for' + {name of cancer}
    # and records whether the clustering succeeded or failed
    # in a boolean list of length N (success = True, failure = False)
    successes = clustering_success_check(
        clusters, labels, 5
    )  

    return (
        labels,
        data,
        data_rescale,
        num_clusters,
        by_clust_km,
        by_cancer_km,
        by_clust_km_rs,
        by_cancer_km_rs,
        by_clust_hc,
        by_cancer_hc,
        thresh,
        freq_cancers,
        successes,
        fig1,
        fig2,
    )


if __name__ == "__main__":
    (
        labels,
        data,
        data_rescale,
        num_clusters,
        by_clust_km,
        by_cancer_km,
        by_clust_km_rs,
        by_cancer_km_rs,
        by_clust_hc,
        by_cancer_hc,
        thresh,
        freq_cancers,
        successes,
        fig1,
        fig2,
    ) = main()
