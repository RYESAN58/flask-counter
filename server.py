from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'lamelo ball'
@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        session['counter'] = session['counter']
        session['counter'] +=1
        print(session['counter'])
        return render_template('index.html')
    else:
        pass

@app.route('/destroy_session', methods=['GET'])
def destroy():
    session['counter'] = 0
    return redirect('/')

@app.route('/plustwo', methods=['GET'])
def plustwo():
    session['counter'] =session['counter'] + 1
    return redirect('/')
@app.route('/resetter',methods = ['GET'])
def reset():
    session['counter']= 0
    return redirect('/')
@app.route('/random', methods=['POST'])
def rand():
    session['num']= request.form["num"]
    session['counter'] = int(session['num']) + int(session['counter'])-1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)