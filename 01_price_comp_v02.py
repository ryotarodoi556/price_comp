# Function to check if the user has entered 'yes' or 'no'
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no.")

# Function to ensure the user input is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print("Sorry, this can't be blank. Please try again.")

# Function to check if the user input is a valid integer
def num_check(question, low, high):
    error = f"Enter a number between {low} and {high}"
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response in (item[:num_letters], item):
                return item
        print(error)

# Main routine
yes_no_list = ["yes", "no"]

# List of sneakers and their prices
sneakers = {
    1: {"name": "Rick Owens Geobasket", "price": 900},
    2: {"name": "Maison Margiela Replica", "price": 800},
    3: {"name": "Balenciaga Triple S", "price": 950},
    4: {"name": "Crocs", "price": 50},
    5: {"name": "Vans Knu Skools", "price": 150},
    6: {"name": "Off-White Vulcanized", "price": 650},
    7: {"name": "Alexander McQueen Oversized", "price": 580},
    8: {"name": "Air Force 1", "price": 120},
    9: {"name": "Yeezy Boost 350", "price": 500},
    10: {"name": "Jordan 4", "price": 400},
}

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to see how to use this price comparison tool? (y/n): ", 1, yes_no_list)
if want_instructions == "yes":
    print("This is a price comparison tool for high-end sneakers available at the store. "
          "\nIt asks how much money you have and gives a list of products that fit the budget. "
          "\nThen it gives a list of sneakers that provide the most value for money.")
    print()

# Get the user's budget
budget = num_check("How much is your budget today?: ", 50, 1000)

# Find affordable sneakers
affordable_sneakers = {k: v for k, v in sneakers.items() if v['price'] <= budget}

# Display affordable sneakers
if affordable_sneakers:
    print("Affordable sneakers within your budget:")
    for key, sneaker in affordable_sneakers.items():
        print(f"{key}: {sneaker['name']} - ${sneaker['price']}")

    # Recommend Crocs as the best value for money if within budget
    if 4 in affordable_sneakers:
        print("\nRecommendation: Crocs offer the best value for money within your budget.")

    # User selection loop
    while True:
        try:
            selected_key = int(input("Select the number of the sneaker you want to choose: "))
            if selected_key in affordable_sneakers:
                selected_sneaker = affordable_sneakers[selected_key]
                print(f"You selected: {selected_sneaker['name']} for ${selected_sneaker['price']}")
                break  # Exit the loop
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
else:
    print("Sorry, no sneakers are available within your budget.")

print("\nThank you for using the sneaker price comparison tool! See you later.")
