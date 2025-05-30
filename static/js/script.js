let contadorQuices = 1;
let contadorExamenes = 1;

function agregarQuiz() {
    const container = document.getElementById('quices-contenedor');
    
    const div = document.createElement('div');
    div.className = 'nota-quiz';

    div.innerHTML = `
        <label for="quiz${contadorQuices}">Quiz ${contadorQuices}:</label>
        <input type="number" id="quiz${contadorQuices}" name="quices[]" step="any" required>
        `;
        
        container.appendChild(div);
        contadorQuices++;
}
function agregarExamen() {
    const container = document.getElementById('examenes-contenedor');

    const div = document.createElement('div');
    div.className = 'nota-examen';

    div.innerHTML = `
        <label for='examen${contadorExamenes}'>Examen ${contadorExamenes}:</label>
        <input type='number' id='examen${contadorExamenes}' name='examenes[]' step='any' required>
        `;

        container.appendChild(div);
        contadorExamenes++;
}

document.addEventListener('DOMContentLoaded', function() {
    agregarQuiz(); // agrega un quiz al iniciar la pagina
    agregarExamen(); // agrega un examen al iniciar la pagina
});