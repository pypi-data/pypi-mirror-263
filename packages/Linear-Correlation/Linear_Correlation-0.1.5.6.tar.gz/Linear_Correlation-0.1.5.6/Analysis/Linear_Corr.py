import pandas as pd
import numpy as np
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
        
        self.variance: float = np.var(self.data[attrib1]), np.var(self.data[attrib2]) if "variance" in args else ''
        self.covariance: float = self.data[attrib1].cov(self.data[attrib2]) if "covariance" in args else ''
        self.correlation: float = self.data[attrib1].corr(self.data[attrib2]) if "correlation" in args else ''
        return self
    
    def show_result(self) -> pd.DataFrame:
        result_dictionary: dict = {
            "Variance": [f"{self.variance[0]:.2f}", f"{self.variance[1]:.2f}"],
            "Covariance": [f"{self.covariance:.2f}", ''],
            "Correlation": [f"{self.correlation:.2f}", '']
        }
        
        res_df = pd.DataFrame(result_dictionary, self.attribs)
        res_df
        return res_df
    
    def show_plot(self, xLabel: str = ..., ylabel: str = ...) -> ...:
        # Scatter plot
        plt.scatter(self.data[self.attribs[0]], self.data[self.attribs[1]], color='blue', alpha=0.5)

        # Set labels and title
        plt.xlabel('Area')
        plt.ylabel('Major Axis Length')
        plt.title(f'Linear Correlation between {xLabel} and {ylabel}')
        # Show plot
        plt.grid(True)
        plt.show()
        return self.data[list(self.attribs)]