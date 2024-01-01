from flask import Flask
app=Flask (__name__)

@app.route('/profile/<username>')
def profile(username):
    return '<h1>this is for %s </h1>' % username
app.run()