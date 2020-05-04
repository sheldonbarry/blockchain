# A module to simulate a simple blockchain in Python
# Copyright (c) 2017 - 2020 Sheldon Barry

from hashlib import sha256
from datetime import datetime

class Block(object):
    """Methods and attributes for the Block class"""
    
    def __init__ (self, index, transaction, previousHash, difficulty): 
        """Constructor for Block object"""
        self.index = index
        self.transaction = transaction
        self.previousHash = previousHash
        self.difficulty = difficulty
        self.timestamp = datetime.now()
        self.nonce = 0
        self.hash = self.mineBlock()

    def __str__(self):
        """Return a string representation of the Block contents"""
        block_string = ''.join([
            "index:        " + str(self.index) + '\n',
            "timestamp:    " + str(self.timestamp) + '\n',
            "difficulty:   " + str(self.difficulty) + '\n',
            "nonce:        " + str(self.nonce) + '\n',
            "transaction:  " + str(self.transaction) + '\n',
            "previousHash: " + self.previousHash + '\n',
            "hash:         " + self.hash + '\n'
            ])
        return block_string

    def calculateHash(self):
        """Calculate a hash based on the Block contents and nonce value"""
        hash_string = ''.join([
            str(self.index), 
            str(self.timestamp), 
            str(self.nonce), 
            str(self.transaction), 
            self.previousHash
            ])
        return sha256(hash_string.encode('ascii')).hexdigest()
        
    def mineBlock(self):
        """Find a valid hash for the Block contents, based on difficulty"""
        while self.calculateHash()[:self.difficulty] != ('0' * self.difficulty):
            self.nonce += 1
        return self.calculateHash()


class Blockchain(object):
    """Methods and attributes for the Blockchain class"""
    
    def __init__(self, difficulty=4):
        """Constructor for the Blockchain object"""
        self.index = 0
        self.difficulty = difficulty
        # create Genesis Block on the chain of Blocks
        self.chain = [Block(self.index, 'Genesis Block', '0'*64, self.difficulty)]

    def addBlock(self,transaction):
        """Add a new block to the Blockchain"""
        self.index += 1
        newBlock = Block(self.index, transaction, self.getLastBlock().hash, self.difficulty)
        self.chain.append(newBlock)

    def getLastBlock(self):
        """Return the last block in the Blockchain"""
        return self.chain[-1]

    def checkChainValid(self):
        """Verify the integrity of the Blockchain"""
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False           
        return True


