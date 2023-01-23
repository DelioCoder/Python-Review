from io import open
import pickle

file = open("name_list", "rb")

list_names_py = pickle.load(file)

print(list_names_py)