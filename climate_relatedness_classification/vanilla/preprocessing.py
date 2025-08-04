import pandas as pd
from datasets import Dataset, DatasetDict

pd.set_option("display.max_columns", None)

# This function simply takes the climateBUG dataset and drops the year and manual columns.
# No further preprocessing is required
def climateBUG_drop_columns(df):

    preprocessed_df = df.drop(["year", "manual"], axis="columns")

    print(preprocessed_df)

    return preprocessed_df

# df = pd.read_json("/home/lukeg/Documents/VS_code/fine_tuning/lxg406/climate_relatedness_classification/data/climateBUG/climateBUG-training-dataset.json")
# ds = climateBUG_to_reduced_climateBUG(df=df)

def climateBUG_reduce_rows(df, rows: int):

    preprocessed_df = df.head(rows)

    preprocessed_df = climateBUG_drop_columns(preprocessed_df)

    print(preprocessed_df)

    return preprocessed_df
