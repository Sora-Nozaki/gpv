from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/index")
def index():
	member_dic = {}
	B4_list = ['B4taro', 'B4jiro', 'B4hanako']
	M1_list = ['M1taro', 'M1jiro', 'M1hanako']
	M2_list = ['M2taro', 'M2jiro', 'M2hanako']
	member_dic['B4'] = B4_list
	member_dic['M1'] = M1_list
	member_dic['M2'] = M2_list
	return render_template('layout.html', message=member_dic)

# 実行関数を追加
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)
