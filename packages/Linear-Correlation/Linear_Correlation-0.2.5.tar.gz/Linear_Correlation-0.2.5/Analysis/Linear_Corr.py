import pandas as pd
import numpy as np
from typing import Any
import matplotlib.pyplot as plt

class DataProcess:
    def __init__(self) -> None:
        self.data: pd.DataFrame = ...
        self.attribs: str = ...
        
        self.variance: float = ...
        self.covariance: float = ...
        self.correlation: float = ...
        
    def set_attribs(self, data: pd.DataFrame, attribs: tuple = ...) -> ...:
        self.data = data
        self.attribs = attribs
        return self

    def calculate(self, args: tuple = ...) -> ...:
        (
            attrib1,
            attrib2
        ) = self.attribs
        
        self.variance: Any = np.var(self.data[attrib1]), np.var(self.data[attrib2]) if "variance" in args else ...
        self.covariance: Any = self.data[attrib1].cov(self.data[attrib2]) if "covariance" in args else ...
        self.correlation: Any = self.data[attrib1].corr(self.data[attrib2]) if "correlation" in args else ...
        return self
    
    def show_result(self) -> pd.DataFrame:
        result_dictionary: dict = {
            "Variance": [
                    f"{self.variance[0]:.2f}"
                    if self.variance[0] != ... else '',
                    
                    f"{self.variance[1]:.2f}"
                    if self.variance[1] != ... else ''
                ],
            "Covariance": [
                    f"{self.covariance:.2f}"
                    if self.covariance != ... else '',
                    
                    ''
                ],
            "Correlation": [
                f"{self.correlation:.2f}"
                if self.correlation != ... else '',
                
                ''
            ]
        }
        
        res_df = pd.DataFrame(result_dictionary, self.attribs)
        res_df
        return res_df
    
    def show_plot(self, xLabel: str = ..., ylabel: str = ..., return_data: bool = False) -> ...:
        # Scatter plot
        plt.scatter(self.data[self.attribs[0]], self.data[self.attribs[1]], color='blue', alpha=0.5)

        # Set labels and title
        plt.xlabel(xLabel)
        plt.ylabel(ylabel)
        plt.title(f'Linear Correlation between {xLabel} and {ylabel}')
        # Show plot
        plt.grid(True)
        plt.show()
        if return_data: 
            return self.data[list(self.attribs)]