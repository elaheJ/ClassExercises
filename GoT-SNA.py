import networkx as nx
import matplotlib.pyplot as plt

#create a graph with all characters
GoT=nx.Graph()
# adding 20 characters
GoT.add_nodes_from(['Daenerys','Howland','AerysII','Jaime','Viserys',
'Lyanna','Elia','Robert','JonArryn','RhaenysNAegon','Ned','Gregor',
'Rhaella','Rickard','Arthur','JonSnow','Benjen', 'Rhaegar','Brandon',
'Tywin'])
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# abduction links  - we create another graph for it - but it has to be directed because abduction is a directionalc relationship
Abduct=nx.DiGraph()
#adding the links - there's only 1 instance of it
Abduct.add_edges_from ([('Rhaegar','Lyanna')], label='abducted')
#extracting labels from the list of edges
Abduct_labels=nx.get_edge_attributes(Abduct, 'label')
#--------------------------------------------------------------------------

#---------------------------------------------------------------------------
# served links - - we create another graph for serve links - it has to be directed because Serve is a directional relationship
Serve=nx.DiGraph()
#adding the links - here are 3 instances of it
Serve.add_edges_from([('Arthur', 'AerysII'), ('Jaime','AerysII'),('Gregor','Tywin')], label='served') 
#extracting labels from the list of edges
Serve_labels=nx.get_edge_attributes(Serve, 'label')
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# Guardian links - - we create another graph for serve links - it has to be directed because Guardian is a directional relationship 
Guardian=nx.DiGraph()
#Guardian the links - there are 3 instances of it
Guardian.add_edges_from([('Ned', 'JonSnow'), ('JonArryn','Robert'),('JonArryn','Ned')],label='guardian')
#extracting labels from the list of edges
Guardian_labels=nx.get_edge_attributes(Guardian, 'label')
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#kill links - we create another graph for serve links - it has to be directed because Kill is a directional relationship
Kill=nx.DiGraph()
#Guardian the links - there are 8 instances of it
Kill.add_edges_from([('Ned', 'Arthur'), ('Gregor','RhaenysNAegon'),('Gregor','Elia'),('Howland', 'Arthur'),('AerysII','Brandon'),('AerysII','Rickard'),('Jaime','AerysII'),('Robert','Rhaegar')], label='killed') 
#extracting labels from the list of edges
Kill_labels=nx.get_edge_attributes(Kill, 'label')
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#redrawing nodes and Abduct links
plt.figure(1,figsize=(12,12))
pos=nx.circular_layout(GoT)
nx.draw(GoT, pos,node_color='grey', node_size=5, with_labels=True)
nx.draw_networkx_edges(Abduct, pos, edge_color='deeppink')
nx.draw_networkx_edge_labels(Abduct, pos, edge_labels=Abduct_labels, label_pos=0.2, 
font_color='deeppink')
#overlaying Serve links on GoT and Abduct links
#drawing the purple Serve edges
nx.draw_networkx_edges(Serve, pos, edge_color='purple')
#adding purple Serve labels to the grarph
nx.draw_networkx_edge_labels(Serve, pos, edge_labels=Serve_labels, label_pos=0.2, 
font_color='purple')
#overlaying Guardian links on GoT and Abduct+Serve links
#drawing the blue Guardian edges
nx.draw_networkx_edges(Guardian, pos, edge_color='blue')
#adding blue Guardian labels to the grarph
nx.draw_networkx_edge_labels(Guardian, pos, edge_labels=Guardian_labels, label_pos=0.2, 
font_color='blue')
#overlaying Kill links on GoT and Abduct+Serve+Guardian links
#drawing green Kill edges
nx.draw_networkx_edges(Kill, pos, edge_color='green')
#extracting labels from the list of edges
Kill_labels=nx.get_edge_attributes(Kill, 'label')
#adding green Kill labels to the grarph
nx.draw_networkx_edge_labels(Kill, pos, edge_labels=Kill_labels, label_pos=0.2, 
font_color='green')
plt.show()
#---------------------------------------------------------------------------
