import pandas as pd


def create_dummies(df,columns):
    '''
        Returns dummies of the columns

        Parameters
        ----------
        data : DataFrame
            The pandas object holding the data.
        column : List of columns
            If passed, will be used to limit data to a subset of columns.

        Return
        ------
        df : pandas.dataframe
            dataframe with dummies of the columns

    '''

    #catch the exception
    if len(columns) > len(df.columns) :
        raise QuickdataAnalysis(df, columns)

    dummies = []
    for col in columns:
        dummies.append(pd.get_dummies(df[col]))
    dataframe_dummies = pd.concat(dummies,axis=1)

    df = pd.concat((df,dataframe_dummies),axis=1)
    
    df = df.drop(columns,axis=1)
    
    return df


def column_value_count(df_col,value,bool_type=True):
    
    '''
        Returns the count of value

        Parameters
        ----------
        df_col : DataFrame.column
            The pandas object holding the data.
        value : int (or) str
            value to be counted
        bool_type : bool
            type of value to count

        Return
        ------
        result : int 
            number of values

    '''

    total = (df_col == value)
    
    result = dict(total.value_counts()).get(bool_type)
    
    return result
