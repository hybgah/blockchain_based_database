from flask import Flask, request, jsonify, render_template
from uuid import uuid4
from werkzeug.utils import secure_filename
import csv

# Our blockchain.py API
from blockchain import Blockchain

block_db = Blockchain()

app = Flask(__name__)
# Universal Unique Identifier
# To identify nodes
node_identifier = str(uuid4()).replace('-', '')

app.config['UPLOAD_FOLDER'] = 'path/to/the/file'


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': block_db.chain,  # print block_db
        'length': len(block_db.chain)
    }
    return jsonify(response), 200

@app.route('/upload_csv')
def upload_csv():
    return render_template('upload_csv.html')


@app.route('/upload_form', methods=['POST','GET'])
def upload_form():
    return render_template('upload_form.html')


@app.route('/update_form',methods=['POST'])
def update_form():
    data = request.form['content']
    return f"Your data will be added to block index:{block_db.new_data(data)}."

@app.route('/update_csv',methods=['POST'])
def update_csv():
    if request.files:
        uploaded_file = request.files['csv_file']
        uploaded_file.save(secure_filename(uploaded_file.filename))
        with open(f'{uploaded_file.filename}') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                block_db.new_data(row)
                if len(block_db.current_data) >= 5:
                    proof = block_db.pow()
                    block = block_db.new_block(proof)
        return "File Readed"
    else:
        return "Nothing Included"

@app.route('/mine', methods=['GET'])
def mine():
    proof = block_db.pow()
    # Forge the new Block by adding it to the chain
    block = block_db.new_block(proof)
    response = {
        'message': 'new block found',
        'index': block['index'],
        'data': block['data'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
