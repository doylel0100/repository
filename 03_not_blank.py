#functions go here
def yes_no(question):

    while True:
        response = input(question)

        if response == "":\
            print("sorry this cant be blank. please try again")
        else:
            return response





# main routine goes here