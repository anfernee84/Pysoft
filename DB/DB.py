import psycopg2
from psycopg2 import Error,DatabaseError, connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_db(dbname):
    try:
        connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",)

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        create_database = f"CREATE DATABASE {dbname}"
        cursor.execute(create_database)
        print (f"Created database: '{dbname}'",'\n')
    except (Exception, Error) as error:
        print ("Error" ,error,'\n')
    finally:
        cursor.close()
        connection.close()
        print("connection closed",'\n')

def create_table(query, db):
    try:
        connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",
            database = db)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(f"Successfully created table '{query.split()[2]}' at database '{db}'", "\n")
    
    except (Exception, Error) as error:
        print ("Error", error)
    finally:
        cursor.close()
        connection.close()
        print("connection closed", "\n")

def insert_to_db(query,db):
    try:
        connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",
            database = db)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(f"Data sucessfully inserted in table '{query.split()[2]}' at database '{db}'", "\n")
    
    except (Exception, Error) as error:
        print ("Error", error)
    finally:
        cursor.close()
        connection.close()
        print("connection closed", "\n")   
  

if __name__ == "__main__":
    create_db("university")

    create_table('''CREATE TABLE students (
	                STUDENT_ID SERIAL PRIMARY KEY,
	                STUDENT_NAME VARCHAR(100) NOT NULL,
                    GROUP_ID INT NOT NULL
	                ) ''', "university")

    
    create_table('''CREATE TABLE groups (
	                GROUP_ID SERIAL PRIMARY KEY,
	                GROUP_NAME VARCHAR(100) NOT NULL
                    ) ''', "university")


    create_table('''CREATE TABLE GRADES (
                    GRADE_ID SERIAL  PRIMARY KEY,
                    GRADE_DATE DATE NOT NULL,
                    GRADE INT NOT NULL,
                    COURSE_ID  INT NOT NULL,
                    STUDENT_ID  INT) ''', "university")

    create_table('''CREATE TABLE TUTORS (
                    TUTOR_ID INT NOT NULL PRIMARY KEY,
                    TUTOR_NAME VARCHAR(100) NOT NULL,
                    GROUP_ID INT NOT NULL
                    ) ''', "university")


    create_table('''CREATE TABLE COURSES (
                    COURSES_ID INT NOT NULL PRIMARY KEY,
                    COURSES_NAME VARCHAR(100) NOT NULL,
                    TUTOR_ID INT NOT NULL ) ''', "university")


    insert_to_db('''INSERT INTO courses (courses_id,courses_name,tutor_id)values (1, 'Phycology', 2);
                    INSERT INTO courses (courses_id,courses_name,tutor_id)values (2, 'Biology', 1);
                    INSERT INTO courses (courses_id,courses_name,tutor_id)values (3, 'Drinkology', 3);
                    INSERT INTO courses (courses_id,courses_name,tutor_id)values (4, 'Programming', 1);
                    INSERT INTO courses (courses_id,courses_name,tutor_id)values (5, 'History', 2);                   
                    ''', "university")

    insert_to_db('''INSERT INTO tutors (tutor_id,tutor_name,group_id) values (1, 'Valeriy Albertovich',3);
                    INSERT INTO tutors (tutor_id,tutor_name,group_id) values (2, 'Onufriy Nikiforovich',2);
                    INSERT INTO tutors (tutor_id,tutor_name,group_id) values (3, 'Aristarkh Bastardovich',1);
                    ''', "university")

    insert_to_db('''INSERT INTO groups (group_id,group_name) values (1, 'Lazy cows');
                    INSERT INTO groups (group_id,group_name) values (2, 'Inglorious bastards');
                    INSERT INTO groups (group_id,group_name) values (3, 'Insane globetrotters');
                    ''', "university")

