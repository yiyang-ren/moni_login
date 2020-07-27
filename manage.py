from flask import Flask,render_template,request,jsonify
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
# 打开csrf防护
CSRFProtect(app)
# 令牌前缀,让token更加复杂
app.config["SECRET_KEY"] = "fjkdjfkdfjdkdfdafdadfa"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        uname = request.form.get('uname')
        pwd = request.form.get('pwd')
        pwd2 = request.form.get('pwd2')
        print(uname)
        print(pwd)

        # 后期连接数据库保存到数据库
        return render_template('index.html',uname=uname)





@app.route('/check',methods=['POST'])
def login():
    """登录功能"""
    uname = request.form.get('uname')
    pwd = request.form.get('pwd')
    if uname=="admin" and pwd == 'AaBb123#':
        return render_template('index.html')
    else:
        return render_template('login.html',errmsg='用户名或密码错误')

@app.route('/ret_name',methods=['GET'])
def ret_name():
    uname = request.args.get('uname')
    if uname == 'admin':
        return jsonify(errno='500',errmsg='false')
    else:
        return jsonify(errno='200',errmsg='ok')



if __name__ == '__main__':
    app.run(debug=True)