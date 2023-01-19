# Text pointer with external files

from io import open

file_text = open("myfile.txt", "r")

# file_text.seek(11) # Position of pointer

# print(file_text.read(11)) # read since the start of the pointer

# file_text.seek(len(file_text.read())/2)

# print(file_text.read())

file_text.seek(len(file_text.readline())) # Cursor located on the last line from the first paragraph

print(file_text.read())