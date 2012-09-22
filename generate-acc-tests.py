import random

# Select a random number of nodes between 1 and 20, and a random number of rules between 1 and num_nodes
for i in range(100) :
	num_nodes = random.randint(2, 100)
	num_rules = random.randint(1, num_nodes - 1)
	print str(num_nodes) + " " + str(num_rules)
	
adj_matrix = [([0] * (num_nodes + 1))] * (num_nodes + 1)
	
# Generate and print consistent rules
for i in range(num_rules) :
            
