# This program DID work fine, but it's been modified.
# There are 3 different things you'll need to fix here.
# Concentrate on fixing data flow in and out of the function *first.*
# Then worry about getting the output and file to be correct.


# Make a box of other characters surrounding the input text
# By default use the asterisk
def box_me(input_text, box_char = '*'):
    box_length = len(input_text) + 2 # space characters and draw character on each end
    # stack up the output
    box_char_line = box_char * box_length + "\n"
    output = box_char_line
    output += box_char + " " + input_text + " " + box_char + "\n"
    output += box_char_line

    return output

if __name__ == "__main__":
    user_input = "Hello world" # I'm not going to mess with user input here, but by making
                               # this a variable and using it everywhere it's needed,
    boxed_text = box_me(user_input) # this program is ready for user input
    print(boxed_text)

    if input("Output to file? (y/n) > ").lower() == 'y':
        with open('boxmein.txt', 'w') as output_file:
            output_file.write(boxed_text)
            print("A copy of your output is in boxmein.txt")