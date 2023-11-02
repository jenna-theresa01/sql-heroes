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


def add_hero():
    name = input("Add your new hero name: ")
    about = input("Tell me about your hero: ")
    bio = input("Tell me about your hero's past: ")
    query = """
            INSERT INTO heroes (name, about_me, biography)
            VALUES (%s, %s, %s)
            """
    execute_modify(query, (name, about, bio,))

add_hero()
