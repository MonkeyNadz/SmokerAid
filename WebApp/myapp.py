import time
import json
from flask import Flask, Markup, render_template
from pathlib import Path


app = Flask(__name__)

def update():
    with open("/var/tmp/SmokerPi/RasPi/temp.log") as log_file:
        lines = [line.rstrip() for line in log_file]

#print(lines)
    labels = []
    values = []
    for l in lines:
        log = json.loads(l)

        labels.append(log["time"])
        values.append(log["temp"])

    return labels, values

target_tmp = 0

path = Path('..')
#print (path.cwd().parent)
settingsPath = str(path.cwd().parent) + "/RasPi/src/"


with open(str(settingsPath) + "settings.conf", "r") as sf:
    data = json.load(sf)
    target_tmp = int(data["target_tmp"])
    sf.close()

@app.route('/')
def line():
    line_labels, line_values = update()
    #line_labels=labels
    #line_values=values
    timeNow = time.time()
    current_tmp = str(line_values[len(line_values)-1])
    return render_template('line_chart.html', title='Smoker Temperature', cur_tmp=current_tmp, max=max(line_values),min=min(line_values), labels=line_labels, values=line_values, tgt_tmp=target_tmp)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
