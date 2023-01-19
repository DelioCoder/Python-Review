from io import open

file_text = open("myfile.txt", "r")

text_lines = file_text.readlines();

file_text.close()

print(text_lines[0])