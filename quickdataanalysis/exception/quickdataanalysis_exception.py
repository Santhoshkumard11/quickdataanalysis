class QuickDataAnalysisException(exception):
    
    def __init__(self,dataframe_col,columns):
        self.columns_length = columns
        self.dataframe_col = dataframe_col

    def __str__(self):
        temp = self.columns_length - self.dataframe_col
        return f"{temp} columns more than the dataframe columns. Check the number of columns"
