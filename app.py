from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def submit():
    nombre = request.form['Nombre']
    notas = []
    pesos = []
    error = None

    try:
        for i in range(1,31):
            if f'nota{i}' in request.form and f'peso{i}' in request.form:
                nota = (request.form[f'nota{i}'])
                peso = (request.form[f'peso{i}'])
            
            if nota and peso:
                notas.append(float(nota))
                pesos.append(float(peso))
            elif nota or peso:
                error = "Por favor, ingrese tanto la nota como el peso para cada trabajo."
                break
            else:
                break
        if not notas or not pesos:
            error = "Por favor, ingrese al menos una nota y su peso."
        elif len(notas) != len(pesos):
            error = "El numero de nota y peso debe ser el mismo"
        else:
            total_peso = sum(pesos)
            if total_peso == 0:
                    error = "La suma de los pesos debe ser diferente de cero"
            else:
                promedio_ponderado = sum(nota * peso for nota, peso in zip(notas, pesos))
                promedio = round(promedio_ponderado, 2)
                if promedio >= 90:
                    resultado = "A"
                elif promedio >= 80:
                    resultado = "B"
                elif promedio >= 70:
                    resultado = "C"
                elif promedio >= 60:
                    resultado = "D"
                else:
                    resultado = "F"
                return render_template('result.html', nombre=nombre, promedio=promedio, letra=resultado, error=None)
                
    except ValueError:
        error = "Por favor, ingrese notas y pesos validos."
    
    return render_template('result.html', nombre=nombre, promedio=None, letra=None, error=error)

if __name__ == '__main__':
    app.run()