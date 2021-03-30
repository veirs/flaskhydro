from flask import Flask, render_template
import datetime
import sounddevice as sd
import sys
import numpy as np

app = Flask(__name__)

def getdata():
	return datetime.datetime.today().timestamp()

samplerate = sd.query_devices('hw:1,0', 'output')['default_samplerate']
start_idx = 0
def callback(outdata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    global start_idx
    t = (start_idx + np.arange(frames)) / samplerate
    t = t.reshape(-1, 1)
    outdata[:] = 1.0 * np.sin(2 * np.pi * 1000.0 * t)
    start_idx += frames


with sd.OutputStream(device='hw:1,0', channels=1, callback=callback,
                     samplerate=samplerate):
    print('#' * 80)
    print('press Return to quit')
    print('#' * 80)
    input()


@app.route('/')
def index():
	now = datetime.datetime.now()
	timestring = now.strftime("%Y-%m-%d %H:%M:%S")
	somedata = getdata()
	templatedata = {
		'title' : 'HTI Hydrophone',
		'time': timestring,
		'dB'  : somedata
		}
	return render_template('index.html', **templatedata)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
