import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask

class Blockchain(object):

    def __init__(self):
        self.current_transactions = []
        self.chain = []
        
        # Create the GENESIS BLOCK  
        self.new_block(previous_hash=1, proof=100)
       
    """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
    """
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        
        self.current_transactions = []
        self.chain.append(block)

        return block
        

    """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
    """
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        # index of block that will hold this transaction
        return self.last_block['index'] + 1

    """
        Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
    """
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
    """
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
    """
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"

    # Returns the last block in the chain
    @property
    def last_block(self):
        return self.chain[-1]

    # Instantiate Node
    app = Flask(__name__)

    # Generate a globally unique address for this node
    node_id = str(uuid4()).replace('-', '')

    # Instantiate Blockchain
    blockchain = Blockchain()

    @app.route('/mine', methods=['GET'])
    def mine():
        pass

    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        pass

    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

