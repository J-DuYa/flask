from flask import Flask, request, render_template, abort, redirect, url_for, make_response, session, escape
app = Flask(__name__)

@app.route("/")
def index():
  if 'username' in session:
    return "Logged in as %s" % escape(session["username"]) 
  return "You are not logged in"

# 登录
@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == "POST":
    session["username"] = request.form["username"]
    return redirect(url_for("index"))
  return '''
      <form action="" method="post">
          <p><input type=text name=username>
          <p><input type=submit value=Login>
      </form>
  '''

# 登出
@app.route("/logout")
def logout():
  session.pop("username", None)
  return redirect(url_for("index"))

# 401界面
@app.errorhandler(401)
def page_not_auth(error):
  return render_template("401.html"), 401

# 404界面
@app.errorhandler(404)
def page_not_found(error):
  res = make_response(render_template("404.html"), 404)
  res.headers["E-question"] = "PageNotFound"
  return res

@app.route("/info", methods=["GET",])
def sendinfo():
  sendid = request.args.get('id')
  return "Get info id is " + str(sendid)

@app.route("/home", methods=["GET"])
def home():
  username = request.args.get("username")
  return render_template("index.html", username=username)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port =8080)