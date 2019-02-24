# Python & Javascript

Chartist is not really designed for real-time update
Needs to redraw the entire chart


Insert Data
db.charts.insert({"name" :"Chart1", "values" : [9,2,9,4,2]})
db.charts.insert({"name" :"Chart2", "values" : [5,1,8,4,5]})
db.charts.insert({"name" :"Chart3", "values" : [15,28,11,14,5]})

db.charts.update({_id:ObjectId("5c717c6ab32d0b246d2adb7b")}, {"name" : "Chart2", "values" : [5,1,8,4,5]})