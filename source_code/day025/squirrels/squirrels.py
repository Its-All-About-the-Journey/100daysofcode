import pandas as pd

color_count = {
	'Fur Color': ['Gray', 'Cinnamon', 'Black'],
	'Count': [0, 0, 0]
}

squirrel_data = pd.read_csv('squirrel_data.csv')

for i, key in enumerate(color_count['Fur Color']):
	color_count['Count'][i] = len(squirrel_data[squirrel_data['Primary Fur Color'] == f'{key}'])

color_df = pd.DataFrame(color_count)
print(color_df)
color_df.to_csv('color_count.csv')


