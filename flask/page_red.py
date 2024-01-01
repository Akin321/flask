from flask import Flask
hello=Flask (__name__)

@hello.route('/')
def home():
    return '<h1>home page</h1>'
@hello.route('/new')
def new():
    return '<h1>this is new page</h1>'

hello.run()