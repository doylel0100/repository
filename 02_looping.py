# main routine starts here

# set max num of tickets below
MAX_TICKETS = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("please enter name or 'xxx' to quit: ")

    tickets_sold += 1

    if name == 'xxx':
        break


# output number of tickets sold
if tickets_sold == MAX_TICKETS:
    peint("congratualations you have sold all the tickets")

