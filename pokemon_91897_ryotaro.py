# Function to check if the user has entered 'yes' or 'no'
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("\nPlease enter yes or no.")


# Function to ensure the user input is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print("\nSorry, this can't be blank. Please try again.")


# Function to check if the user input is a valid integer
def num_check(question, low, high):
    error = f"\nEnter a number between {low} and {high}"
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
    error = f"\nPlease choose {valid_responses[0]} or {valid_responses[1]}"
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response in (item[:num_letters], item):
                return item
        print(error)


# Main routine
yes_no_list = ["yes", "no"]

# List of Pokémon cards and their prices
pokemon_cards = {
    1: {"name": "Charizard Holo", "price": 2000},
    2: {"name": "Pikachu Illustrator", "price": 800},
    3: {"name": "Mewtwo Shadowless", "price": 1300},
    4: {"name": "Bulbasaur Base Set", "price": 50},
    5: {"name": "Blastoise Holo", "price": 150},
    6: {"name": "Gyarados First Edition", "price": 300},
    7: {"name": "Lugia Neo Genesis", "price": 3000},
    8: {"name": "Snorlax Jungle Set", "price": 120},
    9: {"name": "Eevee Promo", "price": 500},
    10: {"name": "Jigglypuff First Edition", "price": 400},
}

# Ask user if they want to see the instructions
want_instructions = string_checker("\nDo you want to see how to use this price comparison tool? (y/n): ", 1,
                                   yes_no_list)
if want_instructions == "yes":
    print("\nThis is a price comparison tool for the rarest Pokémon cards available at the store.")
    print("It asks how much money you have and gives a list of products that fit the budget.")
    print("The budget must be above $50 and below $5000 to ensure that our store does not sell out.")
    print("Then it gives a list of cards that fit the user's budget and a recommendation card.\n")

# Get the user's budget
budget = num_check("\nHow much is your budget today?: ", 50, 5000)

# Loop until the budget is exhausted or below $50
while budget >= 50:
    # Find affordable Pokémon cards
    affordable_cards = {k: v for k, v in pokemon_cards.items() if v['price'] <= budget}

    # Display affordable cards
    if affordable_cards:
        print(f"\nYour remaining budget is: ${budget}")
        print("\nAffordable Pokémon cards within your budget:\n")
        for key, card in affordable_cards.items():
            print(f"{key}: {card['name']} - ${card['price']}")

        # Recommend Bulbasaur as the best value for money if within budget
        if 4 in affordable_cards:
            print("\nRecommendation: Bulbasaur Base Set offers the best value for money within your budget.\n")

        # User selection loop
        while True:
            try:
                selected_key = int(input("\nSelect the number of the Pokémon card you want to choose: "))
                if selected_key in affordable_cards:
                    selected_card = affordable_cards[selected_key]
                    print(f"\nYou selected: {selected_card['name']} for ${selected_card['price']}")

                    # Subtract the price from the user's budget
                    budget -= selected_card['price']

                    # Display how much money is left
                    print(f"\nYou have ${budget} left to spend.")

                    # If the remaining budget is below $50, end the loop
                    if budget < 50:
                        print("\nYou have less than $50 remaining. No further purchases can be made.")
                        budget = 0  # Exit the loop
                        break

                    # Check if the user wants to buy another card
                    another_purchase = yes_no("\nDo you want to buy another card? (yes/no): ")
                    if another_purchase == "no":
                        budget = 0  # Exit the loop by setting the budget to 0
                        break
                    else:
                        # Continue to next iteration to show the menu again
                        break
                else:
                    print("\nInvalid selection. Please try again.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
    else:
        print("\nSorry, no Pokémon cards are available within your remaining budget.")
        break

print("\nThank you for using the Pokémon card price comparison tool! See you later.\n")