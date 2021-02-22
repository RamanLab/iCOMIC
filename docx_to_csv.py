dataframe = pd.read_csv("BWA_MEM.csv", header=0) # specifying that the table has column names

essential = dataframe[dataframe["Essential"] == "yes"]

number_of_essential = len(essential) # returns number of essential parameters

label_array = []
line_edit_array = []

coords_dict = {1: <coord1>, 2: <coord2>, ... }

for i, j, k in zip(range(number_of_essentials), label_array, line_edit_array): 
    <coordinate for label 1> = coords_dict[i+1]
    j.setText(essentials.iloc(i, 2)) # label name to be taken from ith row and 3rd col of the table
    k.setText(essentials.iloc(i, 4))  # line_edit name to be taken from ith row and 5th col of the table