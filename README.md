
---

### ✅ `README.md`

```md
# 🖥️ Linux System Monitor Dashboard

A beautiful, responsive system dashboard to monitor your Linux server's performance in real-time — built with **HTML**, **Tailwind CSS**, **Chart.js**, and a **Flask backend**. It supports standalone mode or can be deployed easily using Docker.

---

## 📌 Project Overview

This lightweight dashboard displays real-time server statistics:

- ✅ CPU Usage
- ✅ Memory Usage
- ✅ Disk Usage
- ✅ Uptime, OS info, Process count
- ✅ Temperature (if available)

Built for Linux systems, and perfect for both local monitoring or deploying on a remote server.

---

## 📂 Project Structure

```

linux-monitor-dashboard/
├── backend/
│   ├── app.py              # Flask API
│   └── requirements.txt    # Python dependencies
│
├── frontend/
│   ├── index.html          # Dashboard UI
│   ├── script.js           # Chart rendering + API fetching
│   └── style.css           # Optional extra styles (or Tailwind via CDN)
│
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Optional for multi-container setup
└── README.md

````

---

## 📥 Clone the Repository

```bash
git clone https://github.com/Ravindulakmina/Linux-monitor-dashboard.git
cd linux-monitor-dashboard
````

---

## ⚙️ Run Locally (Without Docker)

### 🧠 Backend Setup (Flask API)

```bash
# Go to the backend folder
cd backend

# Create virtual environment (Mac/Linux)
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

> Flask server will run on `http://localhost:5000` or similar.

---

### 🎨 Frontend Setup (HTML + JS)

In a **new terminal tab/window**:

```bash
cd frontend

# Run simple HTTP server (Python 3)
python3 -m http.server 8080
```

> Open browser at: `http://localhost:8080`

---

## 🐳 Run with Docker (Recommended)

Make sure Docker is installed on your system.

### Step 1: Build Docker Image

```bash
docker build -t linux-dashboard .
```

### Step 2: Run the Container

```bash
docker run -d -p 5000:5000 --name dashboard linux-dashboard
```

### Step 3: Serve Frontend Separately (Optional)

```bash
cd frontend
python3 -m http.server 8080
```

Now open:
➡️ `http://localhost:8080` → Loads HTML
➡️ HTML fetches stats from: `http://localhost:5000/api/stats`

---

## 🚀 Deploy on Remote Linux Server with Docker

1. SSH into your server.
2. Clone this repository or upload project files.
3. Run the following:

```bash
docker build -t linux-dashboard .
docker run -d -p 5000:5000 --name dashboard linux-dashboard
```

4. Allow the firewall port:

```bash
sudo ufw allow 5000
```

5. Serve the frontend (`index.html`) via NGINX, Apache or Python HTTP server:

```bash
cd frontend
python3 -m http.server 80
```

6. Access via browser:

```
http://<your-server-ip>/
```

Make sure `script.js` points to your Flask API:

```js
const res = await fetch('http://<your-server-ip>:5000/api/stats');
```

---

## 🧾 requirements.txt

Save this file under `/backend/requirements.txt`

```txt
flask
psutil
flask-cors
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🌐 Example Usage

Once everything is running:

* Flask API: `http://localhost:5000/api/stats`
* Frontend: `http://localhost:8080` (locally)
* Remote: `http://<server-ip>`

---

## 🧑‍💻 Author

* **Ravindu Lakmina** – [GitHub](https://github.com/Ravindulakmina)

---

## 📃 License

This project is licensed under the MIT License.

---

## 🙏 Feedback

Found a bug? Have an idea? Feel free to [open an issue](https://github.com/Ravindulakmina/Linux-monitor-dashboard/issues) or contribute via pull request!

```

---

🎁 **Extra Tips**:

- Want to bundle frontend + backend in a single Docker container? I can update the Dockerfile and give you `nginx + flask` in one container.
- If you deploy on a VPS, ensure ports `80` (frontend) and `5000` (backend API) are open.


```
