import sqlite3
import math


def create_planets (db, data_file):
    """ (str, file open for reading) -> NoneType
    Create and insert the Planets table in database with name db with
    the data from the open file data_file.
    """

    # Connect to the database
    con = sqlite3.connect(db)

    # Create a cursor
    cur = con.cursor()

    # Create the Planets table
    cur.execute('''CREATE TABLE Planets(name TEXT, mass TEXT, radius TEXT, escape_vel TEXT)''')

    # Split data to store into table
    for line in data_file:
        data = line.split(',')
        name = data[0].strip()
        mass = data[1].strip()
        radius = data[2].strip()
        escape_vel = calculate_escape_velocity(mass, radius)

        cur.execute('''INSERT INTO Planets VALUES (?, ?, ?, ?)''', (name, mass, radius, escape_vel))

    # Close the cursor
    cur.close()

    # Commit changes
    con.commit()

    # Close the connection
    con.close()


def calculate_escape_velocity(mass, radius):

    GRAV_CONSTANT = 6.67e-11
    return math.sqrt((2 * GRAV_CONSTANT * float(mass)) / float(radius))


def run_query(db, query, args=None):
    ''' (str, str, str) -> list of tuple
    Return the results of running query q on database db.
    If given, args contains the query arguments.
    '''

    con = sqlite3.connect(db)
    cur = con.cursor()

    if args is None:
        cur.execute(query)
    else:
        cur.execute(query, args)

    # Get results, if any
    data = cur.fetchall()

    con.commit()
    cur.close()
    con.close()

    return data


def get_info_by_name(db, name):
    ''' (str, str) -> list of tuple '''

    query = 'SELECT name, mass, radius, escape_vel FROM Planets WHERE name = ?'
    return run_query(db, query, args = (name,))


def get_all_escape_vel(db):
    ''' (str) -> list of tuple '''

    query = 'SELECT name, escape_vel FROM Planets'
    return run_query(db, query)


if __name__ == '__main__':
    
    my_db = 'planets.db'
    
    # Set to True the first run time to create database, then revert to False
    create_table = False
    
    # Open data files
    if create_table:
        planets_file = open('planets.txt')

        # Read info into table
        create_planets(my_db, planets_file)

        # Close data files
        planets_file.close()
        
    