from io import open
import pickle

name_list = ["Pedro", "Ana", "María", "Isabel"]

binary_file = open("name_list", "wb")

pickle.dump(name_list, binary_file)

binary_file.close()

del (binary_file)