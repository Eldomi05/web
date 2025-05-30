from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/google667a48832647648e.html')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def submit():
    nombre = request.form.get('nombre''')
    error = None

    try:
        # obtener notas de examenes y quices
        examenes = request.form.getlist('examenes[]')
        quices = request.form.getlist('quices[]')

        #verificar que las notas esten llegando
        print("Examenes (raw):", examenes)
        print("Quices (raw):", quices)

        #convertir a float
        examenes = [float(n) for n in examenes if n.strip() != '']
        quices = [float(n) for n in quices if n.strip() != '']

        #obtener peseso de examenes y quices
        peso_examen = float(request.form.get('peso_examen')) / 100
        peso_quices = float(request.form.get('peso_quices')) / 100
        print("Examenes (float):", examenes)
        print("Quices (float):", quices)
        print("peso_examen:", peso_examen)
        print("peso_quices:", peso_quices)

        # verificacion
        if not examenes or not quices:
            error = "Por favor, ingrece al menos una nota en cada grupo."
            raise ValueError
    
    # promedio de examnes y quices
        promedio_examenes = sum(examenes) / len(examenes)
        promedio_quices = sum(quices) / len(quices)

        # nota final ponderada
        nota_final = (promedio_examenes * peso_examen) + (promedio_quices * peso_quices)
        nota_final = round(nota_final, 2)
        
        if nota_final >= 90:
            resultado = "A"
        elif nota_final>= 80:
            resultado = "B"
        elif nota_final >= 70:
            resultado = "C"
        elif nota_final >= 60:
            resultado = "D"
        else:
            resultado = "F"
        return render_template('result.html', nombre=nombre, promedio=nota_final, letra=resultado, error=None)
    except Exception as e:
        print(f'ERROR: {e}')
        # Capturar y mostrar el error
        error = str(e) if str(e) else "Por favor, ingrese notas y pesos válidos."
        return render_template('result.html', nombre=nombre, promedio=None, letra=None, error=error)
    

if __name__ == '__main__':
    app.run()