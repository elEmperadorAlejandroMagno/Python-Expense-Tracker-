export async function actualizarTabla(groupedBy) {
  let url = 'http://127.0.0.1:8000/index';
  if (groupedBy) {
    url += `?groupedBy=${groupedBy}`;
  }
  const response = await fetch(url, {
    headers: {
      'X-Requested-With': 'XMLHttpRequest'
    }
  });
  if (!response.ok) {
    console.error('Error al obtener los datos de la tabla');
    return;
  }
  const data = await response.json();

  // Suponiendo que tienes un tbody con id="tablaCuerpo"
  const tbody = document.getElementById('tablaCuerpo');
  tbody.innerHTML = '';
  data.forEach(expense => {
    const row = `<tr>
      <td>${expense.categoria}</td>
      <td>${expense.total_expenses}</td>
      <!-- ...otros campos... -->
    </tr>`;
    tbody.innerHTML += row;
  });
}
