def build_adjacency_list(edges, directed=False):
    adjecency_list = {}
    if directed == False :
        for edge in edges:
            (start,end)=edge
            if start not in adjecency_list.keys():
                adjecency_list[start]= []
            if end not in adjecency_list.keys():
                adjecency_list[end]= []
            adjecency_list[start].append(end)
            adjecency_list[end].append(start)
    if directed == True :
        for edge in edges:
            (start,end)=edge
            if start not in adjecency_list.keys():
                adjecency_list[start]= []
            if end not in adjecency_list.keys():
                adjecency_list[end]= []
            adjecency_list[start].append(end)
    return adjecency_list

def degrees(graph):
    key_list = graph.keys()
    degree={}
    for key in key_list:
        new_key=key
        value = graph.get(key)
        new_value = len(value)
        degree[new_key]=new_value
    return degree

def in_out_degree(graph):
    key_list = graph.keys()
    out_degree={}
    for key in key_list:
        value = graph.get(key)
        new_value = len(value)
        out_degree[key]=new_value
    in_degree = {}
    for key in key_list:
        key_count=0
        in_degree[key]=key_count
    for key in key_list:
        value_list = graph.get(key)
        for element in value_list:
            current_value=in_degree.get(element)
            in_degree[element] = current_value+1


    return out_degree,in_degree

V = {"P1", "P2", "P3", "P4", "P5"}
E = [("A", "B"),  ("B", "C"), ("C", "A"),("A", "D")]

print(build_adjacency_list(E))
print(degrees(build_adjacency_list(E)))
print(build_adjacency_list(E,True))
print(in_out_degree(build_adjacency_list(E,True)))
