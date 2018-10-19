from flask import Flask, jsonify, request
app = Flask(__name__)

# Empty lists where products/Sales are to be POSTED OR GOT

products = []
sale = []    

# Creating the END POINT for ADMIN can add a product
 
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