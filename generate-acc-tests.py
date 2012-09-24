import random

# Select a random number of nodes between 1 and 100, and a random number of rules between 1 and num_nodes
for i in range(100) :
    num_nodes = random.randint(1, 100)
    output = str(num_nodes) + " "
    rulesOut = ""
    ruleCount = 0

    # Generate and print consistent rules
    parent_list = []
    free_list = [i for i in range(1, (num_nodes + 1))]
    # Select a random node as the root, and remove it from the free list bitmap
    root_node = random.randint(1, num_nodes)
    parent_list.append(root_node)
    free_list.remove(root_node) # Poor performance, but allows for the 0 index to be neglected with future use of pop
    # Generate rules
    while len(free_list) > 0 :
        num_free = len(free_list)
        select_num = random.randint(1, num_free)
        for j in range(select_num) :
            preds = []
            for k in parent_list :
                if random.randint(1, 100) < 26 :
                    preds.append(k)
            if len(preds) != 0 :
                ruleCount += 1
                child = free_list.pop(random.randint(0, num_free - 1))
                num_free = len(free_list)
                rulesOut += str(child) + " "
                rulesOut += str(len(preds))
                for k in preds :
                    rulesOut += " " + str(k)
                parent_list.append(child)
                rulesOut += "\n"  
            else :
                child = free_list.pop(random.randint(0, num_free - 1))
                num_free = len(free_list)
                parent_list.append(child)
    output += str(ruleCount) + "\n"
    output += rulesOut + "\n"
print output ,