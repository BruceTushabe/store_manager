from flask import Flask, jsonify, request
app = Flask(__name__)


products = []
sale = []    

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    product = {
        'id': len(products)+1,
        'name': request.json['name'],
        'price':  request.json['price'],
        'quantity':request.json['quantity'],
        'category':request.json['category']
        }

    products.append(product)
    return jsonify({'product': product})





if __name__ == '__main__':
    app.run(debug=True)    