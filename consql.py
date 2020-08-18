import pyodbc
def Select2(conexion):
    print("mostrando datos2")
    cur=conexion.cursor()
    cur.execute("select * from dimusers")
    result= cur.fetchmany(3)
    print(result)
    
def Select(conexion):
    print("mostrando datos")
    cur=conexion.cursor()
    cur.execute("select * from dimusers")
    for fila in cur:
        print(fila)
        
def Insert(conexion):
    print("insert")
    cur=conexion.cursor()
    cur.execute("insert into dimusers values ('BTO\\Alberto')")
    cur.commit()
    Select(conexion)
                
def Update(conexion):
    print("actulizando")
    cur=conexion.cursor()
    cur.execute("update dimusers set account = 'BTO\\Anibal' where accountid = 1007")
    cur.commit()
    Select(conexion)
    
def Delete(CONEXION):
    print("borrando")
    cur=CONEXION.cursor()
    cur.execute("delete from dimusers where accountid = 1007") 
    cur.commit()
    Select(CONEXION)                
    
cn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=.;"
    "Database=DataMart__Security;"
    "Trusted_Connection=Yes;"    
    )

if cn:
    print("conecto!")
    
    
Select2(cn)
#Insert(cn)
#Update(cn)
#Delete(cn)

cn.close()