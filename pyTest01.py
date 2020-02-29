from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('coronaManagerPage.html')

@app.route('/saveTable', methods=['POST'])
def saveTable_post(): # count, number, date, place, time
   count_receive = request.form['count_give']
   number_receive = request.form['number_give']
   date_receive = request.form['date_give'].split(',')
   place_receive = request.form['place_give'].split(',')
   time_receive = request.form['time_give'].split(',')
   print(count_receive, number_receive, date_receive, place_receive, time_receive)

   for i in range(int(count_receive)):
      doc = {
         'c_number' : number_receive,
         'c_date' : date_receive[i],
         'c_place' : place_receive[i],
         'c_time' : time_receive[i]
      }
      db.saveTest.insert_one(doc)

   return jsonify({
      'result': 'success',
      'msg': 'saved'
   })

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)