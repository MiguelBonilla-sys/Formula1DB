import requests
import pandas as pd
import numpy as np


class Formula1Extract:
    def __init__(self, csv_path: str):
        self.csv = csv_path

    def queries(self):
        data = pd.read_csv(self.data)
        return data

    def response(self, data):
        return data.head()
