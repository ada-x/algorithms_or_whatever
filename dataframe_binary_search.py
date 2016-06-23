'''
basic binary search, dataframe implementation. finds a feature from a specified column in a dataframe. formatted to search by "name", however could easily be adapted other types of data. takes 4 inputs: the <name> or search term, the dataframe <df>, the column of the search term <search_col>, and the column containing the feature being searched <feat_col>. dataframe should already be read in so it can be referenced. i've tried to keep the comments as brief yet explanatory as possible. [:
'''

import math


def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]


def find_feature(name, df, search_col, feat_col):

    # The length of the dataset
    length = len(df)

    search_col = int(search_col)
    feat_col = int(feat_col)

    # can totes omit this if not needed
    name = format_name(name)

    # starting upper bound
    upper_bound = length - 1

    # starting lower bound
    lower_bound = 0

    while upper_bound > lower_bound:
        
        # slice again, new index based on new bounds
        index = math.floor((upper_bound + lower_bound) / 2)

        # get next guess. formatting can be omitted
        guess = format_name(df[index][search_col])

        if name == guess:
            return df[index][feature_col]

        # If name comes before the guess
        elif name < guess:

            # upper search bound gets lowered before slicing again
            upper_bound = index - 1

        else:
            # if the name comes after guess
            # raise the lower bound
            lower_bound = index + 1

    # didn't find the feature, return -1
    return -1
    
