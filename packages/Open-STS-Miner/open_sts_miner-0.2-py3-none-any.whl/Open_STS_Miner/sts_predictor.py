import json
import numpy


"""
Count the occurences of children in node
"""
def __count_sequence_children(node, child_counts: dict):
    if not node.sequence in child_counts:
        child_counts[node.sequence] = {}

    for event_type in node.children_by_type:
        child = node.children_by_type[event_type]
        child_count = len(child.full_event_set)
        child_type = child.event_type

        child_counts[node.sequence][child_type] = child_counts[node.sequence].get(
            child_type, 0) + child_count

    for event_type in node.children_by_type:
        child = node.children_by_type[event_type]
        __count_sequence_children(child, child_counts)


"""
Fit a prediction model to a pattern tree

Parameters
----------
root_node: SlicedSequenceNode representing the root of the pattern tree to be fit
path_save_save: String representing the path to save the predictor to

Returns: None
"""
def fit_sts_predictor(root_node, path_to_save: str = "sts_predictor.json"):
    child_counts = {}  # Maps sequences to dictionaries
                        # Each dictionary maps child event types to counts
    __count_sequence_children(root_node, child_counts)

    sequence_probabilities = {}
    for sequence in child_counts:
        children = []
        child_probabilities = []

        seq_child_counts = child_counts[sequence]
        # Count total child occurences
        total = 0
        for child_seq in seq_child_counts:
            total += seq_child_counts[child_seq]

        if total == 0:
            continue

        # Calculate child probabilities
        for child_seq in seq_child_counts:
            probability = seq_child_counts[child_seq] / total
            children.append(child_seq)
            child_probabilities.append(probability)

        sequence_probabilities[sequence] = [children, child_probabilities]

    with open(path_to_save, "w") as file:
        json.dump(sequence_probabilities, file)


"""
Predict the next event type in a given sequence

Parameters
----------
sequence_probabilities: Dictionary representing probabilities of each child occurring for all sequences in a pattern tree
sequence: String representing the sequence for which the next event is predicted

Returns: Next event type
"""
def make_sts_prediction(sequence_probabilities: dict, sequence: str):
    if not sequence in sequence_probabilities:
        raise Exception(f"Error: Sequence {sequence} not in sequence_probabilities!")
    
    children = sequence_probabilities[sequence][0]
    child_probabilities = sequence_probabilities[sequence][1]
    
    next_sequence = numpy.random.choice(children, p=child_probabilities)
    return next_sequence


"""
Load an STS prediction model

Parameters
----------
path: String denoting path to the model to be loaded

Returns: Dictionary of sequence probabilities
"""
def load_predictor(path: str = "sts_predictor.json"):
    with open(path, "r") as file:
        sequence_probabilities = json.load(file)
        return sequence_probabilities

