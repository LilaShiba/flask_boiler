from flask import *
from app import app
from app.models import giphy

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/shoData', methods=['GET','POST'])
def shoData():
    userdata = dict(request.form)
    print(userdata)
    return render_template('shoData.html', name=userdata['name'][0], age=userdata['age'][0])


@app.route('/api_request')
def api_request():
    return render_template('api_request.html')

# add from app.models import giphy
@app.route('/api_info', methods=['GET','POST'])
def api_info():
    api_data = dict(request.form)
    # print(api_data)
    search_term = api_data["search_term"][0]
    data = giphy.api_call(search_term)
    return render_template('api_info.html', data=data[0], all_pics=data[1])
