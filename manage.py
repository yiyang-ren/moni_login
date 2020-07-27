from flask import Flask,render_template,request
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
# 打开csrf防护
CSRFProtect(app)
# 令牌前缀,让token更加复杂
app.config["SECRET_KEY"] = "fjkdjfkdfjdkdfdafdadfa"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/check',methods=['POST'])
def login():
    """登录功能"""
    uname = request.form.get('uname')
    pwd = request.form.get('pwd')
    if uname=="admin" and pwd == 'AaBb123#':
        return render_template('index.html')
    else:
        return render_template('login.html',errmsg='用户名或密码错误')




if __name__ == '__main__':
    app.run(debug=True)