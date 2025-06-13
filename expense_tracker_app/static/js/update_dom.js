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
  if (data) {
    data.forEach(expense => {
      const row = `<tr>
        <td>${expense.categoria}</td>
        <td>${expense.books_quantity }</td>
        <td>${formatCurrency(expense.total_expenses)}</td>
      </tr>`;
      tbody.innerHTML += row;
    });
  } else {
    const notFoundh4 = `
    <tr>
      <td colspan="3" style="text-align: center;">No se ha podido obtener los datos</td>
    </tr>
    `;
    tbody.innerHTML += notFoundh4;
  }
}

function formatCurrency(int) {
  return `$${Number(int).toFixed(2)}`;
}
