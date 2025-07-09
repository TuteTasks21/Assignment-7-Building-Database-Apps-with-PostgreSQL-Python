import psycopg2


def table():
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="Anewdata123", host="localhost", port="5432") 

    cursor=conn.cursor()
    cursor.execute('''create table employees(Name text,ID int,Age int);''')

    print("Table Created Successfully")
    conn.commit()
    cursor.close()

# def data():
#     conn=psycopg2.connect(dbname="postgres",user="postgres",password="Anewdata123", host="localhost", port="5432") 

#     cursor=conn.cursor()
#     name=input("Enter Name: ")
#     id=input("Enter ID: ")
#     age=input("Enter Age: ")
#     query='''insert into employees(Name,ID,Age) values(%s,%s,%s);'''

#     cursor.execute(query,(name,id,age))

#     print("Data Added Successfully")
#     conn.commit()
#     cursor.close()

# data()



def extract():
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="Anewdata123", host="localhost", port="5432") 

    cursor=conn.cursor()
    cursor.execute('''select * from employees;''')
    show=cursor.fetchall()
    print(show[0])

    conn.commit()
    cursor.close()
extract()
