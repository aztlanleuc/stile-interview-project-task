'''
Devon McKenzie
Project Team Task
String recognition
'''

# get the required input from the user
filename = input("What is the file to be scanned (do not include the .txt extension)? ") # the file to be opened
search_type = input("Which search would you like to run ('simple' or 'full')? ").lower() # which function to run

# if the user wants a full search, get a list of the items to search for
if search_type == "full":
    types_input = input("What types of bread would you like to search for (separated by a comma and no space)? ")
    types = types_input.split(",") # splits the input string into a list

# open the file to be scanned
txt = open(filename + ".txt")

# seperate the file into workable lines
temp = txt.readline()
lines = temp.split(". ")

# SIMPLE VERSION. ONLY IDENTIFIES LINES CONTAINING "BREAD"
def find_bread(text):

    # identifying lines that have bread
    lines_cont = [] # this will store a list of the lines containing "bread"
    line_indexes = [] # stores the location of bread in each stored line (will be used to highlight the word)

    for i in text: # check each line in the file
        location = i.find("bread") # will return the index of the first letter of "bread" if contained, otherwise returns -1

        if location != -1: # check if "bread" was found
            lines_cont.append(i) # if it was, add the line to the list to be returned
            line_indexes.append(location) # append the location of "bread" in that line

    if len(lines_cont) != 0: # if the word bread was found
        print("\nThis text contains bread in these lines:")

        for j in range(0, len(lines_cont)): # for each line that "bread" was found in
            temp = lines_cont[j]

            # print the line but with "bread" capitalised
            print(temp[:line_indexes[j] - 1] + " " + temp[line_indexes[j]:line_indexes[j] + 5].upper() + " " + temp[line_indexes[j]+6:])

        print("\nBread was found in this text {} time(s)".format(len(lines_cont)))

    else: # if the word bread was not found
        print("There's no bread in this text :(")

# COMPLEX VERSION. IDENTIFIES ALL VARIETIES OF BREAD SPECIFIED BY THE USER
def find_all_bread(text):

    total_count = 0

    for t in types: # run the whole simple program, but for each type of bread

        lines_cont = [] # this will store a list of the lines containing the current variety
        line_indexes = [] # store the location of that variety in each line

        for i in text: # check each line in the file
            location = i.find(t) # returns the index of the first letter of the variety, if not present returns -1

            if location != -1: # check if the variety was found
                lines_cont.append(i) # if it was, add the line to the list to be returned
                line_indexes.append(location) # append the location of the variety in that line

        if len(lines_cont) != 0: # if the variety was found
            print("__________________________________________________") # spacer to make the output more readable
            print("This text contains {} in these lines:".format(t))

            for j in range(0, len(lines_cont)): # for each line bread was found in

                # get the line and the length of the current variety being checked
                temp = lines_cont[j]
                length = len(t)

                # print the line but with the variety capitalised
                print(temp[:line_indexes[j] - 1] + " " + temp[line_indexes[j]:line_indexes[j] + length].upper() + " " + temp[line_indexes[j] + length + 1:])

            print("\n{} was found in this text {} time(s)".format(t.capitalize(),len(lines_cont)))

            total_count += len(lines_cont)

        else: # if the variety was not found
            print("__________________________________________________")
            print("This text does not contain {} :(".format(t))

    print("__________________________________________________")
    print("Varieties of bread were found in this text a total of {} times".format(total_count))


# depending on search type requested by the user, run the two different functions
if search_type == "simple":
    find_bread(lines)
elif search_type == "full":
    find_all_bread(lines)
else: # in case they mistyped or otherwise didn't give a correct search string
    print("You did not give a correct search type :(")

# close the text file
txt.close()
