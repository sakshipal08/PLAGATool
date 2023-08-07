from algorithm importsklearnCosineSimilarity

app = Flask(__name__,
            static_url_path='/assets',
            static_folder='./templates/assets',
            )

@app.route('/logOut')
deflogOut():
    returnrender_template('index.html')

@app.route('/registration' ,  methods=['POST', 'GET'])
defregistration():
    ifrequest.method=="POST":
          username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        mobile = request.form["mobile"]
        InsertData(username,email,password,mobile)
        returnrender_template('login.html')

    returnrender_template('registration.html')

@app.route('/', methods=['POST', 'GET'])
deflogin():
    ifrequest.method=="POST":
        email = request.form['username']
        passw = request.form['password']
        resp = read_cred(email, passw)
        ifresp != None:
            return redirect("/home")
        else:    message = "Username and/or Password incorrect.\\n        Yo have not registered Yet \\nGo to Register page and do Registration";
            return"<script type='text/javascript'>alert('{}');</script>".format(message)

    returnrender_template('index.html')

@app.route('/home')
defhome():
    # return render_template('index.html')
    returnrender_template('home.html')

@app.route('/checkPlagiarismNLP',methods=["POST"])
defcheckPlagiarismNLP():
    returnrender_template('result.html')
@app.route('/checkPlagiarismSklearn',methods=["POST"])
defcheckPlagiarismSklearn():
    output = sklearnCosineSimilarity.check_plagiarism(os.getcwd()+"\\"+"assignments")
    returnrender_template('result.html',outputs=output)

@app.route('/checkPlagiarismArrayMatrix',methods=["POST"])
defcheckPlagiarismArrayMatrix():
    returnrender_template('result.html' )

@app.route('/index')
defai_engine_page():
    returnrender_template('home.html')
if__name__ == '__main__':
    app.run(debug=False)
    print(sklearnCosineSimilarity.check_plagiarism("assignment"))


