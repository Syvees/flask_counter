from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "this is my flask secret key"

@app.route('/')  #index
def counter():  
    if 'key_name' in session:
        session['key_name'] = session.get('key_name') + 1
    else:
        session ['key_name'] = 1
    return render_template('index.html', total=session.get('key_name'))

@app.route('/counter2') #increase count by 2
def counter2():
    if 'key_name' in session:
        session['key_name'] = session.get('key_name') + 2
    else:
        session ['key_name'] = 1
    return render_template('index.html', total=session.get('key_name'))

@app.route('/destroy_session') #remove all keys
def destroy():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def error_handler(error):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True)
