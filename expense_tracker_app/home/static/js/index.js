document.addEventListener('DOMContentLoaded', () => {
  async function fetchCategories() {
    const response = await fetch('http://127.0.0.1:8000/get_categories');
    if (!response.ok) {
      console.error('Error al obtener las categorías');
      return[];
    }
    return await response.json();
  }

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

  async function initChart() {
    try {
      const categories = await fetchCategories();
      const expensesData = await fetchExpenses();

      const labels = categories;
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
      new Chart(ctx, {
        type: 'pie',
        data: chartData
      });
    } catch (e) {
      console.error('Error al inicializar el gráfico: ', e);
    }
  };
  initChart();
});