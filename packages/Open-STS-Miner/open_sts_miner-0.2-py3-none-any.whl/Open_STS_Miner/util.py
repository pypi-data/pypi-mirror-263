def print_node(node):    
	print(node.sequence)
	if node.event_set != None:
		for event in node.event_set:
			print(event.id, end=", ")
	print(f"Density Ratio: {node.density_ratio:.2f}")
	print("\n")


def print_tree(node):
	if len(node.children) == 0:
		return
	
	for child in node.children:
		print_node(child)
	
	print("--------------\n")
	
	for child in node.children:
		print_tree(child)


def print_node_sliced(node):    
	print(node.sequence)
 
	for id in node.join_sets_by_id:
		join_set = node.join_sets_by_id[id]
		print(f"join_set for event {id}: {join_set}")
	print(f"Density Ratio: {node.density_ratio:.2f}")
	print("\n")


def print_tree_sliced(node):
	if len(node.children_by_type) == 0:
		return
	
	for event_type in node.children_by_type:
		child = node.children_by_type[event_type]
		print_node_sliced(child)
	
	print("--------------\n")
	
	for event_type in node.children_by_type:
		child = node.children_by_type[event_type]
		print_tree_sliced(child)


def traverse_tree(node, sequence_ratios: dict):
	sequence_ratios[node.sequence] = node.density_ratio
	
	for child in node.children:
		traverse_tree(child, sequence_ratios)
  
  
def traverse_tree_sliced(node, sequence_ratios: dict, counts: dict, 
                         filter_unique_sequences: bool = True, max_length = 9999):
    seq_length = len(node.sequence.split("->")) + 1 #Bit of a hack...
    
    if seq_length > max_length:
        return
    
    if node.has_different_event_classes or not filter_unique_sequences:
        sequence_ratios[node.sequence] = node.density_ratio
        counts[node.sequence] = len(node.full_event_set)
    
    for event_type in node.children_by_type:
        child = node.children_by_type[event_type]
        traverse_tree_sliced(child, sequence_ratios, counts, filter_unique_sequences, max_length)
        
            