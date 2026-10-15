import mysql.connector as M
mycon=M.connect(host="localhost",username="root",password="sba2020",database="Library")
mycur=mycon.cursor()
if mycon.is_connected():
    print("success")
    
s="create table library(Bookid int,Bookname varchar(100),Authorname varchar(10),Price int,Bookstaken int)"
mycur.execute(s)
print("Successfully created!")

def add_books():
    e=int(input("Enter the no.of records you want to enter :"))
    for i in range(e):
        Bookname=input("Enter the bookname:")
        Bookid=int(input("Enter the bookid:"))
        Authorname=input("Enter the authorname:")
        Price=int(input("Enter the price:"))
        Qty=int(input("Enter the qty:"))
        Bookstaken=int(input("Enter the booktaken:"))
        mycur.execute("insert into library values('{}',{},'{}',{},{},{})".format(Bookname,Bookid,Authorname,Price,Qty,Bookstaken))
        mycon.commit()
        print("Successfully created!")

def delete_books():
    Bookid=int(input("Enter the bookid:"))
    mycur.execute("delete from library where Bookid={}".format(Bookid))
    mycon.commit()
    print("Successfully deleted!")

def update_books():
    Bookname=input("Enter the bookname:")
    Bookid=int(input("Enter the bookid:"))
    Authorname=input("Enter the authorname:")
    Price=int(input("Enter the price:"))
    mycur.execute("update library set Price={},Authorname='{}',Bookaname={} where Bookid={}".format(Price,Authorname,Bookname,Bookid))
    mycon.commit()
    print("Successfully updated!")

def display_details():
  j = int(input("Enter the bookid: "))
  q = "select * from library where bookid={}".format(j)
  mycur.execute(q)
  record = mycur.fetchone()

def add_column():
    k=input("Enter the coloumn name:")
    l=input("Enter datatype:")
    add="alter table library add('{}','{}')".format(k,l)
    mycur.execute(add)

while True:
    print("=====LIBRARY MENU=====")
    print("1.Add book")
    print("2.Update book details")
    print("3.Delete book")
    print("4.Display records")
    print("5.Add a new column")
    print("=====================")

    n=int(input("Enter the value:"))
    if n==1:
        while True:
            add_books()
            g=input("Do you add more books(y/n):")
            if g=="y":
                continue
            else:
                print("The given books are added successfully!")

    elif n==2:
        while True:
            update_books()
            g=input("Do you add more books(y/n):")
            if g=="y":
                continue
            else:
                print("The given books are updated successfully!")

    elif n==3:
        while True:
            delete_books()
            g=input("Do you add more books(y/n):")
            if g=="y":
                continue
            else:
                print("The given books are deleted successfully!")


    elif n==4:
        while True:
            display_details()
            g=input("Do you add more books(y/n):")
            if g=="y":
                continue
            else:
                print("The datas have been displayed successfully!")


    elif n==5:
        while True:
            add_column()
            g=input("Do you add more books(y/n):")
            if g=="y":
                continue
            else:
                print("The column has been added successfully!")

    else:
        print("Invalid code! Try again!")


j="create table customer_details(bid int,cid int,cname varchar(100),books_issued int,date_of_issue date,date_of_return date)"
mycur.execute(j)
print("Table created sucessfully!")

def add_customerdetails():
    o=int(input("Enter the no.of records you want to enter :"))
    for i in range(o):
        Bookid=int(input("Enter the bookid:"))
        Cid=int(input("Enter the cid:"))
        Cname=input("Enter the cname:")
        n=int(input("Enter the no.of books issued by the customer:"))
        k=input("Enter the date.of books issued by the customer:")
        l=input("Enter the date.of books issued by the customer:")
        klm="insert into customer_details values({},{},'{}',{},'{}','{}')".format(Bookid,Cid,Cname,n,k,l)
        mycur.execute(klm)
        mycon.commit()
        print("Successfully added!")

def update_customerdetails():
    Bookid=int(input("Enter the bookid:"))
    Cid=int(input("Enter the cid:"))
    Cname=input("Enter the cname:")
    n=int(input("Enter the no.of books issued by the customer:"))
    k=input("Enter the date.of books issued by the customer:")
    l=input("Enter the date.of books issued by the customer:")
    klm="update customer_details set cid={},cname='{}',n={},k='{}',l='{}' where Bookid={}".format(cid,cname,n,k,l,Bookid)
    mycur.execute(klm)
    mycon.commit()
    print("Successfully updated!")

def delete_books():
    Bookid=int(input("Enter the bookid:"))
    mycur.execute("delete from customer_details where Bookid={}".format(Bookid))
    mycon.commit()
    print("Successfully deleted!")

def display_all():
    t=int(input("Enter the customer id:"))
    k="select * from customer_details where library.Bookid=customer_details.Bookid and cid={}".format(t)
    mycur.execute(k)
    
def display_name():
    t=int(input("Enter the customer id:"))
    k="select cname from customer_details where library.Bookid=customer_details.Bookid and cid={}".format(t)
    mycur.execute(k)

def display_booksissue():
    t=int(input("Enter the customer id:"))
    k="select books_issued from customer_details where library.Bookid=customer_details.Bookid and cid={}".format(t)
    mycur.execute(k)

def display_date_of_issue():
    t=int(input("Enter the customer id:"))
    r="select date_of_issue from customer_details where library.Bookid=customer_details.Bookid and cid={}".format(t)
    mycur.execute(r)

def display_date_of_return():
    t=int(input("Enter the customer id:"))
    r="select date_of_return from customer_details where library.Bookid=customer_details.Bookid and cid={}".format(t)
    mycur.execute(r)

while True:
    print("=====CUSTOMER DETAILS MENU=====")
    print("1.Add customer details")
    print("2.Update customer details")
    print("3.Delete customer details")
    print("4.Display records")
    print("=====================")

    n=int(input("Enter the value:"))
    if n==1:
        while True:
            add_customerdetails()
            g=input("Do you add more books(y/n):")
            if g=="y":
                continue
            else:
                print("The given books are added successfully!")

    elif n==2:
        while True:
            update_customerdetails()
            g=input("Do you add more books(y/n):")
            if g=="y":
                continue
            else:
                print("The given books are updated successfully!")

    elif n==3:
        while True:
            delete_customerdetails()
            g=input("Do you add more books(y/n):")
            if g=="y":
                continue
            else:
                print("The given books are deleted successfully!")


    elif n==4:
        while True:
            print("=====DISPLAYING CUSTOMER DETAILS MENU=====")
            print("a. display customer name")
            print("b.display no.of book issued by the customer")
            print("c.display the date of issues")
            print("d.display the date of return")
            print("e. display all the records")
            print("=====================")

            x = input("Enter the value:").lower()
            if x=='a':
                while True:
                    display_name()
                    g=input("Do you add more books(y/n):")
                    if g=="y":
                        continue
                    else:
                        print("The given books are displayed successfully!")

            elif x=='b':
                while True:
                    display_booksissue()
                    g=input("Do you add more books(y/n):")
                    if g=="y":
                        continue
                    else:
                        print("The given books are displayed successfully!")

            elif x=='c':
                while True:
                    display_date_of_issue()
                    g=input("Do you add more books(y/n):")
                    if g=="y":
                        continue
                    else:
                        print("The given books are displayed successfully!")

            elif x=='d':
                while True:
                    display_date_of_return()
                    g=input("Do you add more books(y/n):")
                    if g=="y":
                        continue
                    else:
                        print("The given books are displayed successfully!")

            elif x=='e':
                while True:
                    display_all()
                    g=input("Do you add more books(y/n):")
                    if g=="y":
                        continue
                    else:
                        print("The given books are displayed successfully!")
            else:
                print("Invalid code! Try again!")

    






