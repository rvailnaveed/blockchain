import hashlib
import json
from time import time

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    # Creates a new block and adds it to the chain
    def new_block(self):
        pass

    # Adds a new transaction to the list of transactions
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        # index of block that will hold this transaction
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        pass

    # Returns the last block in the chain
    @property
    def last_block(self):
        pass
