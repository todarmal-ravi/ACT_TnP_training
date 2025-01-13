def create_graph(number_of_nodes):
    g=[0]
    g=g*number_of_nodes
    for i in range(number_of_nodes):
        g[i]=[0]*number_of_nodes
    for row in range(0,len(g)):
        for column in range(0,len(g)):
            value=int(input(f"From V{row} to V{column}:"))
            g[row][column]=value
    return g

def print_graph(gr):
    for i in gr:
        print (i)

size=int(input("Enter size of graph:"))
g=create_graph(size)
print_graph(g)