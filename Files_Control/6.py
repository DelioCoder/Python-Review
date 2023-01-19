from io import open

file_text = open("myfile.txt", "r+") # read and write

# print(file_text.readlines())

text_line = file_text.readlines() # return a list of the text file

text_line[1] = "Esta línea ha sido incluida o modificada desde el exterior \n"

file_text.seek(0)

file_text.writelines(text_line) # receives a list as a parameter

file_text.close()