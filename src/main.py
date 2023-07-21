from database.db_connection import execute_query

def menu():
    function_dict = {
        "create_hero": create_hero,
        "remove_hero": remove_hero,  # Dictionary for calling function based on user selection
        "show_hero": show_hero,
        "update_hero": update_hero,
    }
    prompt = input(
        "\n HELLO, WHAT WOULD YOU LIKE TO DO?\n"
        "1 = Create a new hero \n"
        "2 = Show all heroes \n"  # Input for main menu
        "3 = Update an existing hero \n"
        "4 = Remove a hero \n"
    )
    user_choice = int(prompt) - 1

    print(user_choice)

    if 0 <= user_choice <= 3:       # Defensive programming. making sure user choice is index of function dictionary (1-4)
        crud_functions = ["create_hero", "show_hero", "update_hero", "remove_hero"] #Setting a list to refer to to dictionary for menu options
        function_caller = function_dict[crud_functions[user_choice]]    #Setting variable to function dict index. refers to index of dict by index of functions list
        function_caller()       # Calls function by function dictionary value
    else:
        print("Choose a correct option dawg")
        menu()




# Function to create a Hero in the DB

def create_hero():

    name = input("Name your Hero ")
    about_me = input("Tell us about your Hero ")
    biography = input("Tell us your Heroes story ")
    query = """

    INSERT INTO heroes (name, about_me, biography)
    VALUES (%s, %s, %s);

    """

    execute_query(query, (name, about_me, biography))
    
    print(f"Succsessfuly Created Hero {name}!")

    menu()


# Function to Remove a Hero from the Database

def remove_hero():

    delete_name = input("Who would you like to remove? ")
    query = """

    DELETE FROM heroes
    WHERE %s = heroes.name;

    """

    execute_query(query, (delete_name,))

    print(f"Succsesfuly Removed Hero {delete_name}!")

    menu()

# Function to show the Heros

def show_hero():

    query = """

    SELECT * FROM heroes

    """

    hero_list = execute_query(query).fetchall() # Fetches the entire Heroes Table and saving it to a variable

    for hero in hero_list: # looping through the variable Printing the first index of each array which is the heros name
        print(hero[1])

    menu()

# Function to update a Hero

def update_hero():

    select_hero = input("Who Would You Like To Update? ")
    update_name = input("Update Hero name ")
    update_about_me = input("Change Hero info ")
    update_bio = input("Chage Hero backstory ")
    query = """

    UPDATE heroes

    SET name = %s,
    about_me = %s,
    biography = %s

    WHERE %s = heroes.name;

    """

    execute_query(query, (update_name, update_about_me, update_bio, select_hero))

    print(f"Succsessfuly Updated Hero!")

    menu()

menu()