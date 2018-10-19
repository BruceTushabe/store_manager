from flask import Flask, jsonify, request
app = Flask(__name__)

# Empty lists where products/Sales are to be POSTED OR GOT

products = []
sales = []    

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

# This is the END POINT for ADMIN/ATTENDANT can get all products 

@app.route('/api/v1/products', methods =['GET'])
def get_all():
    return jsonify({'products':products})

# END POINT for getting one specific product by id

@app.route('/api/v1/products/<int:id>', methods =['GET'])
def get_one(id):
    prods = [product for product in products if product['id'] == id]
    return jsonify({'product':prods[0]})

# A store attendant can add a sale order

@app.route('/api/v1/sales', methods = ['POST'])
def create_sale():

    sale_order = {
        'saleId': len(sales) +1,
        'attendant': request.json['attendant'],
        'cost': request.json['cost'],
        'total': int(request.json['quantity']) * int(request.json['cost'])
    }

    sales.append(sale_order)
    return jsonify({'sale_order':sale_order})

# END POINT for a Admin get all sale order records

@app.route('/api/v1/sales', methods = ['GET'])
def sale_records():
    return jsonify({'sale_records':sales})









if __name__ == '__main__':
    app.run(debug=True)    