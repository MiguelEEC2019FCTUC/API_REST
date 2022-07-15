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

def insert_Mode3(placa):
    inserted_placa = {}

    conn = db_connection()
    cur = conn.cursor()
    query = ("INSERT INTO Mode3 (Firmware, RS485, Relay, Contact, PWM, CP, Serial,TIMESTAMP) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
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

    conn.close()

    return inserted_placa
#Funçoes que pesquisem uma placa por uma caracteristica
def get_placa_by_RS(rs485,nome_placa):
    placas = []
    conn = db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ? WHERE RS485 = ?",(nome_placa) , (rs485))
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
def get_placa_json(placa_id,nome_placa):
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
def get_placa_by_Serial(serial): #considerando que nao há várias placas com o mesmo Serial nº
    placas = []
    conn = db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mode3 WHERE Serial = ?",(serial,))
    rows = cursor.fetchone()
    # converter para formato dicionário
    #for i in rows:
    placa = {}
    placa["UUID"] = rows["UUID"]
    placa["Firmware"] = rows["Firmware"]
    placa["RS485"] = rows["RS485"]
    placa["Relay"] = rows["Relay"]
    placa["Contact"] = rows["Contact"]
    placa["PWM"] = rows["PWM"]
    placa["CP"] = rows["CP"]
    placa["Serial"] = rows["Serial"]
    placa["TIMESTAMP"] = rows["TIMESTAMP"]
    #placas.append(placa)

    return placa
#-------------------------------------------------
def get_placa_json2(placa_id):
    placa = {}
    try:
        conn = db_connection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM CCS WHERE UUID = ?",(placa_id))

        row = cur.fetchone()

        #converter row em formato dicionário
        placa["placa_id"] = row["placa_id"]
        placa["Serial"] = row["Serial"]
        placa["teste1"] = row ["teste1"]
        placa["teste2"] = row["teste2"]
        placa["teste3"] = row["teste3"]
        placa["test4"] = row["test4"]
        placa["test5"] = row["test5"]
    except:
        placa = {}
    return placa
def insert_CCS(ccs):
    inserted_placa = {}
    conn = db_connection()
    cur = conn.cursor()
    query = ("INSERT INTO CCS (Serial, teste1,teste2,teste3,test4,test5,Firmware,TIMESTAMP) VALUES (?, ?, ?, ?, ?, ?, ?,?)")
    new_serial = request.json['Serial']
    new_test1 = request.json['teste1']
    new_tes2 = request.json['teste2']
    new_test3 = request.json['teste3']
    new_test4 = request.json['test4']
    new_test5 = request.json['test5']
    new_firmware = request.json['Firmware']
    timestamp = currentDateTime
    cur.execute(query, (new_serial,new_test1,new_tes2,new_test3,new_test4,new_test5,new_firmware,timestamp))
    conn.commit()

    inserted_placa = get_placa_json2(cur.lastrowid)

    conn.close()

    return inserted_placa
#-------------------------------------------------
def insert_CHADEMO(chademo):
    inserted_placa = {}
    conn = db_connection()
    cur = conn.cursor()
    query = (
        "INSERT INTO CHADEMO (Serial, teste,Firmware,TIMESTAMP) VALUES (?, ?, ?, ?)")
    new_serial = request.json['Serial']
    new_teste = request.json['teste']
    new_firmware = request.json['Firmware']
    timestamp = currentDateTime
    cur.execute(query, (new_serial, new_teste, new_firmware, timestamp))
    conn.commit()

    inserted_placa = get_placa_json2(cur.lastrowid)

    conn.close()

    return inserted_placa

#rotas para Mode3
@app.route('/tests/Mode3/add', methods = ['POST'])
def api_add_Mode3():
    Mode3 = request.get_json()
    return jsonify(insert_Mode3(Mode3))
@app.route("/tests/Mode3", methods=["GET", "POST"])  # é definido o endpoint API /placas e o método request (GET) e POST
def Mode3():
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
@app.route("/tests/Mode3/Serial/<serial>", methods = ['GET'])
def Serial(serial):
    return jsonify(get_placa_by_Serial(serial))
@app.route("/tests/Mode3/RS/<sn>",methods = ['GET'])
def RS(sn):
    return jsonify(get_placa_by_RS(sn))
@app.route("/tests/Mode3/Relay/<sn>", methods = ['GET'])
def Relay(sn):
    return jsonify(get_placa_by_Relay(sn))
@app.route("/tests/Mode3/Contact/<sn>", methods=['GET'])
def Contact(sn):
    return jsonify(get_placa_by_Contact(sn))
@app.route("/tests/Mode3/PWM/<sn>", methods=['GET'])
def PWM(sn):
    return jsonify(get_placa_by_PWM(sn))
@app.route("/tests/Mode3/CP/<sn>", methods=['GET'])
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

#rotas para CCS
@app.route("/tests/CCS",methods = ['GET'])
def CCS():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM CCS")
        placas = [
            dict(UUID=row[0], Serial = row[1], teste1=row[2], teste2=row[3], teste3=row[4], test4=row[5], test5=row[6], Firmware = row[7],TIMESTAMP = row[8])
            for row in cursor.fetchall()
        ]
        if placas is not None:
            return jsonify(placas)
@app.route("/tests/CCS/add", methods = ['POST'])
def api_add_CCS():
    CCS = request.get_json()
    return jsonify(insert_CCS(CCS))

#rotas para CHADEMO
@app.route("/tests/CHADEMO",methods = ['GET'])
def CHADEMO():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM CHADEMO")
        placas = [
            dict(UUID = row[0], Serial = row[1], teste = row[2], Firmware = row[3], TIMESTAMP = row[4])
            for row in cursor.fetchall()
        ]
        if placas is not None:
            return jsonify(placas)
@app.route("/tests/CHADEMO/add", methods = ['POST'])
def api_add_CHADEMO():
    CHADEMO = request.get_json()
    return jsonify(insert_CHADEMO(CHADEMO))
#--------------------------------------------------------------------
# #CALIBRATION METER
# def CalibData(Array_tensao, Array_corrente):
#
#     data = {}
#
#     data["Tensao"] = Array_tensao
#     data["Corrente"] = Array_corrente
#     print(data)
#     return data
#
# def TestData(P_tensao,P_corrente,req_tensao,req_corrente):
#     data = {}
#
#     data["Tensao"] = P_tensao
#     data["Corrente"] = P_corrente
#     data["Req Tensao"] = req_tensao
#     data["Req Corrente"] = req_corrente
#     print(data)
#
#     return data
#
# def Insert_Calibration(meter):
#     data_inserted = {}
#
#     conn = db_connection()
#     cur = conn.cursor()
#     query = "INSERT INTO METER (Serial, CalibData, TestData,Status,TIMESTAMP) VALUES (?, ?, ?, ?,?)"
#     new_CalibData = request.json['CalibData']
#     new_TestData = request.json['TestData']
#     new_serial = request.json['Serial']
#     new_Status = request.json['Status']
#     timestamp = currentDateTime
#     cur.execute(query, (new_CalibData,new_TestData,new_serial,new_Status,timestamp))
#     conn.commit()
#
#     data_inserted = get_placa_json(cur.lastrowid)
#
#     conn.close()
#
#     return data_inserted
#
# #calibraçao de meters
# @app.route("/Meter/Calibration", methods = ['POST'])
# def api_add_dataMeters():
#     data = request.get_json()
#     return jsonify(Insert_Calibration(data))



# @app.route("/placas/<int:id>", methods=["GET"])  # cria outra API endpoint onde o <id> vai ser o indice do array
# def getPlaca(id):
#     plac = [placas for placas in placas if placas['id'] == id]
#     return jsonify(plac[0])

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
    app.run(debug=True,port=8080)

