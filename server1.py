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
    cursor.execute("insert into todo (val,state,edit,uid) values ('%s',%s,%s,%s)"%(val,0,0,uid))
    db.commit()
    return "ok"

@app.route("/ajax/select",methods=["GET"])
def select ():
    cursor=db.cursor()
    uid=request.args.get("uid")
    sql="select * from todo where uid="+uid
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

app.run(host="0.0.0.0")



