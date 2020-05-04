import blockchain

# initialise Blockchain with difficulty of 4
myCoin = blockchain.Blockchain(4)

# print Genesis Block contents
print(str(myCoin.chain[0]) + '\n')

transactions = [
    {'Sender':'abc@example.com', 'Beneficiary':'xyz@example.com', 'Amount':4}, 
    {'Sender':'def@example.com', 'Beneficiary':'ghi@example.com', 'Amount':10},  
    {'Sender':'jkl@example.com', 'Beneficiary':'pqr@example.com', 'Amount':8}
    ]

# process transactions each in a new block and print mined block contents
for transaction in transactions:
    myCoin.addBlock(transaction)
    print(myCoin.chain[-1])
    print

# Check if chain is valid (should return true)
print('Blockchain integrity is valid? ' + str(myCoin.checkChainValid()))

# Now let's manipulate the data to invalidate the Blockchain
myCoin.chain[1].transaction = {'Sender':'abc@example.com', 'Beneficiary':'def@example.com', 'Amount':12}
# even if we update the hash to the new transaction, validity will still fail
#myCoin.chain[1].hash = myCoin.chain[1].mineBlock()

# Check our chain again (should return false)
print('Blockchain integrity is valid? ' + str(myCoin.checkChainValid()))
print