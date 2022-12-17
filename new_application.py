import sqlite3

# try:

db = sqlite3.connect("user_data.db")
cr = db.cursor()
cr.execute(
    "create table if not exists users(id integer , name text , dep text , phone integer)")
id1 = int(input("Please Advise ID: ").strip())
name = input("Please Advise Name : ").strip().capitalize()
dep = input("Please Advise Department: ")
phone = int(input("please advise Number: ").strip())


cr.execute(f"select rowid from users where id =('{id1}')")
idfetch = cr.fetchall()
if len(idfetch) == 0:
    print("ID Not Exists and will be added")
    cr.execute(f"select rowid from users where name =('{name}')")
    namefetch = cr.fetchall()
    if len(namefetch) == 0:
        print("Name Not Exist and all data will be added")
        cr.execute(
            f"insert into users (id,name,dep,phone) values ('{id1}','{name}','{dep}','{phone}')")
        cr.execute(f"select * from users where id=('{id1}')")
        result = cr.fetchone()
        print(
            f"Thanks for adding below :\nID: {result[0]}\nName: {result[1]}\nDep: {result[2]}\n{result[3]}")
    else:
        print('Name %s found with rowids %s' %
              (name, ','.join(map(str, next(zip(*namefetch))))))
else:
    print('ID %s found with rowids %s' %
          (id1, ','.join(map(str, next(zip(*idfetch))))))


# except:


db.commit()
db.close()
