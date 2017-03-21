
#           It does not prt a blank line after each line of the file

name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

line = file_input.readline()
print(line, end = '')
line = file_input.readline()

print(line, end = '') 
line = file_input.readline()
print(line)

line = file_input.readline()
line_counter = 0
stanza_counter = 1

while line != '':                      # while not end of file

    if line == '\n':
      stanza_counter += 1
      print ()
    else:
      line_counter += 1
      print(line_counter, ") ", line, end = '')              # don't print another new line
    line = file_input.readline()
    
print ()
print ()
print ("The number of stanzas is ",  stanza_counter)

file_input.close()
                         
                          #
                          #  Code Added to Write Poem
file_input = open(name_of_mydocument, 'r')

name_of_outputdocument = 'myoutputdocument.txt'
file_output = open(name_of_outputdocument, 'w')

whole_poem = file_input.read()
file_input.close()

file_output.write("This is a Copy of the Whole Poem\n\n")
file_output.write(whole_poem)
file_output.write("\n\n")
file_output.write("The number of stanzas is: ")
file_output.write(str(stanza_counter))
file_output.close()
