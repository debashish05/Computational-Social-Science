import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

df = pd.read_csv("networkOfFollowers.csv") #Read into a df
G = nx.from_pandas_edgelist(df, 'source', 'target')
num=G.number_of_nodes() #Find the total number of nodes in this graph
print(num)
"""
arr=list(G.nodes)

G_tmp = nx.k_core(G, 10) #Exclude nodes with degree less than 10
from community import community_louvain
partition = community_louvain.best_partition(G_tmp)#Turn partition into dataframe
partition1 = pd.DataFrame([partition]).T
partition1 = partition1.reset_index()
partition1.columns = ['names','group']

G_sorted = pd.DataFrame(sorted(G_tmp.degree, key=lambda x: x[1], reverse=True))
G_sorted.columns = ['names','degree']
G_sorted.head()
dc = G_sorted

combined = pd.merge(dc,partition1, how='left', left_on="names",right_on="names")

pos = nx.spring_layout(G_tmp)
f, ax = plt.subplots(figsize=(10, 10))
plt.style.use('ggplot')#cc = nx.betweenness_centrality(G2)
nodes = nx.draw_networkx_nodes(G_tmp, pos,
                               cmap=plt.cm.Set1,
                               node_color=combined['group'],
                               alpha=0.8)
nodes.set_edgecolor('k')
nx.draw_networkx_labels(G_tmp, pos, font_size=8)
nx.draw_networkx_edges(G_tmp, pos, width=1.0, alpha=0.2)
plt.savefig('debashish_graph.png')
"""
"""
from itertools import combinations

#print(len(list(combinations(G.nodes, 3))))
triad_class = [[],[],[],[]]

for nodes in combinations(G.subgraph(arr).nodes, 3):
            n_edges = G.subgraph(nodes).number_of_edges()
            triad_class[n_edges].append(nodes)


print(len(triad_class[2])," ",len(triad_class[3]))
"""


def get_strongly_cc(G, node):
    """ get storngly connected component of node""" 
    for cc in nx.strongly_connected_components(G):
        if node in cc:
            return cc
    else:
        return set()

def get_weakly_cc(G, node):
    """ get weakly connected component of node""" 
    for cc in nx.weakly_connected_components(G):
        if node in cc:
            return cc
    else:
        return set()



H=G.to_directed()
strong_component = nx.number_strongly_connected_components(H)
weak_component=nx.number_weakly_connected_components(H)

print("Number of connected Components are: ",nx.number_connected_components(G))
print("Number of Strongly connected Components are: ",strong_component)
print("Number of Weakly connected Components are: ",weak_component)
print("Number of attracting Components: ",nx.number_attracting_components(H))
# a strongly connected component with the property that a random walker on 
#the graph will never leave the component, once it enters the component.

print("Number of binconnected components : ",nx.is_biconnected(G))
# It is connected, i.e. it is possible to reach every vertex from every other vertex, by a simple path.
# Even after removing any vertex the graph remains connected.

import itertools


all_connected_subgraphs = 0

# here we ask for all connected subgraphs that have at least 2 nodes AND have less nodes than the input graph
for nb_nodes in range(2, G.number_of_nodes()):
    for SG in (G.subgraph(selected_nodes) for selected_nodes in itertools.combinations(G, nb_nodes)):
        if nx.is_connected(SG):
            all_connected_subgraphs+=1

print("All connected subgraph in the network is: ",all_connected_subgraphs)





"""
combined = combined.rename(columns={"names": "Id"}) #I've found Gephi really likes when your node column is called 'Id'
edges = nx.to_pandas_edgelist(G_tmp)
nodes = combined['Id']
edges.to_csv("edges.csv")
combined.to_csv("nodes.csv")
"""