import sqlite3
import faker

fake = faker.Faker()

def create_table():
    global connection, cursor
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    sql = '''
    CREATE TABLE IF NOT EXISTS person(
    personid INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    address VARCHAR(2024) NOT NULL,
    job VARCHAR(128) NOT NULL,
    age INTEGER NOT NULL
    )
    '''
    cursor.execute(sql)

def insert_fake():
    for _ in range(10):
        name = fake.name().split()
        cursor.execute(f'INSERT INTO person(first_name, last_name, address, job, age) VALUES(?, ?, ?, ?, ?)', (name[0], name[1], fake.address(), fake.job(), fake.random_int(16, 80)))
    connection.commit()
    connection.close()

def update_something(id, parametr, new_one):
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    sql = f'''
    UPDATE person SET {parametr} = {new_one} WHERE personid = {id}
        '''
    cursor.execute(sql)
    connection.commit()
    connection.close()

def kill_person(id):
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    sql = f'''
    DELETE FROM person WHERE id = {id}
        '''
    cursor.execute(sql)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_table()
    #update_something(2, 'age', 21)
    #kill_person(2)
    insert_fake()