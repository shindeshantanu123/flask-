import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='shantanu')
    
def addEmp(t):
    db=getConnection()
    sql='insert into emp1 values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()



def selectAllEmp():
    db=getConnection()
    sql='select * from emp1'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deleteEmp(id):
    db=getConnection()
    sql='delete from  emp1 where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectEmpById(id):
    db=getConnection()
    sql='select * from emp1 where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update emp1 set name=%s,contact=%s,email=%s,passw=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def log(t):
    db=getConnection()
    sql="select name,passw from emp1 where name=%s and passw=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
