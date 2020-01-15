class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    # Creates a new block and adds it to the chain
    def new_block(self):
        pass

    # Adds a new transaction to the list of transactions
    def new_transaction(self):
        pass

    # Hashes a Block
    @staticmethod
    def hash(block):
        pass

    # Returns the last block in the chain
    @property
    def last_block(self):
        pass
