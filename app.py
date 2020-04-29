from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route("/ping")
def ping():
    return jsonify({'message':'pong!'})

@app.route("/products")
def getproducts():
    return jsonify({"Products":products,"message":"List's Products"})

@app.route("/products/<string:product_name>")
def getproduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound)>0):
        return jsonify({"Product":productsFound[0]})
    else: 
        return jsonify({"message":"No se encontro este producto"})

@app.route("/products", methods = ['POST'])
def addPrducts():
    new_product = {
        "name" : request.json['name'],
        "price" : request.json['price'],
        "quantity" : request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"nessage":"Product Added Succefuly","products":products})

@app.route("/products/<string:product_name>", methods = ['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound)>0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['identity'] = request.json['quantity']
        return jsonify({

            "Message": "Product Updated",
            "pruduct" : productFound[0]
        })
    return jsonify({"Product not Found"})

@app.route("/products/<string:product_name>", methods = ['DELETE'])
def deleteproduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({"New list of Products":products})
    return jsonify({"message":"Product not Found"})



if __name__=="__main__":
    app.run(debug=True, port=4000)

