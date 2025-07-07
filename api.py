from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "price": 10.99},
    {"id": 2, "name": "Item 2", "price": 12.99},
    {"id": 3, "name": "Item 3", "price": 15.99}
]
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# GET "List all items"
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"})

# POST "Create a new item"
@app.route("/items", methods=["POST"])
def create_item():
    new_item = request.json
    if not new_item or 'name' not in new_item or 'price' not in new_item:
        return jsonify({"error": "Invalid item data"}), 400
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# PUT "Update an existing item"
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_data = request.json
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    if 'name' in updated_data:
        item['name'] = updated_data['name']
    if 'price' in updated_data:
        item['price'] = updated_data['price']
    return jsonify(item)

# DELETE "Delete an item"
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):   
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 204





if __name__ == '__main__':
    app.run(debug=True)