import pandas as pd
from datasets import Dataset, DatasetDict

pd.set_option('display.max_columns', None)


def climate_fever_to_claim_evidence_pairs(df):
    print("DF\n", df.head())

    exploded_df = df.explode("evidences", ignore_index=True)
    # df_exploded = df_exploded.drop(columns=["evidences"]).reset_index(drop=True)

    print("\nEXPLODED\n", exploded_df.head())
    print(f"\nColumns: {exploded_df.columns}")

    evidences = pd.json_normalize(exploded_df["evidences"])

    preprocessed_df = pd.concat([
        exploded_df[["claim_id", "claim"]].reset_index(drop=True),
        evidences[["evidence_id", "evidence_label", "evidence", "entropy"]]
    ], axis=1)

    print("\nPREPROCESSED\n", preprocessed_df.head())
    print(f"\nColumns: {preprocessed_df.columns}\n")
    print(preprocessed_df.loc[1])

    dataset = Dataset.from_pandas(preprocessed_df)
    return dataset



df = pd.read_json("/home/lukeg/Documents/VS_code/climate_project/lxg406/data/climate_fever/climate-fever-dataset-sample.jsonl", lines=True)
ds = climate_fever_to_claim_evidence_pairs(df=df)
print(ds[4])
print(ds[3])
print(ds[9])
print(ds[77])
