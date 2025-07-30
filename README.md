# 🔁 Python Load Balancer (Mini Project)

This project demonstrates a simple **round-robin load balancer** written in Python. The load balancer listens on **port 9000** and distributes incoming HTTP requests across **three backend servers** running on ports **9001**, **9002**, and **9003**.

Each backend server serves a unique `index.html` page with a different background color and server name, making it easy to visualize load balancing in action.

---

## 📁 Project Structure

- `load_balancer.py`: Implements the round-robin load balancer.
- `server.py`: Launches a basic HTTP server serving files from a specified directory.
- `sites/server_1`, `sites/server_2`, `sites/server_3`: Contain individual HTML files for each server.

---

## 🚀 How to Run

1. **Start the Backend Servers**  
   Open three terminals and run each server on ports `9001`, `9002`, and `9003` using `server.py`.

2. **Start the Load Balancer**  
   In a separate terminal, run `load_balancer.py`. This starts the balancer on `http://localhost:9000`.

3. **Test the Setup**  
   Open your browser and visit `http://localhost:9000`. Refreshing the page will cycle through the three backend servers.

---

## 🛠 Technologies Used

- Python Standard Library
  - `http.server`
  - `socketserver`
  - `http.client`
  - `itertools`

No external libraries or frameworks are required.

---

## 📌 Future Enhancements

- Health checks for backend servers
- Logging and performance tracking
- Support for POST and other HTTP methods
- Docker containerization for easier deployment

---

## 👤 Author

**Name**: Jashia333  
**GitHub**: [https://github.com/Jashia333](https://github.com/Jashia333)

---

Feel free to fork this repo, suggest improvements, or use it as a starting point for more advanced networking and load balancing projects.
