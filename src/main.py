from database.db_connection import execute_query, execute_modify

def select_all_heroes():
    query = """
        SELECT * from heroes
    """
    returned_items = execute_query(query)
    for item in returned_items:
        print(item[1])
    return returned_items

select_all_heroes()

# Create
# add a conditional to ask if the user wants to add a new hero
# if the answer is "no" or "n" then the user should be able to skip this step 
def add_hero():
    prompt = input("Do you want to add a new hero? Y or N: ")
    if prompt.upper() == "Y":
        name = input("Add your new hero name: ")
        about = input("Tell me about your hero: ")
        bio = input("Tell me about your hero's past: ")
        query = """
                INSERT INTO heroes (name, about_me, biography)
                VALUES (%s, %s, %s);
                """
        execute_modify(query, (name, about, bio,))
    elif prompt.upper() == "N":
        print("Add new hero skipped.")
    else: 
        print("Invalid entry. Please enter Y or N")

add_hero()

# Read


# Update
# add a conditional statement to ask if the user wants to update a hero
# if "no" or "n" the user should be able to skip this step
def update_hero():
    prompt = input("Do you want to update a hero? Y or N: ")
    if prompt.upper() == "Y":
        old_hero = input("Enter current hero name: ")
        new_hero = input("What is the name of your new hero: ")
        query = """
                UPDATE heroes
                SET name = (%s)
                WHERE name = (%s);
                """
        execute_modify(query, (old_hero, new_hero))
        print(old_hero, " changed to ", new_hero)
    elif prompt.upper() == "N":
        print("Skipped update")
    else: 
        print("invalid input. PLease enter Y or N")

update_hero()

# Delete
# add a conditional statement to ask if the user wants to delete a hero
# if "yes" or "y" the SINGLE hero is deleted
# if "no" or "n" the user will skip this step
def delete_hero():
    prompt = input("Are you sure you want to delete a hero? Y or N: ")
    if prompt.upper() == "Y":
        name = input("what hero are you wanting to delete: ")
        query = """
            DELETE
            FROM heroes
            WHERE name = (%s);
            """
        execute_modify(query, (name,))
    elif prompt.upper() == "N":
        print("Hero deleted")
    else:
        print("Invalid input. Please print Y or N")

delete_hero()
