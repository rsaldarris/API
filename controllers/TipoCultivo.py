from flask import jsonify, request
from db.db import cnx

class TipoCultivo():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM tipo_cultivos")
        rows = cur.fetchall()
        print("prueba")
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns,row)
            json = dict(registro)
            lista.append(json)
            
        return jsonify(lista)
        cnx.close

    def create(body):
        data = (body['codigo'],body['latitud'],body['longitud'],body['producto'],body['area'],body['imag'])
        sql = "INSERT INTO tipo_cultivos(codigo, latitud, longitud, producto, area, foto) VALUES(%s, %s, %s, %s, %s, %s)"
        print("intento")
        cur.execute(sql,data)
        cnx.commit()
        return {'estado':"Insertado"}, 200