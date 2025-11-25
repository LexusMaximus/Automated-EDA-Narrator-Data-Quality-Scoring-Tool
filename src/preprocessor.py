# Encapsulation + getters
# src/preprocessor.py
from dateutil import parser

class Preprocessor:
    def __init__(self, df):
        self._df = df.copy()          # protected

    def trim_strings(self, cols):
        for c in cols:
            if c in self._df:
                self._df[c] = self._df[c].astype(str).str.strip()
        return self

    def parse_dates(self, cols):
        for c in cols:
            if c in self._df:
                self._df[c] = self._df[c].apply(lambda x: parser.parse(x) if x and isinstance(x,str) else x)
        return self

    def get_df(self):
        return self._df
