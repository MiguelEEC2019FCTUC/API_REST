from flask import Flask, jsonify, request  # import funçoes do flask modulo
import sqlite3
import datetime
import json

conn = sqlite3.connect('identifier.sqlite',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

cursor = conn.cursor()


currentDateTime = datetime.datetime.now()

# query = ("SELECT UUID,Serial,Firmware,Flash,RS485,Relay,Contacto,PWM,CP FROM sqlite_master")
def imprimirTabela():
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()

    query = ("SELECT UUID,Firmware,RS485,Relay,Contact,CP,PWM,Serial FROM Mode3")
    cursor.execute(query)
    print(cursor.fetchall())

    conn.commit()

    conn.close()
    return


# def InserirTabela(uuid, firmware, rs485, relay, contact, cp, pwm, serial):
#     conn = sqlite3.connect('identifier.sqlite')
#     cursor = conn.cursor()
#
#     query = "INSERT INTO Mode3 (UUID,Firmware,RS485,Relay,Contact,CP,PWM,Serial) VALUES (?,?,?,?,?,?,?,?)"
#     data = (uuid, firmware, rs485, relay, contact, cp, pwm, serial)
#     cursor.execute(query, data)
#     conn.commit()
#
#     cursor.close()
#
#     return


# InserirTabela(5, 6, 1, 1, 1, 0, 1, 321) #nota: nao se pode introdizir uuid repetidos porque sao primary key
# imprimirTabela()

app = Flask(__name__)  # é criado um objeto do tipo flask e guardado com o nome app

# placas = [  # cria-se um array de dados e guarda-se na variável accounts
#   {'placa': "HRW48584", 'id': 12, 'Flash': "SIM"},  # esta placa tem indice na tabela 1
#  {'placa': "TTY87373", 'id': 3, 'Flash': "NAO"}  # e esta tem indice 2 e assim sucessivamente
# ]

# class Mode3:
#     def __init__(self, uuid, firmware, rs485, relay, contact, cp, pwm, serial):
#         self.uuid = uuid
#         self.firmware = firmware
#         self.rs485 = rs485
#         self.relay = relay
#         self.contact = contact
#         self.cp = cp
#         self.pwm = pwm
#         self.serial = serial

def db_connection():
    conn = sqlite3.connect('identifier.sqlite')
    return conn


def get_placa_json(placa_id):
    placa = {}
    try:
        conn = db_connection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Mode3 WHERE UUID = ?",(placa_id))

        row = cur.fetchone()

        #converter row em formato dicionário
        placa["placa_id"] = row["placa_id"]
        placa["Firmware"] = row["Firmware"]
        placa["Relay"] = row ["Relay"]
        placa["Contact"] = row["Contact"]
        placa["PWM"] = row["PWM"]
        placa["CP"] = row["CP"]
        placa["Serial"] = row["Serial"]
    except:
        placa = {}
    return placa


def insert_placa(placa):
    inserted_placa = {}
    try:
        conn = db_connection()
        cur = conn.cursor()
        query = "INSERT INTO Mode3 (Firmware, RS485, Relay, Contact, PWM, CP, Serial,TIMESTAMP) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        new_Firmware = request.json['Firmware']
        new_RS485 = request.json['RS485']
        new_Relay = request.json['Relay']
        new_Contact = request.json['Contact']
        new_PWM = request.json['PWM']
        new_CP = request.json['CP']
        new_Serial = request.json['Serial']
        timestamp = currentDateTime
        cur.execute(query, (new_Firmware, new_RS485, new_Relay, new_Contact, new_PWM, new_CP, new_Serial, timestamp))
        conn.commit()

        inserted_placa = get_placa_json(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_placa

#Funçoes que pesquisem uma placa por uma caracteristica
def get_placa_by_RS(rs485):
    placas = []
    conn = db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mode3 WHERE RS485 = ?", (rs485))
    rows = cursor.fetchall()
    #converter para formato dicionário
    for i in rows:
        placa = {}
        placa["UUID"] = i["UUID"]
        placa["Firmware"] = i["Firmware"]
        placa["RS485"] = i["RS485"]
        placa["Relay"] = i["Relay"]
        placa["Contact"] = i["Contact"]
        placa["PWM"] = i["PWM"]
        placa["CP"] = i["CP"]
        placa["Serial"] = i["Serial"]
        placa["TIMESTAMP"] = i["TIMESTAMP"]
        placas.append(placa)

    return placas
def get_placa_by_Relay(relay):
    placas = []
    conn = db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mode3 WHERE Relay = ?", (relay))
    rows = cursor.fetchall()
    #converter para formato dicionário
    for i in rows:
        placa = {}
        placa["UUID"] = i["UUID"]
        placa["Firmware"] = i["Firmware"]
        placa["RS485"] = i["RS485"]
        placa["Relay"] = i["Relay"]
        placa["Contact"] = i["Contact"]
        placa["PWM"] = i["PWM"]
        placa["CP"] = i["CP"]
        placa["Serial"] = i["Serial"]
        placa["TIMESTAMP"] = i["TIMESTAMP"]
        placas.append(placa)

    return placas
def get_placa_by_Contact(contac):
    placas = []
    conn = db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mode3 WHERE Contact = ?", (contac))
    rows = cursor.fetchall()
    #converter para formato dicionário
    for i in rows:
        placa = {}
        placa["UUID"] = i["UUID"]
        placa["Firmware"] = i["Firmware"]
        placa["RS485"] = i["RS485"]
        placa["Relay"] = i["Relay"]
        placa["Contact"] = i["Contact"]
        placa["PWM"] = i["PWM"]
        placa["CP"] = i["CP"]
        placa["Serial"] = i["Serial"]
        placa["TIMESTAMP"] = i["TIMESTAMP"]
        placas.append(placa)

    return placas
def get_placa_by_PWM(pwm):
    placas = []
    conn = db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mode3 WHERE PWM = ?", (pwm))
    rows = cursor.fetchall()
    #converter para formato dicionário
    for i in rows:
        placa = {}
        placa["UUID"] = i["UUID"]
        placa["Firmware"] = i["Firmware"]
        placa["RS485"] = i["RS485"]
        placa["Relay"] = i["Relay"]
        placa["Contact"] = i["Contact"]
        placa["PWM"] = i["PWM"]
        placa["CP"] = i["CP"]
        placa["Serial"] = i["Serial"]
        placa["TIMESTAMP"] = i["TIMESTAMP"]
        placas.append(placa)

    return placas
def get_placa_by_CP(cp):
    placas = []
    conn = db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mode3 WHERE CP = ?", (cp))
    rows = cursor.fetchall()
    #converter para formato dicionário
    for i in rows:
        placa = {}
        placa["UUID"] = i["UUID"]
        placa["Firmware"] = i["Firmware"]
        placa["RS485"] = i["RS485"]
        placa["Relay"] = i["Relay"]
        placa["Contact"] = i["Contact"]
        placa["PWM"] = i["PWM"]
        placa["CP"] = i["CP"]
        placa["Serial"] = i["Serial"]
        placa["TIMESTAMP"] = i["TIMESTAMP"]
        placas.append(placa)

    return placas
@app.route('/placas/add', methods = ['POST'])
def api_add_placa():
    placa = request.get_json()
    return jsonify(insert_placa(placa))


@app.route("/placas", methods=["GET", "POST"])  # é definido o endpoint API /placas e o método request (GET) e POST
def Placas():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM Mode3")
        placas = [
            dict(UUID=row[0], Firmware=row[1], RS485=row[2], Relay=row[3], Contact=row[4], CP=row[5], PWM=row[6],
                 Serial=row[7], TIMESTAMP = row[8])
            for row in cursor.fetchall()
        ]
        if placas is not None:
            return jsonify(placas)

@app.route("/placas/RS/<sn>",methods = ['GET'])
def RS(sn):
    return jsonify(get_placa_by_RS(sn))
@app.route("/placas/Relay/<sn>", methods = ['GET'])
def Relay(sn):
    return jsonify(get_placa_by_Relay(sn))
@app.route("/placas/Contact/<sn>", methods=['GET'])
def Contact(sn):
    return jsonify(get_placa_by_Contact(sn))
@app.route("/placas/PWM/<sn>", methods=['GET'])
def PWM(sn):
    return jsonify(get_placa_by_PWM(sn))
@app.route("/placas/CP/<sn>", methods=['GET'])
def CP(sn):
    return jsonify(get_placa_by_CP(sn))

    # if request.method == "POST":
    #     new_Firmware = request.form['Firmware']
    #     new_RS485 = request.form['RS485']
    #     new_Relay = request.form['Relay']
    #     new_Contact = request.form['Contact']
    #     new_PWM = request.form['PWM']
    #     new_CP = request.form['CP']
    #     new_Serial = request.form['Serial']
    #
    #     query = """INSERT INTO Mode3 (Firmware, RS485, Relay, Contact, PWM, CP, Serial) VALUES (?,?,?,?,?,?,?)"""
    #     cursor = cursor.execute(query, (new_Firmware, new_RS485, new_Relay, new_Contact, new_PWM, new_CP, new_Serial))
    #     conn.commit()
    #     return f"placa com id: {cursor.lastrowid} created sucessufully", 201


# @app.route("/placas/<int:id>", methods=["GET"])  # cria outra API endpoint onde o <id> vai ser o indice do array
# def getPlaca(id):
#     plac = [placas for placas in placas if placas['id'] == id]
#     return jsonify(plac[0])
#
#
# @app.route("/placas", methods=["POST"])  # cria-se outra endpoint com o metodo POST para ser adicionados novos dados
# def addPlaca():
#     placa = request.json['placa']
#     id = request.json['id']
#     data = {'placa': placa, 'id': id}
#     placas.append(data)
#     data['placa']
#     data['id']
#     return jsonify(data)


# é necessário adicionar um método PUT para o caso de ser preciso alterar dados de uma placa
# @app.route("/placas/<int:id>", methods=["PUT"])
# def AlterarPlaca(id):  # faz a verificaçao da placa pelo id
#     plac = [placas for placas in placas if placas['id'] == id]
#     plac[0]['placa'] = request.json.get('placa', plac[0]['placa'])
#     plac[0]['id'] = request.json.get('id', plac[0]['id'])
#
#     return jsonify(plac[0])
#
#
# # apresentar lista de todas as placas que estao flashadas
# @app.route("/placas/flash", methods=["GET"])
# def getFlash():  # verifica as placas se estao flashadas
#     Pflashed = []
#     for i in placas:
#         if placas[i].flash == "SIM":
#             Pflashed.append(placas[i])
#
#     # plac = [placas for placas in placas if placas['Flash'] == flash]
#     return jsonify(Pflashed)


if __name__ == '__main__':
    app.run(debug=True)
