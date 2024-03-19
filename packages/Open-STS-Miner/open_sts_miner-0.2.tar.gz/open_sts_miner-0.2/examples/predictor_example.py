from Open_STS_Miner import sts_miner
from Open_STS_Miner import sts_predictor
import pandas
import geopandas
import os


#Load sample dataset as an EventDatabase
sample_df = pandas.read_csv(os.path.join("..", "sample_data", "sample_events.csv"))
sample_gdf = geopandas.GeoDataFrame(sample_df, geometry=geopandas.points_from_xy(
	sample_df["X"], 0))

event_database = sts_miner.EventDatabase(sample_gdf, [10], 10)

#Perform mining with Slicing STS Miner
root_node = event_database.mine_events_sliced(1, 2, 2.5, 3)

#Fit prediction model
sts_predictor.fit_sts_predictor(root_node, "sample_predictor.json")
predictor = sts_predictor.load_predictor("sample_predictor.json")

print(f"Prediction for input sequence A: {sts_predictor.make_sts_prediction(predictor, 'A')}")
print(f"Prediction for input sequence B: {sts_predictor.make_sts_prediction(predictor, 'B')}")
print(f"Prediction for input sequence A -> C: {sts_predictor.make_sts_prediction(predictor, 'A -> C')}")

