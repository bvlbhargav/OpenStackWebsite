
#Importing Flask package

from flask import Flask, render_template, request, json
app = Flask(__name__)

#Routing configuration for the Welcome page of the application
@app.route("/")
def main():
    return render_template('index.html')

#Routing configuration for the Signup page of application
@app.route('/showSignUp/')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    #Signup code will be written here
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

     # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    
if __name__ == "__main__":
    app.run()