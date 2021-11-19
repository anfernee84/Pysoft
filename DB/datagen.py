import psycopg2
from random import randrange
import faker
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from datetime import datetime, timedelta
import random

#------------------------------------- Grade Generation---------------------------------
try:
    connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",
            database = "university")
    cursor = connection.cursor()
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

  
    sql_query = 'INSERT INTO grades (GRADE_DATE, GRADE, COURSE_ID, STUDENT_ID ) VALUES (%s, %s, %s, %s)'
    for i in range (1, 31):
        for j in range(20):
            fake_date = faker.Faker().date_between(start_date='-20y', end_date='-10y')
            cursor.execute(sql_query, ( fake_date, randrange(2, 6), randrange(1, 6),i))

except (Exception, Error) as error:
    print('Error', error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection is closed')


#----------------------------------------Groups generation-----------------------------------
# try:
#     connection = psycopg2.connect(

#             user = "postgres",
#             password = "password",
#             host = "10.0.17.42",
#             port = "5432",
#             database = "university")
#     cursor = connection.cursor()
#     connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#     sql_query = 'INSERT INTO groups VALUES (%s, %s, %s, %s)'

#     for i in range (1, 601):
#         group_names = ['Lazy cows', 'Inglorious bastards', 'Insane globetrotters']
#         cursor.execute(sql_query, (randrange(1, 4), random.choice(group_names), i, randrange(1, 4)))

# except (Exception, Error) as error:
#     print('Error', error)

# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print('Connection is closed')


#-------------------------------------Students Generation------------------------------------------
try:
    connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",
            database = "university")
    cursor = connection.cursor()
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    sql_query = 'INSERT INTO students (STUDENT_NAME, GROUP_ID) VALUES (%s, %s)'

    for j in range(1,4):
        for i in range (1, 11):
            fake_name = faker.Faker().name()
            cursor.execute(sql_query, ( fake_name,j))

except (Exception, Error) as error:
    print('Error', error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection is closed')        