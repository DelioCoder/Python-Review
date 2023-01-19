from io import open

file_text = open("myfile.txt", "a")

file_text.write("\n siempre es una buena ocasión para estudiar Python")

file_text.close()