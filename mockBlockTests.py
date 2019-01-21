import unittest
from blockchain import Blockchain

class TestMockBlock(unittest.TestCase):
    def setUp(self):
        blockchain = Blockchain()
        self.genesis_block = create_genesis_block()
        self.new_block1 = Block(index=last_block.index + 1,
						data=self.unconfirmed_transactions,
						previous_hash=last_block.compute_hash())
        # self.new_block2 = Block(index=last_block.index + 1,
        #                 data=self.unconfirmed_transactions,
        #                 previous_hash=last_block.compute_hash())

    def test_genesis(self):
        self.assertEqual(genesis_block.index,0)
        self.assertEqual(genesis_block.previous_hash,0)
        self.assertEqual(self.chain[0],genesis_block)

    def test_transaction(self):
        #test transaction is successfully added by checking if the students
        #method adds the transaction and a block with the transaction
        new_tx = Transaction(A,B,10).toDict()
        self.assertEqual(new_tx,new_transaction(A,B,10))
        self.assertEqual(self.unconfirmed_transactions[0],new_tx);

    def test_mine(self):
        new_block = mine()
        self.assertEqual(new_block,self.chain[-1])
        self.assertEqual(self.unconfirmed_transactions,False)

    def test_proof_of_work(self):
        comp_hash = proof_of_work(new_block1)
        assert comp_hash.startswith('0' * self.difficulty)

    def test_add_block(self):
        boolean_true = add_block(new_block1)
        off_chain_block = Block(index=22,data=[],previous_hash=-99)
        boolean_false = add_block(off_chain_block)
        self.assertEqual(new_block1,chain[-1])
        self.assertEqual(boolean_true,True)
        self.assertEqual(boolean_false,False)

    def my_check_integrity(self):
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

    def test_check_integrity(self):
        self.assertEqual(self.check_integrity,self.my_check_integrity)

    def tearDown(self):
        self.genesis_block.dispose()
        self.genesis_block = None
        self.new_block1.dispose()
        self.new_block1 = None


if __name__ == '__main__':
    unittest.main()
