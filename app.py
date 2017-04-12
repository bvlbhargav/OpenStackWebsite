
#Importing Flask package

from flask import Flask, render_template
app = Flask(__name__)

#Routing configuration for the Welcome page of the application
@app.route("/")
def main():
    return render_template('index.html')

#Routing configuration for the Signup page of application
@app.route('/showSignUp/')
def showSignUp():
    return render_template('signup.html')
    
if __name__ == "__main__":
    app.run()