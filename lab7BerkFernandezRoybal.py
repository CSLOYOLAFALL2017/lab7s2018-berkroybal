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

def max(file_name):
    file_name = file_name_input()
    movie_file = open(file_name, "r")
    max_profit = 0
    for line in file_name:
        movie_info = "release_date, title, budget, boxoffice_gross"
        release_date, title, budget, boxoffice_gross = movie_info.split(",")
        profit = boxoffice_gross - budget
        if profit > max_profit:
            max_profit = profit
    return max_profit