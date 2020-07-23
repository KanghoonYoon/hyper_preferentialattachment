# hyper_preferentialattachment
We proposed **Preferential Attachment on hypergraph with constraint** to predict co-authorship problem. In a variety of research of co-authorship, the simple graph structure is introduced to include the relations between authors or between authors and publications and it is linked by edge connecting 2-pair nodes. However,  the relation of co-authorship has more general form which simultaneously contains several authors(more than 2-pairs) in one edge. This general information can be expressed by **hypergraph**. Also,  **Preferential Attachment(PA)** is well-known graph evolving algorithm. By suggesting the PA on hypergraph, we can design the evolution of co-authorship by general architecture   </i> 

----------

Hypergraph
-------------
![Hypergraph](./image/hyper.PNG)

Hyper PA have more expressivity of graph structure.
For simple graph, Publication 3 information vanishs.

Hyper PA
-------------
![HyperPA](./image/hyperpa.png)

The update(evolution) scheme of co-authorship network.


Node Feature Extraction and Prediction
------------

We use the following features

	- max(Degree) - min(Degree)  (in hyperedge)

	- Averaged Degree (in hyperedge)

	- max(closeness) (in hyperedge)

	- Cluster coefficient

	- Averaged Jaccard similarity (all possible pairs in hyperedge)

	- Adamic Adar index


By passigng the input to MLP model, we get the probability that authors in same hyperedge co-work.

	
