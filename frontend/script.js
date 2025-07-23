async function fetchStats() {
  const res = await fetch('http://localhost:5001/api/stats');
  const data = await res.json();
  return data;
}

function renderSystemInfo(data) {
  const ul = document.getElementById("systemInfo");
  ul.innerHTML = `
    <li><strong>Hostname:</strong> ${data.hostname}</li>
    <li><strong>OS:</strong> ${data.os}</li>
    <li><strong>Uptime:</strong> ${data.uptime}</li>
    <li><strong>CPU Cores:</strong> ${data.cpu_cores}</li>
    <li><strong>CPU Temp:</strong> ${data.cpu_temp} °C</li>
    <li><strong>Processes:</strong> ${data.process_count}</li>
  `;
}

function createChart(ctx, label, used, total, color) {
  return new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Used', 'Free'],
      datasets: [{
        label,
        data: [used, total - used],
        backgroundColor: [color, '#2d3748']
      }]
    },
    options: {
      responsive: true,
      cutout: '70%'
    }
  });
}

async function setupDashboard() {
  const data = await fetchStats();
  renderSystemInfo(data);

  createChart(document.getElementById('cpuChart'), 'CPU', data.cpu_percent, 100, '#4fd1c5');
  createChart(document.getElementById('memoryChart'), 'Memory', data.memory_used, data.memory_total, '#63b3ed');
  createChart(document.getElementById('diskChart'), 'Disk', data.disk_used, data.disk_total, '#f6ad55');
}

setupDashboard();
