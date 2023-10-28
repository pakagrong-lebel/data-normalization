# Python script for data normalization
import pandas as pd
def normalize_data(data_frame):
    normalize_data = (data_frame - data_frame.min()) / (data_frame.max() - data_frame.min())
    return normalize_data
                                                        