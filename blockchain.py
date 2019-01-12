from time import time
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

		self.index = index
		self.timestamp = time()
		self.previous_hash = previous_hash
		self.data = data
		self.nonce = 0

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
		#difficulty of PoW algorithm
		self.difficulty = 2

		self.unconfirmed_transactions = []
		self.chain = []

		self.create_genesis_block();

	def create_genesis_block(self):
		"""
		A function to generate the genesis block and appends it to the chain.
		The genesis block has index 0, previous_has of 0, and a valid hash
		"""

		genesis_block = Block(index=0, data=[], previous_hash=0);
		self.chain.append(genesis_block);

	def new_transaction(self, sender, recipient, value):
		new_tx = Transaction(sender, recipient, value).toDict();
		self.unconfirmed_transactions.append(new_tx);
		return new_tx;

	def mine(self):
		"""
		This function serves as an interface to add the pending
		transactions to the blockchain by adding them to the block
		and figuring out Proof of Work.
		"""
		last_block = self.last_block
		new_block = Block(index=last_block.index + 1,
						data=self.unconfirmed_transactions,
						previous_hash=last_block.compute_hash())
		proof = self.proof_of_work(new_block)
		self.add_block(new_block)
		self.unconfirmed_transactions = []
		return new_block

	def proof_of_work(self, block):
		"""
		Function that tries different values of nonce to get a hash
		that satisfies our difficulty criteria.
		"""
		computed_hash = block.compute_hash()
		while not computed_hash.startswith('0' * self.difficulty):
			block.nonce += 1
			computed_hash = block.compute_hash()
		return computed_hash;

	def add_block(self, block):
		"""
		A function that adds the block to the chain after verification.
		"""
		last_block = self.last_block
		previous_hash = last_block.compute_hash()
		if previous_hash != block.previous_hash:
			return False
		self.chain.append(block)
		return True

	def check_integrity(self):
		"""
		a function that checks the intergrity of the blockchain
			- each block in the chain holds the hash of the previous block
			- the genesis block has index 0 and previous hash of 0
		"""
		previous_hash = 0;
		index = 0;

		for block in chain:
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

