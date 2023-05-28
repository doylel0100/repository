#frc code


#not blank funct
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("sorry this cant be blank. please try again")
        else:
            return response

#answer options (string checker)
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")
            continue

# check users enter a number more than zero, has a custom
# error message.  Uses 'type' to accommodate either
# an integer of float
def num_check(question, type):

    if type == int:
        error = "Please enter an integer that is more than zero"
    else:
        error = "Please enter a number is more than zero"

    while True:

        try:
            response = type(input(question))
            return response

        except ValueError:
            print(error)





#check valid options
yes_no_list = ["yes","no"]

# have you seen this program?
want_instructions = yes_no("have you seen this program before? ")


if want_instructions == "no":
    print("instructions go here")


product_name = not_blank('product name:')


item_amount = num_check('how many items will you be producing', int)


print ("please eneter variable costs below..."
       "enter 'xxx' as item name when done. \n")

while True:
    item_name = not_blank('item name')
    quantity = num_check('quantity')
    how_much = not_blank('how much? $')
    return







