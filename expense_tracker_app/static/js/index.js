document.addEventListener('DOMContentLoaded', () => {
  let chartInstance = null;

  async function fetchExpenses() {
    const response = await fetch('http://127.0.0.1:8000/get_distribution_expenses');
    if (!response.ok) {
      console.error('Error al obtener los datos de las expenses');
      return[];
    }
    return await response.json();
  }

  function generateUniqueColors(count) {
    const colors = new Set();
    while(colors.size < count) {
      const r = Math.floor(Math.random() * 256);
      const g = Math.floor(Math.random() * 256);
      const b = Math.floor(Math.random() * 256);
      
      const color = `rgb(${r},${g},${b})`;
      colors.add(color); 
    }
    return Array.from(colors);
  }

  async function initChart(type) {
    try {
      const expensesData = await fetchExpenses();

      const labels = expensesData.map(expense => expense.category);
      const data = expensesData.map(expense => expense.total_expenses);
      const backgroundColors = generateUniqueColors(labels.length);

      const chartData = {
        labels: labels,
        datasets: [{
          label: 'Expense Distribution',
          data: data,
          backgroundColor: backgroundColors,
          hoverOffset: 4
        }]
      };

      const ctx = document.getElementById('myChart');

      if(chartInstance) {
        chartInstance.destroy();
      }

      chartInstance = new Chart(ctx, {
        type: type,
        data: chartData
      });
    } catch (e) {
      console.error('Error al inicializar el gráfico: ', e);
    }
  };

  initChart('pie');

  const pieChart = document.getElementById("PieChart");
  const barsChart = document.getElementById("BarChart");

  pieChart.addEventListener('click', () => {
    initChart('pie');
  })
  barsChart.addEventListener('click', () => {
    initChart('bar');
  })

  const groupData = document.getElementById("Grouped");
  groupData.addEventListener('change', () => {
    let value = groupData.value;
    window.location.href = `http://127.0.0.1:8000/index?groupedBy=${value}`;
  })
});