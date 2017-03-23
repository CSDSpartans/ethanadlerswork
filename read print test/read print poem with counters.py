name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     



line = file_input.readline()
print("      ", line, end = '')
line = file_input.readline()
print("      ", line, end = '')
line = file_input.readline()


line_counter = 0
stanza_counter = 0
total_lines_in_file = 2

while line != '':                      
    total_lines_in_file += 1
    if line == '\n':
      stanza_counter += 1
      print ()
    else:
      line_counter += 1
      if line_counter < 10:
        print(line_counter, ")   ", line, end = '')
      else:
        print(line_counter, ")  ", line, end = '')
    
    line = file_input.readline()
    
  



print ()
print ()
print ("The total number of stanzas in this poem are: ",  stanza_counter, '.')
print ("The total number of lines are: ", total_lines_in_file, '.')

file_input.close()
