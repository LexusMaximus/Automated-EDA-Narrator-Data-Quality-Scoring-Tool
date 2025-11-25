# EDAAnalyzer
# src/eda_analyzer.py
import pandas as pd
import numpy as np
from scipy import stats
from typing import Dict, Any

class EDAAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.results = {}

    def summary_stats(self, numeric_only=True) -> Dict[str, Any]:
        if numeric_only:
            stats_df = self.df.select_dtypes(include=[np.number]).describe().to_dict()
        else:
            stats_df = self.df.describe(include='all').to_dict()
        self.results['summary'] = stats_df
        return stats_df

    def missing_summary(self):
        missing = self.df.isnull().sum().to_dict()
        pct = (self.df.isnull().mean()*100).round(2).to_dict()
        out = {col: {"missing": int(missing[col]), "pct": float(pct[col])} for col in self.df.columns}
        self.results['missing'] = out
        return out

    def duplicate_count(self):
        count = int(self.df.duplicated().sum())
        self.results['duplicates'] = count
        return count

    def outlier_counts(self, method='iqr'):
        outliers = {}
        num = self.df.select_dtypes(include=[np.number]).columns
        for c in num:
            series = self.df[c].dropna()
            if method == 'zscore' and len(series) > 1:
                zs = np.abs(stats.zscore(series))
                outliers[c] = int((zs > 3).sum())
            else:  # IQR
                q1 = series.quantile(0.25)
                q3 = series.quantile(0.75)
                iqr = q3 - q1
                lower = q1 - 1.5 * iqr
                upper = q3 + 1.5 * iqr
                outliers[c] = int(((series < lower) | (series > upper)).sum())
        self.results['outliers'] = outliers
        return outliers

    def categorical_balance(self, column, top_n=5):
        if column not in self.df:
            return {}
        vc = self.df[column].value_counts(dropna=False).head(top_n)
        return vc.to_dict()

    def correlation_matrix(self):
        num = self.df.select_dtypes(include=[np.number])
        if num.shape[1] < 2:
            return {}
        corr = num.corr().round(3).to_dict()
        self.results['correlation'] = corr
        return corr

    def run_all(self):
        self.summary_stats()
        self.missing_summary()
        self.duplicate_count()
        self.outlier_counts()
        self.correlation_matrix()
        return self.results
