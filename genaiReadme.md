Blockchain-based AI-Powered Intrusion Detection and Prevention System
Overview
This project implements a Blockchain-based AI-Powered Intrusion Detection and Prevention System designed to enhance network security. By leveraging blockchain technology for immutable tracking of security threats and AI-based anomaly detection, the system is capable of detecting and preventing attacks in real time. The system integrates several components that work together to provide robust security, including:

AI-driven anomaly detection to monitor network activity and detect potential threats.
Blockchain smart contracts to track and block suspicious IPs and ensure the integrity of the threat response.
Real-time reporting and alert system that notifies administrators of security events.
Nmap scanning for network vulnerabilities and open ports, with automated response mechanisms to prevent potential attacks.
Features
AI-Powered Threat Detection:

Uses a neural network model to detect anomalous behavior in network traffic.
Automatically flags abnormal patterns and generates a security score.
Blockchain Integration:

Smart contracts on the blockchain maintain a record of blocked IP addresses.
Prevents unauthorized access by blocking IPs found to be malicious or attempting to exploit vulnerabilities.
Automated Defense Mechanism:

When an anomaly is detected, the system blocks the offending IP using a blockchain smart contract.
Nmap scanning is used to identify open ports and potential vulnerabilities in the network. If suspicious activity is detected, the system automatically updates the smart contract to block the attacker.
Real-Time Alerts and Reporting:

Provides real-time notifications through a Flask-based server, displaying alerts on a web interface.
Continuous updates of the detected anomalies and blocked IPs for administrative monitoring.
Blockchain-backed Transparency:

The use of blockchain ensures transparency and traceability for all blocked IPs, providing an immutable history of actions taken by the system.
Architecture
Data Collection:

Data is collected from the network and blockchain for anomaly detection.
Nmap scans the network periodically to identify vulnerabilities.
AI Model:

The AI model processes the incoming network data and determines whether it deviates from normal behavior.
If the AI detects an anomaly, it flags the data for further action.
Smart Contract Interaction:

When an anomaly is detected, the system interacts with the blockchain smart contract to block the offending IP.
Alert and Reporting:

The Flask server generates real-time alerts and provides a user-friendly dashboard where administrators can monitor threats, blocked IPs, and security statuses.
Components
Blockchain Smart Contract:

The smart contract is deployed on a local Ethereum blockchain (Ganache) and is responsible for maintaining a list of blocked IPs.
AI Model:

A PyTorch-based neural network model is used to detect anomalies in network traffic data.
Nmap Scanning:

Regular Nmap scans are used to detect network vulnerabilities. If multiple open ports are detected, the system flags the IP and automatically adds it to the blockchain's blocked IP list.
Flask Web Application:

A simple Flask web server to display alerts and generate reports in real-time. The application presents the current list of detected anomalies, blocked IPs, and other relevant security events.
Getting Started
Prerequisites
Python 3.8+
Solidity (for blockchain smart contracts)
Ganache CLI or Ganache GUI (local Ethereum blockchain)
Truffle (for smart contract deployment)
Web3.py (Python library for interacting with Ethereum blockchain)
PyTorch (for AI model)
Flask (for web application)
Nmap (for network scanning)
Installation


git clone https://github.com/your-repo/blockchain-ai-intrusion-system.git
cd blockchain-ai-intrusion-system


pip install -r requirements.txt


truffle migrate


python app.py


python ai_nmap_service.py


Future Enhancements
Machine Learning Model Improvement: Implement more sophisticated ML models to improve anomaly detection accuracy.
Distributed Ledger Integration: Expand the system to use a decentralized ledger for added security.
Advanced Threat Analysis: Incorporate advanced methods such as deep packet inspection for more granular threat detection.