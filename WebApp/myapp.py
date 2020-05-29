import time
import csv
from flask import Flask, Markup, render_template

app = Flask(__name__)

labels = []
values = []

with open("/var/tmp/SmokerPi/RasPi/temp.log") as csvfile:
#    csv_dict = csv.DictReader(csvfile, delimiter=",")
    csv_dict = dict(filter(None, csv.reader(csvfile)))


    labelKeys = ["Time"]
    labels = [ csv_dict[x] for x in labelKeys ]

    valueKeys = ["Temp"]
    values = [ csv_dict[x] for x in valueKeys ]


#labels = [
#    'JAN', 'FEB', 'MAR', 'APR',
#    'MAY', 'JUN', 'JUL', 'AUG',
#    'SEP', 'OCT', 'NOV', 'DEC'
#]

#values = [
#    967.67, 1190.89, 1079.75, 1349.19,
#    2328.91, 2504.28, 2873.83, 4764.87,
#    4349.29, 6458.30, 9907, 16297
#]

@app.route('/')
def line():
    line_labels=labels
    line_values=values
    timeNow = time.time()
    return render_template('line_chart.html', title='Smoker Temperature', cur_tmp=timeNow, max=17000, labels=line_labels, values=line_values)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
