from Open_STS_Miner import sts_miner
from Open_STS_Miner import util
import pandas
import geopandas
import os


#Load sample dataset as an EventDatabase
sample_df = pandas.read_csv(os.path.join("..", "sample_data", "sample_events.csv"))
sample_gdf = geopandas.GeoDataFrame(sample_df, geometry=geopandas.points_from_xy(
	sample_df["X"], 0))

event_database = sts_miner.EventDatabase(sample_gdf, [10], 10)

#Calculate global density of different event types
density_A = event_database.calc_global_density("A")
print(f"Global density of event type A: {density_A:.2f}")

density_B = event_database.calc_global_density("B")
print(f"Global density of event type B: {density_B:.2f}")

density_C = event_database.calc_global_density("C")
print(f"Global density of event type C: {density_C:.2f}")

print()

#Perform mining with Naive STS Miner
root_node = event_database.mine_events_naive(1, 2, 2.5)

#Extract sequence ratios from pattern tree
sequence_ratios = {}
util.traverse_tree(root_node, sequence_ratios)

print("Naive STS Miner Results:")
print(f"Sequence index for A -> B: {sequence_ratios['A -> B']:.2f}")
print(f"Sequence index for A -> C: {sequence_ratios['A -> C']:.2f}")

print(f"Sequence index for A -> C -> A: {sequence_ratios['A -> C -> A']:.2f}")
print(f"Sequence index for A -> C -> B: {sequence_ratios['A -> C -> B']:.2f}")

print(f"Sequence index for A -> C -> A -> B: {sequence_ratios['A -> C -> A -> B']:.2f}")
print(f"Sequence index for A -> C -> A -> C: {sequence_ratios['A -> C -> A -> C']:.2f}")

#Perform mining with Slicing STS Miner
root_node = event_database.mine_events_sliced(1, 2, 2.5, 3)

#Extract sequence ratios and counts from pattern tree
sequence_ratios = {}
counts = {}
util.traverse_tree_sliced(root_node, sequence_ratios, counts)

print("Slicing STS Miner Results:")
print(f"Sequence index for A -> B: {sequence_ratios['A -> B']:.2f}")
print(f"Sequence index for A -> C: {sequence_ratios['A -> C']:.2f}")

print(f"Sequence index for A -> C -> A: {sequence_ratios['A -> C -> A']:.2f}")
print(f"Sequence index for A -> C -> B: {sequence_ratios['A -> C -> B']:.2f}")

print(f"Sequence index for A -> C -> A -> B: {sequence_ratios['A -> C -> A -> B']:.2f}")
print(f"Sequence index for A -> C -> A -> C: {sequence_ratios['A -> C -> A -> C']:.2f}")

