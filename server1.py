from flask import Flask,request,render_template,redirect,make_response,session
import pymysql
import json
import common.common as m
app=Flask(__name__);
app.secret_key="uek"
db=pymysql.connect("localhost","root","123456","w1801",cursorclass=pymysql.cursors.DictCursor)
@app.route("/",methods=["GET"])
def index():
    print(session.get("login"))
    if(not session.get("login")):
        return redirect("/login")
    else:
        res=make_response(render_template("index.html"))
        return res
@app.route("/ajax/save",methods=["get"])
def save():
    info={"uid":session.get("uid"),"uname":session.get("uname")}
    print(json.dumps(info))
    return json.dumps(info)
@app.route("/login",methods=["GET"])
def login():
    return render_template("login.html");

@app.route("/reg",methods=["GET"])
def reg():
    return render_template("reg.html");


@app.route("/ajax/add",methods=["GET"])
def add ():
    uid=request.args.get("uid")
    cursor=db.cursor()
    val=request.args.get("val")
    did=request.args.get("did")
    cursor.execute("insert into todo (val,state,edit,uid,did) values ('%s',%s,%s,%s,%s)"%(val,0,0,uid,did))
    db.commit()
    return "ok"

@app.route("/ajax/select",methods=["GET"])
def select ():
    cursor=db.cursor()
    uid=request.args.get("uid")
    did=request.args.get("did")
    sql="select * from todo where uid="+uid+" and did="+did
    cursor.execute(sql)
    result=cursor.fetchall()
    return json.dumps(result)

@app.route("/ajax/del",methods=["GET"])
def delete():
    id=request.args.get("id")
    cursor = db.cursor()
    sql="delete from todo where id="+id
    cursor.execute(sql)
    db.commit()
    return "ok"
@app.route("/ajax/update",methods=["GET"])
def update():
    attr=request.args.get("attr");
    val=request.args.get("val");
    id=request.args.get("id");
    cursor = db.cursor()
    sql="update todo set %s='%s' where id=%s"%(attr,val,id)
    cursor.execute(sql)
    db.commit();
    return "ok"

@app.route("/ajax/adduser",methods=["POST"])
def adduser():
    uname=request.form["uname"]
    pass1=request.form["pass"]
    pass2=request.form["pass1"]
    if uname=="" or pass1=="" or pass1 != pass2:
        return redirect("/reg")

    cursor=db.cursor()
    sql="insert into user (uname,pass) values ('%s','%s')"%(uname,m.md5(pass1))
    cursor.execute(sql);
    db.commit()
    return "ok"

@app.route("/ajax/checkUser",methods=["GET"])
def checkUser():
    uname=request.args.get("uname");
    cursor = db.cursor()
    sql = "select * from user where uname='%s'"%(uname)
    result=cursor.execute(sql);
    if(result):
        return "err"
    else:
        return "ok"

@app.route("/ajax/checkLogin",methods=["POST"])
def checkLogin():
    uname=request.form["uname"]
    pass1=request.form["pass"]
    cursor = db.cursor()
    sql = "select * from user where uname=%s and pass=%s"
    cursor.execute(sql,[uname,m.md5(pass1)]);
    result=cursor.fetchall()
    if len(result)>0:
        arr={"uname":result[0]["uname"],"uid":result[0]["uid"],"message":"ok"}
        return json.dumps(arr)
    else:
        return json.dumps({"message":"error"})

#添加目录
@app.route("/ajax/adddir",methods=["GET"])
def adddir():
    name=request.args.get("name")
    type=request.args.get("type")
    uid=request.args.get("uid")
    pid=request.args.get("pid")
    edit=request.args.get("edit")
    cursor = db.cursor()
    sql="insert into dir (name,type,uid,pid,edit) values (%s,%s,%s,%s,%s)"
    cursor.execute(sql,[name,type,uid,pid,edit])
    inserid=db.insert_id()
    db.commit()
    return str(inserid)

#目录的查询和获取
@app.route("/ajax/selectdir",methods=["GET"])
def selectdir():
    uid=request.args.get("uid")
    cursor = db.cursor()
    sql="select * from dir where uid=%s"
    cursor.execute(sql,[uid])
    result=cursor.fetchall()
    return json.dumps(result)

# 目录的修改
@app.route("/ajax/dirupdate",methods=["GET"])
def dirupdate():
    id = request.args.get("id")
    attr = request.args.get("attr")
    val = request.args.get("val")
    cursor = db.cursor()
    sql = "update dir set "+attr+"=%s where id=%s"
    cursor.execute(sql, [val,id])
    db.commit()
    return "ok"

# 删除目录

@app.route("/ajax/deleteDir",methods=["GET"])
def deleteDir():
    ids=request.args.get("ids");
    obj=json.loads(ids)
    str1="("
    str2="("
    flag=True
    for item in obj:
        str1+=str(item["id"])+","
        if(item["type"]==0):
            flag=False
            str2+=str(item["id"])+","
    str1=str1[:-1]
    str2=str2[:-1]
    str1+=")"
    str2+=")"
    if flag:
        str2="(0)"
    cursor = db.cursor()
    sql1="delete from dir where id in "+str1;
    sql2="delete from todo where did in "+str2;

    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
    except:
        db.rollback()
    else:
        db.commit()

    return "ok"



app.run(host="0.0.0.0")



