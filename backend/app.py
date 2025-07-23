from flask import Flask, jsonify
import psutil
import platform
import os
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    uptime_seconds = int(psutil.boot_time())
    uptime = timedelta(seconds=(psutil.time.time() - uptime_seconds))
    temperature = "N/A"

    try:
        temps = psutil.sensors_temperatures()
        if "coretemp" in temps:
            temperature = temps["coretemp"][0].current
    except Exception:
        pass

    return {
        "cpu_percent": cpu_percent,
        "memory_percent": memory.percent,
        "memory_used": round(memory.used / (1024 ** 3), 2),
        "memory_total": round(memory.total / (1024 ** 3), 2),
        "disk_percent": disk.percent,
        "disk_used": round(disk.used / (1024 ** 3), 2),
        "disk_total": round(disk.total / (1024 ** 3), 2),
        "uptime": str(uptime),
        "cpu_temp": temperature,
        "cpu_cores": psutil.cpu_count(logical=False),
        "hostname": platform.node(),
        "os": f"{platform.system()} {platform.release()}",
        "process_count": len(psutil.pids())
    }

@app.route("/api/stats", methods=["GET"])
def stats():
    return jsonify(get_system_info())

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Linux Monitor API is running."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
