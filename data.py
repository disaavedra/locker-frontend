import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCUdFV7H0O6Xdxv88Ava2M0xLBfr1RFasM",
  "authDomain": "proyecto3-pds-system.firebaseapp.com",
  "projectId": "proyecto3-pds-system",
  "storageBucket": "proyecto3-pds-system.appspot.com",
  "messagingSenderId": "939097439559",
  "appId": "1:939097439559:web:6509bd0e3e79d3287fa062",
  "databaseURL": "https://proyecto3-pds-system-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)

def insert_order(order_data):
    try:
        db = firebase.database()
        db.child("order").push(order_data) 
        return "Datos insertados correctamente"
    except Exception as error:
        print("Error:", error)
        return "Error al insertar datos"

def get_orders():
    try:
        db = firebase.database()
        orders = db.child("order").get().val()
        return orders
    except Exception as error:
        print("Error:", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
def find_mail_by_value(data, target_value):
    for key, value in data.items():
        if value.get('value') == target_value:
            return value.get('mail')
    return None

# Ejemplo de uso
order_data = [{
    "value": 12345678,
    "mail": "usuario1@gmail.com"
}, 
{
    "value": 87654321,
    "mail": "usuario2@gmail.com"
},
{
    "value": 12121212,
    "mail": "usuario3@gmail.com"
}]
