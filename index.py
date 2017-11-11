import os
import pymysql as pms
from bottle import *

conn = pms.connect(host='tsuts.tskoli.is', port=3306, user='1311992289', passwd='mypassword', db='1311992289_vef2Verk10')

def rows(cur):
    return [x for x in cur]

class Info:
    def __init__(self, site="", title="", prev_site="", message=""):
        self.__info = dict()
        self.__info["site"] = site
        self.__info["title"] = title
        self.__info["psite"] = prev_site
        self.__info["message"] = message

    def site(self, new_site=None):
        self.__info["site"] = self.__info["site"] if new_site is None else new_site
        return self.__info["site"]

    def title(self, new_title=None):
        self.__info["title"] = self.__info["title"] if new_title is None else new_title
        return self.__info["title"]

    def prev_site(self, new_prev_site=None):
        self.__info["psite"] = self.__info["psite"] if new_prev_site is None else new_prev_site
        return self.__info["psite"]

    def message(self, new_message=None):
        self.__info["message"] = self.__info["message"] if new_message is None else new_message
        return self.__info["message"]

    def info(self, new_info=None):
        self.__info = self.__info if new_info is None else new_info
        return self.__info

info = Info()

"^[^#*\"'<>{}[]().,]+$"

@route("/")
def home():
    global info
    info = Info("home", "Home", info.prev_site(), "")
    cook = request.get_cookie("user", secret="MoneyMoneyMoney")
    if info.prev_site() != "login":
        return template("index", info=info)
    else:
        if cook is not None:
            return template("Velkominn " + cook + "<form style=\"texte-align: center;\" method=\"post\" action=\"/\"><p style=\"display: none;\">{{info.prev_site(\"login\")}}{{info.site(\"home\")}}{{info.title(\"Home\")}}</p><input style=\"display: none;\" type=\"text\" name=\"info\" value=\"{{str(info.info())}}\"><input type=\"submit\" value=\"Log out\"></form>", info=info)
        else:
            return template("index", info=info)
@route("/", method="POST")
def home2():
    global info
    eval("info.info(" + request.forms["info"].replace("'", "\"") + ")")
    if info.site() == "home" and request.get_cookie("user", secret="MoneyMoneyMoney") is None:
        user = request.forms["user"]
        passw = request.forms["pass"]
        with conn.cursor() as cur:
            if info.prev_site() == "sign_up":
                cur.execute("SELECT * FROM users WHERE user='" + user + "'")
                row = rows(cur)
                if len(row) > 0:
                    info = Info("sign_up", "Sign Up", info.prev_site(), "Notandi er þegar til")
                else:
                    cur.execute("INSERT INTO users (user, pass) VALUES ('" + user  +"', '" + passw + "');")
                    conn.commit()
            elif info.prev_site() == "login":
                cur.execute("SELECT * FROM users WHERE user='" + user + "' and pass='" + passw + "'")
                row = rows(cur)
                if len(row) > 0:
                    response.set_cookie("user", user, "MoneyMoneyMoney")
                else:
                    info = Info("login", "Login", info.prev_site(), "Notandi er ekki til eða lykilorð er ekki rétt")
            else:
                print("not supposed to happen")
    else:
        response.delete_cookie("user")
    return template("index", info=info) if info.site() != "home" else "<meta http-equiv=\"refresh\" content=\"0; URL='/'\" />"

if os.environ.get("IS_HEROKU") is not None:
    run(host=0.0.0.0, port=os.environ.get("PORT"))
else:
    run()

conn.close()
