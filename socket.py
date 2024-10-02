from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
abi = json.loads('[{"inputs":[{"internalType":"string","name":"ip","type":"string"}],"name":"blockIP","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"ip","type":"string"}],"name":"isBlocked","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"ip","type":"string"}],"name":"IPBlocked","type":"event"}]')
bytecode = '0x608060405234801561001057600080fd5b506105a3806100206000396000f3fe60806040526004361061003f5760003560e01c8063b3f4fdf114610044578063d0e30db01461006b575b600080fd5b61004c600480360381019061004791906100e8565b61007a565b60405161005991906100ff565b60405180910390f35b6100626100b0565b60405161006f91906100ff565b60405180910390f35b60008054905090565b8060008190555050565b600081359050610087816100e1565b92915050565b6000602082840312156100a05761009f6100a8565b5b60006100ae8482850161007c565b91505092915050565b6100bc816100c3565b82525050565b60006020820190506100d760008301846100b3565b92915050565b60006100e8826100c3565b91506100f3836100c3565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115610124576101236100c3565b5b828201905092915050565b600061013f8261012e6100c3565b915061014a8361012e6100c3565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0382111561017a576101796100c3565b5b828204905092915050565b600061019e8261012e6100c3565b91506101a98361012e6100c3565b9250828210156101c2576101c16100c3565b5b82820390509291505056fea2646970667358221220c3b3d7c1f8e4c6f7a8d2d7b6d3e8f7c6e5d4c3b2a1f0e9d8c7b6a5d4c3b2a1f64736f6c63430008070033'
acct = w3.eth.accounts[0]
SecurityContract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = SecurityContract.constructor().transact({'from': acct, 'gas': 3000000})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
