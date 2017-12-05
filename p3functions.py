def make_indicators(df, names):
    """Make indicator columns in dataframe df of whether existing columns are 
    equal to given values.

    Args:
        df (pandas.DataFrame): Dataframe to be modified.
        names (dict)         : Dictionary containing:
                                 - Keys: Desired indicator column names
                                 - Values: Two item tuple containing:
                                     - Original dataframe column
                                     - Value to compare to column

    Returns:
        void: Dataframe df is modified in place.
    """
    for k,v in names.items():
        df[k] = 1*(df[v[0]] == v[1])
