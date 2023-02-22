import pandas as pd

# Read in the data


df = pd.read_csv('test_data.csv')
sample_route_data = df.to_dict('records')

aggregated_stop_sequences = {}
aggregated_day_types = {}

for row in sample_route_data:
    if row['day_type'] not in aggregated_day_types:
        aggregated_day_types[row['day_type']] = []
    aggregated_day_types[row['day_type']].append(row['day_type'])

    # if row['direction_id'] not in aggregated_stop_sequences:
    #     aggregated_stop_sequences[row['direction_id']] = []
    # aggregated_stop_sequences[row['direction_id']].append(row['stop_sequence'])

print(aggregated_day_types)
# sample_route_data['stop_sequence'].groupby(sample_route_data['direction_id'])
# stop_sequence_aggregated_df
# for row in sample_route_data:
#     new_dict = {}
#     this_df = pd.DataFrame(row, index=[0])
    