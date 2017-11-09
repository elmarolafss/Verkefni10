import pymysql
from bottle import *



@route("/nyskra")
def nyskra():
    return template("verkefni10.tpl")

@route("/a_adgang")
def a_adgang():
    return template("innskraning.tpl")

@route("/gogn", method="POST")
def gogn():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1010972509', passwd='mypassword',db='1010972509_vef2verk10')
    cur = conn.cursor()
    name = request.forms.get("name")
    psw = request.forms.get("psw")
    while True:
        try:
            cur.execute("INSERT INTO user Values('%s','%s')" % (name,psw))
            break
        except pymysql.err.IntegrityError:
            return template("errorsida.tpl")
    conn.commit()
    cur.close()
    conn.close()
    return template("innskraning.tpl")

@route("/sida", method="POST")
def sida():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1010972509', passwd='mypassword',db='1010972509_vef2verk10')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user;")
    uname = request.forms.get("uname")
    passw = request.forms.get("passw")

    for i in cur:
        if i[0] == uname and i[1] == passw:
            return template("sida.tpl")
    cur.close()
    conn.close()
    return template("errorsida2.tpl")



run(host="localhost", port=8080, debug=True)