# Obtain user input for file name
def file_name_input():
    file_name = input("Enter a file name > ")
    fileNotFound = True  # get inside loop at least once
    while (fileNotFound):
        try:
            movie_file = open(file_name, "r")
            fileNotFound = False  # do not get back in loop
            # read from file
        except FileNotFoundError:  # ask for file name again
            file_name = input("Enter a file name >")
    return file_name

# Find max profit of movies
def max(file_name):
    movie_file = open(file_name, "r")
    print(movie_file)
    max_profit = 0
    max_profit_title = ""
    for line in movie_file:
        print(line)
        release_date, title, budget, boxoffice_gross = line.split(",")
        boxoffice_gross = float(boxoffice_gross)
        budget = float(budget)
        profit = boxoffice_gross - budget
        if profit > max_profit:
            max_profit = profit
            max_profit_title = title
    return max_profit_title, max_profit

# Writes release date, name, and profit to file named by user
def info_file(file_name):
    movie_file = open(file_name, "r")
    movie_info_file = input("Enter a file name to save movie information to ")
    new_file = open(movie_info_file, "w")
    for line in movie_file:
        release_date, title, budget, boxoffice_gross = line.split(",")
        boxoffice_gross = float(boxoffice_gross)
        #print("gross =", boxoffice_gross)
        budget = float(budget)
        #print("Budget =", budget)
        profit = boxoffice_gross - budget
        #print("profit =", profit)
        print(release_date, title, profit, file = new_file)

#Main File
def main():
    movie_file_input = file_name_input()
    max_profit = max(movie_file_input)
    print("The movie with the highest profit is ", max_profit)
    movie_info_file = info_file(movie_file_input)

main()