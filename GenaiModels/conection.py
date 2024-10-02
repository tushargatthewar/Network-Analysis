import subprocess
from web3 import Web3
import json
import time

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
abi = json.loads('[{"inputs":[{"internalType":"string","name":"ip","type":"string"}],"name":"blockIP","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"ip","type":"string"}],"name":"isBlocked","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"ip","type":"string"}],"name":"IPBlocked","type":"event"}]')
contract_address = '0x...' 
contract = w3.eth.contract(address=contract_address, abi=abi)
acct = w3.eth.accounts[0]

def run_nmap(target):
    result = subprocess.run(['nmap', '-sS', '-p-', target], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def parse_nmap_output(output):
    lines = output.split('\n')
    open_ports = []
    for line in lines:
        if '/tcp' in line and 'open' in line:
            port = line.split('/tcp')[0]
            open_ports.append(port)
    return open_ports

def main():
    target_ip = '192.168.1.100'
    while True:
        output = run_nmap(target_ip)
        open_ports = parse_nmap_output(output)
        if len(open_ports) > 3:
            tx_hash = contract.functions.blockIP(target_ip).transact({'from': acct, 'gas': 200000})
            w3.eth.wait_for_transaction_receipt(tx_hash)
            print(f"Blocked IP {target_ip} due to open ports: {open_ports}")
        time.sleep(300)

if __name__ == "__main__":
    main()
