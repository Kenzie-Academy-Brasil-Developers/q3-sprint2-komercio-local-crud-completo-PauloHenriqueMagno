from flask import Flask, request, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "name": "sabonete", "price": 5.99},
    {"id": 2, "name": "perfume", "price": 39.90},
    {"id": 3, "name": "tapete", "price": 10.30},
    {"id": 4, "name": "tunica", "price": 19.29},
    {"id": 5, "name": "chuveiro", "price": 119.19},
    {"id": 6, "name": "arroz", "price": 30.10},
    {"id": 7, "name": "oleo de cozinha", "price": 11.15},
    {"id": 8, "name": "carne moida", "price": 39.90},
    {"id": 9, "name": "bola", "price": 25.99},
    {"id": 10, "name": "cantil", "price": 55.99},
    {"id": 11, "name": "copo", "price": 5.99},
    {"id": 12, "name": "panela", "price": 25.99},
    {"id": 13, "name": "prato", "price": 10.99},
    {"id": 14, "name": "açucar", "price": 7.99},
    {"id": 15, "name": "sal", "price": 5.99},
    {"id": 16, "name": "pipoca", "price": 3.14},
    {"id": 17, "name": "sabonete", "price": 5.99},
    {"id": 18, "name": "miojo", "price": 2.39},
    {"id": 19, "name": "alface", "price": 3.99},
    {"id": 20, "name": "tomate", "price": 9.99},
    {"id": 21, "name": "macarrao", "price": 6.40},
    {"id": 22, "name": "mesa", "price": 115.99},
    {"id": 23, "name": "cadeira gamer", "price": 445.99},
    {"id": 24, "name": "mouse gamer", "price": 215.99},
    {"id": 25, "name": "tv", "price": 995.99},
    {"id": 26, "name": "liquidificador", "price": 65.99},
    {"id": 27, "name": "furadeira", "price": 99.15},
    {"id": 28, "name": "ferro de passar", "price": 55.80},
    {"id": 29, "name": "coberta", "price": 55.99},
    {"id": 30, "name": "sofa", "price": 600.15}
]

@app.get("/products")
def get_products():
    """ Lista os produtos """

    return jsonify(produtos), 200

@app.get("/products/<id>")
def get_product(id: int):
    """ Mostra o produto com o mesmo id """
    
    id = int(id)
    product = dict()
    for item in produtos:
        if item["id"] == id:
            product = dict(item)

    if product == {}:
        return jsonify({"message": "ID não encontrado"}), 404

    return jsonify(product), 200

@app.post("/products")
def post_product():
    """ Insere um novo produto """

    last_prod = produtos[len(produtos)-1]
    data = dict(request.json)

    if not (data.get("name") and data.get("price")):
        return jsonify({"message": "Necessario name e price"}), 400

    data["id"] = last_prod["id"] + 1
    produtos.append(data)
    return jsonify(data), 201

@app.patch("/products/<id>")
def patch_product(id: int):
    """ Modificar o produto """

    id = int(id)
    data = dict(request.json)
    done = bool(False)
    for item in produtos:
        if item["id"] == id:
            item["name"] = data.get("name", item["name"])
            item["price"] = data.get("price", item["price"])
            done = bool(True)

    if done:
        return jsonify(), 204

    return jsonify({"message": "ID não encontrado"}), 404

@app.delete("/products/<id>")
def delete_product(id: int):
    """ Deletar o produto """

    id = int(id)
    index = 0
    is_found = bool(False)
    for item in produtos:
        if (item["id"] == id or is_found):
            is_found = bool(True)
        else:
            index += 1


    if is_found:
        produtos.pop(index)
        return jsonify(), 204

    return jsonify({"message": "ID não encontrado"}), 404