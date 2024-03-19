from sts_miner import *
from util import *
import pandas
import os
import unittest
from shapely.geometry import Polygon


class TestEventDatabase(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sample_df = pandas.read_csv(os.path.join("..", "..", "sample_data", "sample_events.csv"))
        
        self.sample_gdf = geopandas.GeoDataFrame(self.sample_df, geometry=geopandas.points_from_xy(
            self.sample_df["X"], 0))
             
        #sample_df["Coordinates"] = sample_df["X"].apply(lambda x: numpy.array([x]))
        #sample_df.drop(columns=["X"])

        self.event_database = EventDatabase(self.sample_gdf, [10], 10)
      
        
    def test_global_density(self):
        density_A = self.event_database.calc_global_density("A")
        self.assertEqual(density_A, 0.04)
        
        density_B = self.event_database.calc_global_density("B")
        self.assertEqual(density_B, 0.16)
        
        density_C = self.event_database.calc_global_density("C")
        self.assertEqual(density_C, 0.06)
        
        
    def test_local_density(self):
        buffer_dist = 2
        time_threshold = 2.5
        
        events_df = self.event_database.events_df
        
        event1 = events_df[events_df["ID"] == 1]
        density_b_V1 = self.event_database.calc_density_around_point(self.event_database.events_df, "B", event1, buffer_dist, event1.Time.iloc[0], time_threshold)
        self.assertEqual(density_b_V1, 0)
        
        event2 = events_df[events_df["ID"] == 2]
        density_b_V2 = self.event_database.calc_density_around_point(self.event_database.events_df, "B", event2, buffer_dist, event2.Time.iloc[0], time_threshold)
        self.assertEqual(density_b_V2, 0.4)
        
        event3 = events_df[events_df["ID"] == 3]
        density_b_V3 = self.event_database.calc_density_around_point(self.event_database.events_df, "B", event3, buffer_dist, event3.Time.iloc[0], time_threshold)
        self.assertEqual(density_b_V3, 0.5)
        
        event4 = events_df[events_df["ID"] == 4]
        density_b_V4 = self.event_database.calc_density_around_point(self.event_database.events_df, "B", event4, buffer_dist, event4.Time.iloc[0], time_threshold)
        self.assertEqual(density_b_V4, 0.3)
        
    
    def test_naive_mining(self):        
        root_node = self.event_database.mine_events_naive(1, 2, 2.5)
                
        sequence_ratios = {}
        traverse_tree(root_node, sequence_ratios)
        
        self.assertAlmostEqual(sequence_ratios["A -> B"], 1.88, 2)
        self.assertAlmostEqual(sequence_ratios["A -> C"], 2.08, 2)
        
        self.assertAlmostEqual(sequence_ratios["A -> C -> A"], 1.25, 2)
        self.assertAlmostEqual(sequence_ratios["A -> C -> B"], 1.09, 2)
        
        self.assertAlmostEqual(sequence_ratios["A -> C -> A -> B"], 2.50, 2)
        self.assertAlmostEqual(sequence_ratios["A -> C -> A -> C"], 1.67, 2)
        
        self.assertFalse("A -> A" in sequence_ratios)
        self.assertFalse("A -> C -> C" in sequence_ratios)
        self.assertFalse("A -> C -> A -> A" in sequence_ratios)
        

    def test_slicing_length_4(self):
        slice_dfs, event_sets, overlap_sets = self.event_database.split_into_slices(2.5, 4, self.event_database.events_df)
        
        slices = []
        for slice_df in slice_dfs:
            slice_set = set(slice_df["ID"].tolist())
            slices.append(slice_set)
        
        for id in [1, 2, 3, 16, 17, 19, 20, 21, 22, 23, 25, 15, 24, 26]:
            self.assertTrue(id in slices[0])
        
        for id in [4, 5, 7, 8, 9, 10, 12, 13, 14, 6, 11, 18]:
            self.assertFalse(id in slices[0])
            
        self.assertTrue(len(slices[0].intersection(slices[1])) > 0)
        
        for id in [2, 3, 10, 12, 13, 14, 16, 17, 20, 21, 22, 23, 25, 11, 15, 24, 26]:
            self.assertTrue(id in slices[1])
        
        for id in [1, 4, 5, 7, 8, 9, 19, 6, 18]:
            self.assertFalse(id in slices[1])
            
        self.assertTrue(len(slices[1].intersection(slices[2])) > 0)
        
        for id in [3, 4, 10, 12, 13, 14, 20, 21, 22, 25, 11, 18, 26]:
            self.assertTrue(id in slices[2])
        
        for id in [1, 2, 5, 7, 8, 9, 16, 17, 19, 23, 6, 15, 24]:
            self.assertFalse(id in slices[2])
            
        self.assertTrue(len(slices[2].intersection(slices[3])) > 0)
        
        for id in [4, 5, 7, 8, 9, 12, 13, 14, 6, 18]:
            self.assertTrue(id in slices[3])
        
        for id in [1, 2, 3, 10, 16, 17, 19, 20, 21, 22, 23, 25, 15, 24, 26]:
            self.assertFalse(id in slices[3])


    def test_slicing_length_5(self):
        slice_dfs, event_sets, overlap_sets = self.event_database.split_into_slices(2.5, 5, self.event_database.events_df)
        
        slices = []
        for slice_df in slice_dfs:
            slice_set = set(slice_df["ID"].tolist())
            slices.append(slice_set)
            
        for id in [1, 2, 3, 10, 11, 12, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26]:
            self.assertTrue(id in slices[0])
        
        for id in [4, 5, 7, 8, 9, 13, 14, 6, 18]:
            self.assertFalse(id in slices[0])
            
        self.assertTrue(len(slices[0].intersection(slices[1])) > 0)
        
        for id in [3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 16, 18, 20, 21, 22, 23, 25, 26]:
            self.assertTrue(id in slices[1])
        
        for id in [1, 2, 7, 9, 15, 17, 19, 24]:
            self.assertFalse(id in slices[1])
            
        self.assertTrue(len(slices[1].intersection(slices[2])) > 0)
        
        for id in [4, 5, 6, 7, 8, 9, 13, 14, 18]:
            self.assertTrue(id in slices[2])
        
        for id in [1, 2, 3, 10, 11, 12, 16, 17, 19, 20, 21, 22, 23, 15, 24, 25, 26]:
            self.assertFalse(id in slices[2])


    def test_slicing_length_3(self):
        slice_dfs, event_sets, overlap_sets = self.event_database.split_into_slices(2.5, 3, self.event_database.events_df)
        
        slices = []
        for slice_df in slice_dfs:
            slice_set = set(slice_df["ID"].tolist())
            slices.append(slice_set)
        
        #0 - 3
        
        for id in [1, 2, 15, 16, 17, 19, 23, 24]:
            self.assertTrue(id in slices[0])
        
        for id in [3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 6, 11, 18, 20, 21, 22, 25, 26]:
            self.assertFalse(id in slices[0])
            
        self.assertTrue(len(slices[0].intersection(slices[1])) > 0)
        
        #0.5 - 3.5
        
        for id in [1, 2, 15, 16, 17, 19, 22, 23, 24]:
            self.assertTrue(id in slices[1])
        
        for id in [3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 6, 11, 18, 20, 21, 25, 26]:
            self.assertFalse(id in slices[1])
            
        self.assertTrue(len(slices[1].intersection(slices[2])) > 0)
        
        #1 - 4
        
        for id in [1, 2, 3, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26]:
            self.assertTrue(id in slices[2])
        
        for id in [4, 5, 7, 8, 9, 10, 12, 13, 14, 6, 11, 18, 19]:
            self.assertFalse(id in slices[2])
            
        self.assertTrue(len(slices[2].intersection(slices[3])) > 0)
        
        #1.5 - 4.5    
    
        for id in [2, 3, 10, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26]:
            self.assertTrue(id in slices[3])
        
        for id in [1, 4, 5, 7, 8, 9, 12, 13, 14, 6, 11, 18, 19]:
            self.assertFalse(id in slices[3])
            
        self.assertTrue(len(slices[3].intersection(slices[4])) > 0)
            
        #2 - 5
            
        for id in [3, 10, 11, 12, 15, 16, 20, 21, 22, 23, 25, 26]:
            #self.assertTrue(id in slices[3])
            self.assertIn(id, slices[4])
        
        for id in [1, 2, 4, 5, 7, 8, 9, 13, 14, 6, 17, 18, 19, 24]:
            self.assertFalse(id in slices[4])
            
        self.assertTrue(len(slices[4].intersection(slices[5])) > 0)
            
        #2.5 - 5.5
            
        for id in [3, 10, 11, 12, 13, 14, 16, 20, 21, 22, 23, 25, 26]:
            self.assertTrue(id in slices[5])
        
        for id in [1, 2, 4, 5, 7, 8, 9, 6, 15, 17, 18, 19, 24]:
            self.assertFalse(id in slices[5])
            
        self.assertTrue(len(slices[5].intersection(slices[6])) > 0)
            
        #3 - 6
            
        for id in [3, 10, 11, 12, 13, 14, 20, 21, 22, 25, 26]:
            self.assertTrue(id in slices[6])
        
        for id in [1, 2, 4, 5, 7, 8, 9, 6, 15, 16, 17, 18, 19, 23, 24]:
            self.assertFalse(id in slices[6])
            
        self.assertTrue(len(slices[6].intersection(slices[7])) > 0)
            
        #3.5 - 6.5
            
        for id in [3, 4, 10, 11, 12, 13, 14, 20, 21, 25, 26]:
            self.assertIn(id, slices[7])
        
        for id in [1, 2, 5, 7, 8, 9, 6, 15, 16, 17, 18, 19, 22, 23, 24]:
            self.assertFalse(id in slices[7])
            
        self.assertTrue(len(slices[7].intersection(slices[8])) > 0)
            
        #4 - 7
            
        for id in [4, 10, 11, 12, 13, 14, 18]:
            self.assertIn(id, slices[8])
        
        for id in [1, 2, 3, 5, 7, 8, 9, 6, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26]:
            self.assertFalse(id in slices[8])
            
        self.assertTrue(len(slices[8].intersection(slices[9])) > 0)
            
        #4.5 - 7.5
            
        for id in [4, 5, 6, 8, 11, 12, 13, 14, 18]:
            self.assertTrue(id in slices[9])
        
        for id in [1, 2, 3, 7, 9, 10, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26]:
            self.assertFalse(id in slices[9])
            
        self.assertTrue(len(slices[9].intersection(slices[10])) > 0)
            
        #5 - 8
            
        for id in [4, 5, 6, 7, 8, 9, 13, 14, 18]:
            self.assertTrue(id in slices[10])
        
        for id in [1, 2, 3, 10, 11, 12, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26]:
            self.assertFalse(id in slices[10])


    def run_test_sliced_mining_for_length(self, slice_length: float):
        root_node = self.event_database.mine_events_sliced(1, 2, 2.5, slice_length)
        #print_tree_sliced(root_node)
        
        sequence_ratios = {}
        counts = {}
        traverse_tree_sliced(root_node, sequence_ratios, counts)
        
        self.assertAlmostEqual(sequence_ratios["A -> B"], 1.88, 2)
        self.assertAlmostEqual(sequence_ratios["A -> C"], 2.08, 2)
        
        self.assertAlmostEqual(sequence_ratios["A -> C -> A"], 1.25, 2)
        self.assertAlmostEqual(sequence_ratios["A -> C -> B"], 1.09, 2)
        
        self.assertAlmostEqual(sequence_ratios["A -> C -> A -> B"], 2.50, 2)
        self.assertAlmostEqual(sequence_ratios["A -> C -> A -> C"], 1.67, 2)
        
        self.assertFalse("A -> A" in sequence_ratios)
        self.assertFalse("A -> C -> C" in sequence_ratios)
        self.assertFalse("A -> C -> A -> A" in sequence_ratios)


    def test_sliced_mining_length_4(self):
        self.run_test_sliced_mining_for_length(4)
        
        
    def test_sliced_mining_length_3(self):
        self.run_test_sliced_mining_for_length(3)
        
        
    def test_sliced_mining_length_5(self):
        self.run_test_sliced_mining_for_length(5)
        
        
    def test_sliced_mining_length_3_5(self):
        self.run_test_sliced_mining_for_length(3.5)
        
    
    def test_sliced_mining_length_4_7(self):
        self.run_test_sliced_mining_for_length(4.7)
        
        
    def test_sliced_mining_length_5_4(self):
        self.run_test_sliced_mining_for_length(5.4)
        
        
    def test_sliced_mining_length_2_error(self):
        self.assertRaises(Exception, self.event_database.mine_events_sliced, 1, 2, 2.5, 2)
    
    
    def test_event_database_creation_no_event_type(self):
        self.assertRaises(Exception, EventDatabase, self.sample_gdf.drop(columns=["EventType"]), [10], 10)


    def test_event_database_creation_no_time(self):
        self.assertRaises(Exception, EventDatabase, self.sample_gdf.drop(columns=["Time"]), [10], 10)
        
        
    def test_event_database_creation_no_id(self):
        self.assertRaises(Exception, EventDatabase, self.sample_gdf.drop(columns=["ID"]), [10], 10)
        
        
    def test_event_database_creation_bad_geometry(self):
        gdf = self.sample_gdf[:2].set_geometry([Polygon(((1, 1), (2, 2), (3, 3))), Polygon(((4, 4), (5, 5), (6, 6)))])
        self.assertRaises(Exception, EventDatabase, gdf, [10], 10)


if __name__ == '__main__':
    unittest.main()
