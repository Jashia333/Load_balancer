# Load_balancer
🔁 Python Load Balancer (Mini Project)
This project implements a simple round-robin load balancer in Python on port 9000, which distributes traffic across three HTTP backend servers running on ports 9001, 9002, and 9003.

Each backend serves its own unique index.html file with distinct server identification and background color.

📁 Project Structure
pgsql
Copy
Edit
Load_balancer/
│
├── load_balancer.py          # Load balancer listening on port 9000
├── server.py                 # Simple HTTP server for backend nodes
├── sites/
│   ├── server_1/
│   │   └── index.html        # Blue background – Server 1
│   ├── server_2/
│   │   └── index.html        # Green background – Server 2
│   └── server_3/
│       └── index.html        # Coral background – Server 3
└── README.md                 # Project documentation
🚀 How to Run
1. Start Backend Servers
Open three separate terminals and run the following:

bash
Copy
Edit
python server.py 9001 sites/server_1
python server.py 9002 sites/server_2
python server.py 9003 sites/server_3
Each will serve its own index.html page.

2. Start the Load Balancer
In a new terminal:

bash
Copy
Edit
python load_balancer.py
This starts the load balancer on port 9000.

🌐 Test It
Open your browser and go to:

arduino
Copy
Edit
http://localhost:9000/
Each refresh will cycle between the three backend servers:

Server 1 (light blue)

Server 2 (light green)

Server 3 (light coral)

🛠 Technologies Used
Python Standard Library

http.server and socketserver for backend HTTP servers

http.client and BaseHTTPRequestHandler for load balancer

Round-robin logic using itertools.cycle

📚 Learning Goals
This mini project is designed to demonstrate:

Basic concepts of load balancing

HTTP protocol flow in Python

Using multiple backend servers

Simple round-robin request forwarding

📌 Future Improvements
Health checks for backends

Threaded or asynchronous request handling

Logging and analytics

Support for POST requests

Dockerized setup

👤 Author
Name: Jashia333

GitHub: github.com/Jashia333