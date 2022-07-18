import hashlib
from time import time
# from urlparse import urlparse
from urllib.parse import urlparse

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_data = []
        # Genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        # Creates a new block and adds it to the chain
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'data': self.current_data,
            'proof': proof,
            'hash' : self.hash(self.current_data,previous_hash or self.chain[-1]['hash']),
            'previous_hash': previous_hash or self.chain[-1]['hash']
        }
        self.current_data = []
        self.chain.append(block)
        return block

    def new_data(self, data):
        # Adds a new transaction to the list of transaction
        self.current_data.append(data)
        return self.last_block['index']+1

    @staticmethod
    def hash(data,previous_hash):
        # Hashes a Block
        block_string = str(data + [previous_hash]).encode()
        return hashlib.sha256(block_string).hexdigest()

    def pow(self):
        proof = 0
        data_pre_hash = self.hash(self.current_data, self.last_block['hash'])
        # Repeat while finding correct value
        while self.valid_proof(data_pre_hash, str(proof)) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(data_pre_hash, proof):
        guess = str(data_pre_hash + proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # If first four characters are 0000, return True
        return guess_hash[:4] == "0000"  # nonce

    @property
    def last_block(self):
        # Returns the last block in the chain
        return self.chain[-1]
