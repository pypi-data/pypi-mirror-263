import pandas as pd

from tk_core.common.files import read_json

# Load the data
data = read_json("examples/serp_api/example_batch_serp_results.json")

# dataframe
df = pd.DataFrame.from_dict(data)
df1 = pd.json_normalize(data)
