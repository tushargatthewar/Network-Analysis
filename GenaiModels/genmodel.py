from flask import Flask, jsonify
import threading
import time
import torch
import torch.nn as nn
import torch.optim as optim
from web3 import Web3
import json
import random

app = Flask(__name__)
alerts = []

class GenAI(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(GenAI, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = GenAI(10, 5, 10)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.MSELoss()
x = torch.randn((100, 10))
y = torch.randn((100, 10))
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(x)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
abi = json.loads('[{"inputs":[{"internalType":"string","name":"ip","type":"string"}],"name":"blockIP","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"ip","type":"string"}],"name":"isBlocked","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"ip","type":"string"}],"name":"IPBlocked","type":"event"}]')
contract_address = contract.address
contract = w3.eth.contract(address=contract_address, abi=abi)
acct = w3.eth.accounts[0]

def get_data_from_blockchain():
    event_filter = contract.events.IPBlocked.createFilter(fromBlock='latest')
    while True:
        for event in event_filter.get_new_entries():
            ip = event['args']['ip']
            alerts.append({'ip': ip, 'action': 'Blocked'})
            print(f"IP {ip} blocked.")
        time.sleep(2)

def detect_anomalies(data):
    input_tensor = torch.tensor(data, dtype=torch.float).unsqueeze(0)
    output = model(input_tensor)
    loss = criterion(output, input_tensor)
    return loss.item()

def generate_report(data, score):
    report = {
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        'data': data,
        'score': score,
        'status': 'ALERT' if score > 1.0 else 'Normal'
    }
    if score > 1.0:
        ip = "192.168.1.100"
        tx_hash = contract.functions.blockIP(ip).transact({'from': acct, 'gas': 200000})
        w3.eth.wait_for_transaction_receipt(tx_hash)
    alerts.append(report)
    print(report)

def process_data(data):
    score = detect_anomalies(data)
    generate_report(data, score)

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts)

def run_flask():
    app.run(port=5000)

threading.Thread(target=run_flask).start()
threading.Thread(target=get_data_from_blockchain).start()
while True:
    data = [random.random() for _ in range(10)]
    process_data(data)
    time.sleep(5)
