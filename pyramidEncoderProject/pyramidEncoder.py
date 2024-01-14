def decode(message_file):
    pyramid = []
    with open(message_file, 'r') as file:  # Replace "message_file" with the correct file path
        for line in file:
            number, word = line.split()
            pyramid.append((int(number), word))

    pyramid.sort()
    #print(pyramid) # Sort the pyramid list based on the numbers
    print_elements(pyramid) # Print the words in the pyramid
    
    
def print_elements(array):
    i = 0
    skipped = 0
    while i <= len(array):
        print(array[i])
        print(array[i][1], end="") 
        skipped += 1
        i += skipped + 1


    
decode("coding_qual_input.txt")


