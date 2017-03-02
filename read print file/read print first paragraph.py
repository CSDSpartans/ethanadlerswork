# This reads the first few lines of the document

name_of_mydocument = 'mydocument.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

                                     #read the first few lines
line = file_input.readline()
line = file_input.readline()
line = file_input.readline()

                                     # This reads the first paragraph

                                     # \n - indicates blank line
while line != '\n':                  # while not a blank line
    print(line)                       
    line = file_input.readline()

file_input.close()
