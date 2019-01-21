from time import time
import datetime
import hashlib as hasher

class Transaction:

	def __init__(self, sender, recipient, value):
		self.sender = sender
		self.recipient = recipient
		self.value = value

	def toDict(self):
		return {
			'sender': self.sender,
			'recipient': self.recipient,
			'value': self.value
		}

	def __str__(self):
		toString = self.sender + " -> " + self.recipient + " (" + self.value + ") "
		return toString;

class Block:
	def __init__(self, index, data, previous_hash):
		#TODO: Block initializer

	def compute_hash(self):
		sha = hasher.sha256()

		sha.update(str(self.index) +
			str(self.timestamp) +
			str(self.previous_hash) +
			str(self.data) +
			str(self.nonce));

		return sha.hexdigest()

	def __str__(self):
		toString =  str(self.index) + "\t" + str(self.timestamp) +"\t\t" + str(self.previous_hash) + "\n"
		for tx in self.data:
			toString +=  "\t" + str(tx) + "\n"
		return toString;

class Blockchain:
	def __init__(self):
		#TODO: implement Blockchain class initializer

	def create_genesis_block(self):
		"""
		A function to generate the genesis block and appends it to the chain.
		The genesis block has index 0, previous_has of 0, and a valid hash
		"""

		#TODO: implement creating a new genesis block

	def new_transaction(self, sender, recipient, value):
		#TODO: implement adding new transactions
		return 0;

	def mine(self):
		"""
		This function serves as an interface to add the pending
		transactions to the blockchain by adding them to the block
		and figuring out Proof of Work.
		"""
		#TODO: implement mining
		return 0

	def proof_of_work(self, block):
		"""
		Function that tries different values of nonce to get a hash
		that satisfies our difficulty criteria.
		"""
		#TODO: implement proof of work
		return 0;

	def add_block(self, block):
		"""
		A function that adds the block to the chain after verification.
		"""
		#TODO: implement adding a block to a chain
		return 0

	def check_integrity(self):
		"""
		a function that checks the intergrity of the blockchain
			- each block in the chain holds the hash of the previous block
			- the genesis block has index 0 and previous hash of 0
		"""
		previous_hash = 0;
		index = 0;

		for block in self.chain:
			if block.index != index:
				return False
			if block.previous_hash != previous_hash:
				return False;

			previous_hash = block.compute_hash();
			index = index + 1;

		return True;


	@property
	def last_block(self):
		return self.chain[-1]

def timestamp_to_string(epoch_time):
	return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')
