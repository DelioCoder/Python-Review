from io import open

file_text = open("myfile.txt", "r")

text = file_text.read()

file_text.close()

print(text)