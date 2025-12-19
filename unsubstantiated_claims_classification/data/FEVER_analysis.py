import pandas as pd

df = pd.read_json("/home/lukeg/Documents/VS_code/fine_tuning/lxg406/unsubstantiated_claims_classification/data/climate_fever/climate-fever-dataset-r1.jsonl", lines=True)

exploded_df = df.explode("evidences", ignore_index=True)

evidences = pd.json_normalize(exploded_df["evidences"])

preprocessed_df = pd.concat([
    exploded_df[["claim_id", "claim"]].reset_index(drop=True),
    evidences[["evidence_id", "evidence_label", "evidence", "entropy"]]
], axis=1)

# Outputs a dataframe with columns: ['claim_id', 'claim', 'evidence_id', 'evidence_label', 'evidence', 'entropy']

label_counts = preprocessed_df["evidence_label"].value_counts()
num_records = len(preprocessed_df)

print("Count of all labels:")
print(label_counts)
print()
print("Total records")
print(num_records)