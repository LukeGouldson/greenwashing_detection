import pandas as pd
from datasets import Dataset, DatasetDict

pd.set_option('display.max_columns', None)


# This function explodes the evidences section of climate-fever such that we produce 5 claim-evidence pairs for each claim
# The dataset therefore becomes x5 bigger
def climate_fever_to_claim_evidence_pairs(df):

    exploded_df = df.explode("evidences", ignore_index=True)

    evidences = pd.json_normalize(exploded_df["evidences"])

    preprocessed_df = pd.concat([
        exploded_df[["claim_id", "claim"]].reset_index(drop=True),
        evidences[["evidence_id", "evidence_label", "evidence", "entropy"]]
    ], axis=1)

    # Outputs a dataframe with columns: ['claim_id', 'claim', 'evidence_id', 'evidence_label', 'evidence', 'entropy']
    return preprocessed_df

# df = pd.read_json("/home/lukeg/Documents/VS_code/climate_project/lxg406/data/climate_fever/climate-fever-dataset-sample.jsonl", lines=True)
# ds = climate_fever_to_claim_evidence_pairs(df=df)
