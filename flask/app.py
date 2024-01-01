from flask import Flask
new=Flask (__name__)

@new.route('/profile/jerry')
def profile():
    return '<h1>this is jerry</h1>'

new.run()