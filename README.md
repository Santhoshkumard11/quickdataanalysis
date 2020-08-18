# quick data analysis

[![PyPi](https://img.shields.io/badge/pypi%20package-0.0.1-blue)](https://pypi.org/project/quickdataanalysis/)
[![](https://img.shields.io/github/license/Santhoshkumard11/quickdataanalysis.svg?colorB=00fff0)](https://github.com/Santhoshkumard11/quickdataanalysis/blob/master/LICENSE.md)
[![Release](https://img.shields.io/badge/Next%20Release-Oct%2020-green)](https://pypi.org/project/quickdataanalysis/)
![Issues](https://img.shields.io/github/issues/Santhoshkumard11/quickdataanalysis)

This packages allows you to kick start your data analysis and make faster insights of the data.

# Requirements
* Pandas >=1.0.1

## Documentation

## 1) Creating Dummies for columns

The create_dummies method will return dummies for the columns. For example you want to dummies for Gender column put the column name in a list and you will get the dataframe with the dummies.

       >>> df =  create_dummies(df_train,["sex"])
       >>> df
       male female
       0      1
       1      0
       1      0
       1      0

## 2) Counting the column values

The count_values method will return the number of values in the columns. For example you want to count the number of females.

    >>> count_values(df_train["female"],1,False)
      312

## ToDo

 - [ ] Add more method



All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome :)

Happy Coding!!
