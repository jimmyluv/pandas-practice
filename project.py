import pandas as pd

# # Read the CSV file
data = pd.read_csv('users.csv')

# # Convert the data to a dictionary
my_dict = data.to_dict('dict')

print(my_dict)
print(type(data))
print(type(my_dict))