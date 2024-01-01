from flask import Flask, render_template

app=Flask (__name__)

@app.route('/profile/<username>')
def home(username):
    return render_template('profile.html',username=username)

app.run(debug=True)