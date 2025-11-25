# Base class + inheritance + polymorphism
import pandas as pd
import numpy as np

class EDAAnalyzer:
    def __init__(self, df):
        self._df = df                # protected
        self.results = {}

    def run_all(self):
        # Base method (polymorphism)
        return {"summary": self._df.describe().to_dict()}

class NumericAnalyzer(EDAAnalyzer):
    def run_all(self):
        num = self._df.select_dtypes(include=[np.number])
        self.results['summary'] = num.describe().to_dict()
        return self.results

class CategoricalAnalyzer(EDAAnalyzer):
    def run_all(self):
        cat = self._df.select_dtypes(include=['object'])
        self.results['summary'] = cat.describe(include='all').to_dict()
        return self.results
