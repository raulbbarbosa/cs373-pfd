import random

# Select a random number of nodes between 1 and 20, and a random number of rules between 1 and num_nodes
for i in range(100) :
	num_nodes = random.randint(1, 100)
	num_rules = random.randint(0, num_nodes - 1)
	print str(num_nodes) + " " + str(num_rules)
	
adj_matrix = [[0 for i in range(num_nodes + 1)] for j in range(num_nodes + 1)]
	
# Generate and print consistent rules
'''
free_list = []
for i in range(num_rules) :
    node = random.randint(1, num_nodes)
    for j in range(1, num_nodes + 1) :
        if j != node and random.randint(10) < 3 :
        
            adj_matrix[node][j] = 1
    free_list += []
'''
    
def find_cycle(root, mark_list, adj_matrix)

    for adj_node in range(1, len(adj_matrix)) :

        if(ajd_matrix[adj_node][root] ==1) # I have an edge to adj_node    
            if(mark_list[adj_node] == GREY)
                return True
            else 
                mark_list[adj_node] = GREY
                if find_cycle(adj_node, mark_list, adj_matrix)
                    return True
    return False
                    
        


