from io import open

text_file = open("myfile.txt", "w") # Create and Opening

some_text = "Estupendo día para estudiar Python \n el miércoles"

text_file.write(some_text) # Manipulate

text_file.close() #Cierre