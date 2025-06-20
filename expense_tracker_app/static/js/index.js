import { actualizarTabla } from './update_dom.js';

document.addEventListener('DOMContentLoaded', () => {

  let chartInstance = null;
  let currentGroupedBy = "";

  async function fetchExpenses(groupedBy) {
    let url = "http://127.0.0.1:8000/index";
    if (groupedBy) {
      url += `?groupedBy=${groupedBy}`;
    }
    const response = await fetch(url, {
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    });
    if (!response.ok) {
      console.error('Error al obtener los datos de las expenses');
      return [];
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

  async function initChart(type, groupedBy) {
    try {
      const expensesData = await fetchExpenses(groupedBy);
      console.log(expensesData);
      try {
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
    } catch (e) {
      console.error('Error al fetch de datos', e);
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

  async function actualizarTablaYGrafico(groupedBy) {
  // Actualiza la tabla
  await actualizarTabla(groupedBy);
  // Actualiza el gráfico (usa el tipo actual, por ejemplo 'pie')
  initChart('pie', groupedBy);
  }

  const groupData = document.getElementById("Grouped");
  groupData.addEventListener('change', () => {
    let value = groupData.value;
    currentGroupedBy = value;
    actualizarTablaYGrafico(currentGroupedBy);
  });
});
