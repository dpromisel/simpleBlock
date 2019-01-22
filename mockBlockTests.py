import unittest
from blockchain_solution import Transaction, Block, Blockchain


blockchain = Blockchain()
genesis_block = blockchain.chain[0]
last_block = blockchain.last_block
new_block1 = Block(index=last_block.index + 1,
				data=blockchain.unconfirmed_transactions,
				previous_hash=last_block.compute_hash())

class TestMockBlock(unittest.TestCase):

    def test_genesis(self):
        self.assertEqual(genesis_block.index,0)
        self.assertEqual(genesis_block.previous_hash,0)
        self.assertEqual(blockchain.chain[0],genesis_block)

    def test_transaction(self):
        #test transaction is successfully added by checking if the students
        #method adds the transaction and a block with the transaction
        new_tx = Transaction("A","B",10).toDict()
        self.assertEqual(new_tx,blockchain.new_transaction("A","B",10))
        self.assertEqual(blockchain.unconfirmed_transactions[0],new_tx);

    def test_mine(self):
        new_block = blockchain.mine()
        self.assertEqual(new_block,blockchain.chain[-1])
        self.assertEqual(blockchain.unconfirmed_transactions,[])

    def test_proof_of_work(self):
        comp_hash = blockchain.proof_of_work(new_block1)
        assert comp_hash.startswith('0' * blockchain.difficulty)

    def test_add_block(self):
        boolean_true = blockchain.add_block(new_block1)
        off_chain_block = Block(index=22,data=[],previous_hash=-99)
        boolean_false = blockchain.add_block(off_chain_block)
        self.assertEqual(new_block1,blockchain.chain[-1])
        self.assertEqual(boolean_true,True)
        self.assertEqual(boolean_false,False)

    def test_check_integrity(self):
        assert blockchain.check_integrity

if __name__ == '__main__':
    unittest.main()
