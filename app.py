# we invoke the necessary libraries
from flask import Flask, render_template, jsonify, request
from config import config
from flask_mysqldb import MySQL
import controller

# The access point is created
server = Flask(__name__)

# The connection point to the base is created.
mysql = MySQL(server)


# The route to enter the service is created.
@server.get('/vehiculos')
def index():
    try:
        return controller.stock(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


# The path displaying unit information is created.
@server.get('/vehiculos/<string:name>')
def get_vehicle(name):
    try:
       return controller.vehicle(mysql, name)
    except Exception as ex:
        return jsonify({'message': ex})


# The route to create a new vehicle is created.
@server.post('/vehiculos')
def create_vehicle():
    try:
        cursor = mysql.connection.cursor()
        sql = """insert into vehicle(name, motor, gearbox, security) values ('{0}', '{1}', '{2}',
        '{3}') """.format(request.json['name'], request.json['motor'], request.json['gearbox'],
                          request.json['security'])
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'message': 'Vehicle created'})
    except Exception as ex:
        return jsonify({'message': ex})


# The route to create a new stock is created.
@server.post('/stock')
def create_stock():
    try:
        cursor = mysql.connection.cursor()
        sql = """insert into stock (name, supplier, selling_price, quantity) 
        values ('{0}', '{1}', '{2}', '{3}')""".format(request.json['name'], request.json['supplier'],
                                                      request.json['selling_price'], request.json['quantity'])
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'message': 'Stock update'})
    except Exception as ex:
        return jsonify({'message': ex})


# The route is created to remove the stock
@server.delete("/stock/<string:codigo>")
def delete_stock(codigo):
    try:
        cursor = mysql.connection.cursor()
        sql = "delete from stock where idstock = '{0}'".format(codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'message': "The stock was successfully removed"})
    except Exception as ex:
        return jsonify({'message': ex})


# A function is created to show when a page is not found.
def page_not_found(error):
    return render_template('404.html')


# the application is executed
if __name__ == '__main__':
    server.config.from_object(config['development'])
    server.register_error_handler(404, page_not_found)
    server.run()