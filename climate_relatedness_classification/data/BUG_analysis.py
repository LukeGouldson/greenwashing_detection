import pandas as pd

df = pd.read_json("/home/lukeg/Documents/VS_code/fine_tuning/lxg406/climate_relatedness_classification/data/climateBUG/climateBUG-training-dataset.json")

label_counts_tr = df["label"].value_counts()
num_records_tr = len(df)

print("Training Dataset")
print("Count of all labels:")
print(label_counts_tr)
print()
print("Number of records:")
print(num_records_tr)
print()

df = pd.read_json("/home/lukeg/Documents/VS_code/fine_tuning/lxg406/climate_relatedness_classification/data/climateBUG/climateBUG-testing-dataset.json")
label_counts_te = df["label"].value_counts()
num_records_te = len(df)

print("Testing Dataset")
print("Count of all labels:")
print(label_counts_te)
print()
print("Number of records:")
print(num_records_te)
print()

print("Totals")
print("Count of labels:")
print(label_counts_tr + label_counts_te)
print()
print("Number of records:")
print(num_records_te + num_records_tr)
print()
