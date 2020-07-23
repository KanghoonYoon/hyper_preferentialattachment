import numpy as np
import random
from src.utils import *


def hyper_PA(Data_class, m=8, update_iter=1000, mu=3, rejection_type = 'jaccard', threshold = 0):
    def calculate_prob(degrees):
        prob = dict()
        deg_sum = np.sum([deg for deg in degrees.values()])
        for node, degree in degrees.items():
            prob[node] = degree / deg_sum
        return prob

    if rejection_type is None:
        similarity_measure = no_similarity
    elif rejection_type == 'jaccard':
        similarity_measure = averaged_jaccard_similarity
    elif rejection_type == 'adamic_adar':
        similarity_measure = adamic_adar
    time_sequence = list(np.random.poisson(mu, update_iter))

    ## select m node
    for num_add_node in time_sequence:
        node_choices = random.choices(list(Data_class.nodes), k=m)
        p = calculate_prob(Data_class.degrees)

        for node1 in node_choices:
            while 1:

                new_edge = [node1] + list(random.choices(list(p.keys()), weights=list(p.values()), k=num_add_node))
                edge_similarity = similarity_measure(Data_class, new_edge)

                if (new_edge not in Data_class.edges.values()) & (edge_similarity > threshold):

                    Data_class.add_edge(new_edge)
                    break

            ## in addition to adding edge, other self feature should be updated.
            ## have to restrict the maximum length of hyper edges
            ## 2-hop

def predict(Graph, edge):

    if edge in Graph.edges.values():
        pred = True
    else:
        pred = False

    return pred

def evaluate(Graph, Query):

    tp = tn = fp = fn = 0

    for i in range(len(Query.query)):

        pred = predict(Graph, Query.query[i])

        if (Query.answer == True) & (pred == True):
            tp += 1
        elif (Query.answer == True) & (pred == False):
            tn += 1
        elif (Query.answer == False) & (pred == True):
            fp += 1
        elif (Query.answer == False) & (pred == False):
            fn += 1

    precision = tp / (tp+fp)
    recall = tp / (tp+tn)
    f1 = 2*precision*recall/(precision+recall)
    return precision, recall, f1


