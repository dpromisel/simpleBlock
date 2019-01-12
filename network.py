from flask import Flask, request, render_template, jsonify, redirect
from blockchain import Blockchain

app =  Flask(__name__)

# the node's copy of blockchain
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/new_transaction', methods=['POST'])
def new_transaction():
	sender = request.form["sender"]
	recipient = request.form["recipient"]
	value = request.form["value"]

	blockchain.new_transaction(sender, recipient, value);

	return redirect('/')

@app.route('/pending_tx')
def get_pending_tx():
	transactions = blockchain.unconfirmed_transactions
	
	response = {'transactions': transactions}
	return jsonify(response), 200

@app.route('/mine', methods=['GET'])
def mine_unconfirmed_transactions():
	result = blockchain.mine()
	if not result:
		return "No transactions to mine"
	return "Block #{} is mined.".format(result)

app.run(debug=True, port=8000)
