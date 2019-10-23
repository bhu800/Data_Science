import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import  preprocessing


def read_data(path_to_file):
    """ Returns Pandas dataframe for given csv file

        Parameters
        ----------
        path_to_file: string
            Given csv file

        Returns
        -------
        pandas.Dataframe
    """
    df = pd.read_csv(path_to_file)
    return df
    pass


def show_box_plot(attribute_name, dataframe):
    """ Displays boxplot for atrribute

        Parameters
        ----------
        attribute_name: string
            Attribute selected
        dataframe: pandas.Dataframe
            DataFrame for the given dataset
        Returns
        -------
        None
    """
    # dataframe.boxplot(column=[attribute_name])
    plt.boxplot(dataframe[attribute_name])
    plt.show()


def replace_outliers(dataframe):
    """ Replaces the outliers in the given dataframe

        Parameters
        ----------
        dataframe: pandas.Dataframe
            DataFrame for the given dataset
        Returns
        -------
        pandas.Dataframe
    """
    dataframe2 = dataframe.copy()
    for i in dataframe2.columns:
        col = dataframe2[i]
        median = col.median()
        Q1 = col.quantile(.25)
        Q3 = col.quantile(.75)
        IQR = Q3 - Q1
        dataframe2.loc[(col<(Q1-1.5*IQR)) | (col>(Q3+1.5*IQR)), i] = median
    return dataframe2
    pass


def range(dataframe, attribute_name):
    """ Gives Range of Selected Attribute

        Parameters
        ----------
        attribute_name: string
            Attribute selected
        dataframe: pandas.Dataframe
            DataFrame for the given dataset
        Returns
        -------
        pair(float,float)
    """
    min = dataframe[attribute_name].min()
    max = dataframe[attribute_name].max()
    return (min, max)
    pass


def min_max_normalization(dataframe, range=None):
    """ Returns normalized pandas dataframe

        Parameters
        ----------
        dataframe: pandas.Dataframe
            Dataframe for the given dataset
        range: pair(float,float)
            Normalize between range
        Returns
        -------
        pandas.Dataframe
    """
    dataframe_to_normalize = dataframe.copy()
    dataframe_normalized = (dataframe_to_normalize-dataframe_to_normalize.min())/(dataframe_to_normalize.max()-dataframe_to_normalize.min())
    if range != None:
        offset = range[0]
        scaling_factor = range[1]-range[0]
        dataframe_normalized = offset + dataframe_normalized*scaling_factor
    return dataframe_normalized
    pass


def standardize(dataframe):
    """ Returns standardized pandas dataframe

        Parameters
        ----------
        dataframe: pandas.Dataframe
            Dataframe for the given dataset
        Returns
        -------
        pandas.Dataframe
    """
    dataframe_to_standardize = dataframe.copy()
    dataframe_standardize = (dataframe_to_standardize-dataframe_to_standardize.mean())/dataframe_to_standardize.std()
    return dataframe_standardize
    pass


def main():
    """ Main Function
        Parameters
        ----------

        Returns
        -------
        None
    """
    path_to_file = "landslide_data2_original.csv"
    dataframe = read_data(path_to_file).iloc[:, 2:]
    # dataframe2 = pd.DataFrame(dataframe)
    # print("*****", dataframe['fixed_acidity'].median(), dataframe['fixed_acidity'].quantile(.25), dataframe['fixed_acidity'].quantile(.75))
    # show_box_plot('fixed_acidity', dataframe)

    # outlier correction
    dataframe_corrected = replace_outliers(dataframe)
    # print("*****", dataframe['fixed_acidity'].median(), dataframe['fixed_acidity'].quantile(.25), dataframe['fixed_acidity'].quantile(.75))
    # show_box_plot('fixed_acidity', dataframe_corrected)

    # plotting box plots with and without outlier correction
    for i in dataframe.columns:
        plt.boxplot([dataframe[i], dataframe_corrected[i]])
        plt.title(i)
        plt.show()

    for i in dataframe_corrected.columns:
        Range = range(dataframe, i)
        print("Range of {} : {}".format(i, Range))

    print("***** min_max_normalization : range(0, 1) *****")
    print(min_max_normalization(dataframe_corrected))
    print("***** min_max_normalization : range(0, 20) *****")
    print(min_max_normalization(dataframe_corrected, range=(0, 20)))
    print(min_max_normalization(dataframe_corrected, range=(0, 20)).max())
    print("***** standardization *****")
    print("###BEFORE###", dataframe_corrected.mean(), dataframe_corrected.std())
    print(standardize(dataframe_corrected))
    print("###AFTER###", standardize(dataframe_corrected).mean(), standardize(dataframe_corrected).std())

    x = dataframe.values
    StandardScaler = preprocessing.StandardScaler()
    x_scaled1 = StandardScaler.fit_transform(x)
    df_scaled1 = pd.DataFrame(x_scaled1)
    print(df_scaled1)

    MinMaxScaler = preprocessing.MinMaxScaler()
    x_scaled2 = MinMaxScaler.fit_transform(x)
    df_scaled2 = pd.DataFrame(x_scaled2)
    print(df_scaled2)



if __name__ == "__main__":
    main()