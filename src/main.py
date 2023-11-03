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
    name = input("Add your new hero name: ")
    about = input("Tell me about your hero: ")
    bio = input("Tell me about your hero's past: ")
    query = """
            INSERT INTO heroes (name, about_me, biography)
            VALUES (%s, %s, %s);
            """
    execute_modify(query, (name, about, bio,))

add_hero()

# Read


# Update
# add a conditional statement to ask if the user wants to update a hero
# if "no" or "n" the user should be able to skip this step
def update_hero():
    name = input("Change the name of your hero: ")
    about = input("Tell me about this new hero: ")
    bio = input("Where did this new hero come from: ")
    query = """
            UPDATE heroes
            SET name = (%s), about_me = (%s), biography = (%s)
            WHERE name = @name;
            """
    execute_modify(query, (name, about, bio))

update_hero()

# Delete
# add a conditional statement to ask if the user wants to delete a hero
# if "yes" or "y" the SINGLE hero is deleted
# if "no" or "n" the user will skip this step
def delete_hero():
    prompt = input("Are you sure you want to delete a hero? Y or N: ")
    if prompt is "Y":
        name = input("what hero are you wanting to delete: ")
    else: 
        
    query = """
            DELETE
            FROM heroes
            WHERE name = (%s);
            """
    execute_modify(query, (prompt, name))

delete_hero()
