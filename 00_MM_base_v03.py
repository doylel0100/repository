import pandas
import random
from datetime import date


# functions go here
def slow_instructions():
    print('''\n
_*_*_*_*_* instructions_*_*_*_*_*_
    
    
for each ticket,enter ...
- the persons name (cant be blank)
- age (between 12 and 120)
-payment method (cash / cradit)

when u have entered all users press 'xxx' to quit

the program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

th information will also be automatically written tp
a text file.

****************************''')


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("sorry this cant be blank. please try again")
        else:
            return response


# check user integer
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an intager ")


# calculator the ticket price based age
def calc_tickets_price(var_age):
    if 12 <= var_age <= 15:
        ticket_price = 7.50
        return ticket_price
    elif 16 <= var_age <= 64:
        ticket_price = 10
        return ticket_price
    else:
        ticket_price = 6.50
        return ticket_price


def string_checker(question, num_letters, valid_responses):
    error = "please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2
    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine goes here

# set max num tickets
MAX_TICKETS = 10
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

all_names = []
all_tickets_cost = []
all_surcharges = []

# ask user if they want to see the instructions
want_instructions = string_checker("do you want to read the instructions? ", 1,
                                   yes_no_list)

if want_instructions == "yes":
    print("instructions go here")

print()

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = not_blank("enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    age = num_check("age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young")
        continue
    else:
        print("old >:(")
        continue

    # calculate ticket cost
    ticket_cost = calc_tickets_price(age)
    print("age:{}, Ticket price: ${:.2f}".format(age, ticket_cost))

    tickets_sold += 1

    payment_method = string_checker("Choose a payment method (cash / credit)", 2,
                                    payment_list)

    if payment_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_cost * .05

    print()

    # Add ticket details to lists
    all_names.append(name)
    all_tickets_cost.append(ticket_cost)
    all_surcharges.append(surcharge)

# output number of tickets sold
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_tickets_cost,
    "Surcharge": all_surcharges}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('name')

# calc ticket total ticket price
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# profit calc
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose winner from and find total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

today = date.today()

day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = "\n____ Mini Movie Fundraiser Ticket data ({}/{}/{})----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# set index to name
mini_movie_frame.set_index("Name")
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

Ticket_cost_heading = "\n---- Tickets Cost / Profit -----"
total_ticket_sales = "total ticket sales: ${:.2f}".format(total)
total_profit = "total profit : ${:.2f}".format(profit)

sales_status = "\n*** all the tickets have been sold"

winner_heading = "\n---- raffel winnner-----"
winner_text = "the winner of the raffel is {}.  " \
              "they have own ${}. ie: their ticket is " \
              "free".format(winner_name, total_won)

# set up text strings...
ticket_cost_heading = "***** Ticket Costs ***** \n"

to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

for item in to_write:
    print(item)

write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

text_file.close()


