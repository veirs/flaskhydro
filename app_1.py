from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
def do_toggle_AGC():
	with open('agc_control.txt', 'r') as f:
		agc = f.read()
	if agc == '1':
	  agc = '0'
	else:
	  agc = '1'
	print("Current AGC=", agc)
	with open('agc_control.txt', 'w') as f:
		f.write(agc)

def getdata():
	infile = open('currentreport.txt', 'r')
	data = infile.read()
	items = data.split('_')
	print(items[1], items[3], items[5])
	return (items[1], items[3], items[5])

@app.route('/', methods=['GET', 'POST'])
def index():
	print(request.method)
	if request.method == 'POST':
		if request.form.get('toggleAGC') == 'toggle_AGC':
			do_toggle_AGC()		
	now = datetime.datetime.now()
	timestring = now.strftime("%Y-%m-%d %H:%M:%S")
	somedata = getdata()
	templatedata = {
		'title' : 'HTI Hydrophone',
		'time': timestring,
		'dB'  : somedata[0],
		'dBave': somedata[1],
		'Gain' : somedata[2]
		}
	return render_template('index.html', **templatedata)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)  #port=80, 
