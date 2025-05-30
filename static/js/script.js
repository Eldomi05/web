let contadorNotas = 1;

function agregarNota() {
    const container = document.getElementById('notas-contenedor');
    
    const div = document.createElement('div');
    div.className = 'nota-peso';

    div.innerHTML = `
        <label for="nota${contadorNotas}">Nota ${contadorNotas}:</label>
        <input type="number" id="nota${contadorNotas}" name="nota${contadorNotas}" step="any" required>

        <label for="peso${contadorNotas}">Peso ${contadorNotas}:</label>
        <input type="number" id="peso${contadorNotas}" name="peso${contadorNotas}" step="any" required>
        `;

    container.appendChild(div);
    contadorNotas++;
}

document.addEventListener('DOMContentLoaded', function() {
    agregarNota(); // agrega una nota al iniciar la pagina
});