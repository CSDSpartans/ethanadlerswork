#   This reads and prints the whole document.
#           It prints a blank line after each line of the file

name_of_mydocument = 'mydocument.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

line = file_input.readline()
while line != '':                    # while not end of file
    print(line)                      # prints the line and a blank new line
    line = file_input.readline()
        
file_input.close()
