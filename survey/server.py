from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'secret' # set a secret key for security purposes

@app.route('/')
def sign_up():
    return render_template("sign_up.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return redirect('/show')

@app.route("/show")
def show_user():
    return render_template('show.html')

if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

