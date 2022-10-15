from flask import jsonify, request, json

def stock(mysql):
    cursor = mysql.connection.cursor()
    sql = "select v.name, su.name, s.selling_price, v.motor, v.gearbox, v.security " \
          "from stock s " \
          "inner join vehicle v on (s.name = v.id) inner join supplier su on (s.supplier = su.idsupplier)"
    cursor.execute(sql)
    data = cursor.fetchall()
    vehicles = []
    for fila in data:
        vehicle = {'name': fila[0], 'supplier': fila[1], 'price': fila[2], 'motor': fila[3], 'gearbox': fila[4],
                   'security': fila[5]}
        vehicles.append(vehicle)
    return jsonify({'vehicles': vehicles, 'message': 'Listed vehicles'})


def vehicle(mysql, name):
    cursor = mysql.connection.cursor()
    sql = "select v.name, su.name, s.selling_price, v.motor, v.gearbox, v.security from stock s " \
          "inner join vehicle v on (s.name = v.id) inner join supplier su on (s.supplier = su.idsupplier) " \
          "where v.name = '{0}'".format(name)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data is not None:
        vehicle = {'name': data[0], 'supplier': data[1], 'price': data[2], 'motor': data[3], 'gearbox': data[4],
                   'security': data[5]}
        return jsonify({'vehicles': vehicle, 'message': 'Information on the vehicle found'})
    else:
        return jsonify({'message': 'Vehicle not found'})

