import pyrebase

Config  =  {
    "apiKey": "AIzaSyC6YRogkoIApFmoZl3Hc__qtklNCH5Un88",
    "authDomain": "weather-monitoring-syste-9625a.firebaseapp.com",
    "projectId": "weather-monitoring-syste-9625a",
    "databaseURL":"https://weather-monitoring-syste-9625a-default-rtdb.firebaseio.com/",
    "storageBucket": "weather-monitoring-syste-9625a.appspot.com",
    "messagingSenderId": "787347206326",
    "appId": "1:787347206326:web:9fd9218a2cdd71fd6f7617",
    "measurementId": "G-4LJKN5JWQ2"}

firebase =pyrebase.initialize_app(Config)

db=firebase.database()

#push data
data={"distance_data":[["date:29-06-2021","+data:80","+time:1.35"],["date:29-06-2021","+data:80","+time:1.36"],["date:29-06-2021","+data:80","+time:1.37"],["date:29-06-2021","+data:80","+time:1.38"]],"flow_data":[["date:29-06-2021","+data:37","+time:1.35"],["date:29-06-2021","+data:37","+time:1.37"],["date:29-06-2021","+data:38","+time:1.37"],["date:29-06-2021","+data:38","+time:1.38"]]}
db.push(data)
