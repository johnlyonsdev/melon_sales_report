
def count_melons():
    print("*" * 80) # Prints the line of asterisks
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0} # Creates a tuple to tally the melon types
    file = open("orders-by-type.txt") # Opens the order text file
    
    for line in file: # Iterates over each line in the file
        data = line.split("|") # Splits the file on each dividing character
        melon_type = data[1] # Selects the melon type based on it's location in the file
        melon_count = int(data[2]) # Selects the count of each order and converts it to an int
        melon_tallies[melon_type] += melon_count # Adds the count to the proper melon type in the melon tallies tuple

    file.close()
    melon_revenue(melon_tallies) # Calls the melon_revenue function

def melon_revenue(tuple):
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 } # Creates a tuple with the prices of each type of melon
    total_revenue = 0 # Creates a variable to count the revenue

    for melon_type in tuple: # Iterates through each melon type in the melon tallies tuple
        price = melon_prices[melon_type] # Picks the price for the melon type from the melon_prices tuple 
        revenue = price * tuple[melon_type] # Multiplies the price by the count of the melon type to establish the revenue
        total_revenue += revenue # Adds the revenue for this type of melon to the total revenue
        print(f"We sold {tuple[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}") # Prints the data for this type of melon


def sales_stats():
    print("*" * 42) # Prints the line of asterisks
    sales = [0, 0] # Creates the empty array we are going to store the sales stats in
    file = open("orders-with-sales.txt") # Opens the file showing the orders and sales

    for line in file: # Iterates through each line in the file
        data = line.split("|") # Splits each line based on the dividing character
        if data[1] == "0": # Depending on if the sales ID is 0, we will go to the section of the if loop that refers to the sales person or the section that refers to the computer
            sales[0] += float(data[3]) # Adds the revenue from the sale to the computer's stats
        else:
            sales[1] += float(data[3]) # Adds the revenue from the sale to the sales team's stats
    produce_report(sales) # Calls the produce_report function

def produce_report(arr):
    print(f"Salespeople generated ${arr[1]:.2f} in revenue.") # Print the stats for the sales team
    print(f"Internet sales generated ${arr[0]:.2f} in revenue.") # Print the stats for the computer
    if arr[1] > arr[0]: # If statement that checks if the sales team of the computer has sold more
        print("Guess there's some value to those salespeople after all.") # Draws a conclusion if the sales team has sold more
    else:
        print("Time to fire the sales team! Online sales rule all!") # Draws a conclusion if the computer has sold more
    print("*" * 42) # Prints the line of asterisks

count_melons() # Calls the count_melons function
sales_stats() # Calls the sales_stats function
