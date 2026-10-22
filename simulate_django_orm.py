import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="0000",database="DjangoORM")
print("connection created")
cur=conn.cursor()
# cur.execute("create database DjangoORM")
# print("database created")

# cur.execute("create table employee(id int primary key auto_increment,name varchar(20),designation varchar(20),salary decimal(10,2))")
# print("table created")

class Employee:
    
    def create(self,*args,**kwargs):
        print(kwargs)
        print(kwargs.keys())
        print(tuple(kwargs.values()))
        print(kwargs.items())

        cols=""
        placeholder="%s,%s,%s"
        for col in kwargs.keys():
            if cols!="":
                cols+=','
            cols=cols+col

        values = tuple(kwargs.values())
        query=f"insert into employee({cols}) values ({placeholder})"
        cur.execute(query,values)
        conn.commit()

    def list(self,*args,**kwargs):
        cur.execute("select * from employee")
        for emp in cur:
            print(emp)

        # print(cur.fetchall())

    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}={kwargs.get(key)}")
            print(cur.fetchall())

    def update(self,*args,**kwargs):
        print(args,kwargs)
        for key in kwargs:
            cur.execute(f"update employee set {key}='{kwargs.get(key)}' where id={args[0]}")
            conn.commit()
    
    def delete(self,*args,**kwargs):
        cur.execute(f"delete from employee where id={args[0]}")
        conn.commit()

    def filter():
        pass

employee=Employee()

while True:
    print("1.create employee")
    print("2.list all employee")
    print("3.employee detail view")
    print("4.update employee")
    print("5.delete employee")
    print("6.Exit")
    choice=int(input("enter your choice:"))
        
    if choice == 1:
        name = input("Enter your name: ")
        desig = input("Enter your designation: ")
        sal = float(input("Enter your salary: "))

        employee.create(name=name,designation=desig,salary=sal)

    
    elif choice==2:
        employee.list()

    elif choice == 3:
        emp_id = int(input("Enter employee ID: "))
        employee.retrieve(id=emp_id)

    elif choice==4:
        id=int(input("enter the employee id for updating:"))
        print("update:")
        print("1.name")
        print("2.designation")
        print("3.salary")
        choice=int(input("enetr your choice:"))
        if choice==1:
            name=input("enter the new name:")
            employee.update(id,name=name)
        elif choice==2:
            design=input("enter the new designation:")
            employee.update(id,designation=design)
        elif choice==3:
            sal=float(input("enter the new salry:"))
            employee.update(id,salary=sal)
        else:
            print("invalid choice entered")

    elif choice==5:
        id=int(input("enter the employee id for deleting:"))
        employee.delete(id)

    elif choice==6:
        print("filter options:")
        print("1.filter by name:")
        print("2.filter by designation:")
        print("3.filter by salary:")
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("enter your name:")
            employee.filter(name=name)
        if choice==2:
            design=input("enter your designation:")
            employee.filter(designation=design)
        if choice==3:
            sal=input("enter your salary:")
            employee.filter(salary=sal)

        employee.filter()

    elif choice==7:
        break

    else:
        print("invalid choice entered")






conn.close()