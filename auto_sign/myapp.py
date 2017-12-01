import sys
from flask import Flask, request
from auto.get_data import getData
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
    	params = {  'fromCityCode':request.form['fromCityCode'],
	       'toCityCode':request.form['toCityCode'],
			'fromDate':request.form['fromDate'],
			'returnDate':request.form['returnDate'],
			'carrier':request.form['carrier'],
			'isFirstQuery':request.form['isFirstQuery'],
			'transitCity':request.form['transitCity'],
			'flightType':request.form['flightType']}
        return getData(params)
    else:
        return """
        use post <br>
        post_param = {'fromCityCode':'CTU','toCityCode':'XIY','fromDate':'2017-11-26','returnDate':'2017-11-27','carrier':'','isFirstQuery':'1','transitCity':'PEK','flightType':'3'}

         """
    
if __name__ == '__main__':
    app.debug = False
    app.run()
