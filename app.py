from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_promedio', methods=['POST'])
def calcular_promedio():
    try:
        notas_finales = []

        for i in range(1, 4):
            laboratorio1_str = request.form.get(f"laboratorio1_{i}")
            laboratorio2_str = request.form.get(f"laboratorio2_{i}")
            parcial_str = request.form.get(f"parcial_{i}")

            # Verificar si los valores son None antes de convertir a flotante
            if laboratorio1_str is not None and laboratorio2_str is not None and parcial_str is not None:
                laboratorio1 = float(laboratorio1_str)
                laboratorio2 = float(laboratorio2_str)
                parcial = float(parcial_str)

                promedio_computo = (laboratorio1 * 0.3) + (laboratorio2 * 0.3) + (parcial * 0.4)
                notas_finales.append(promedio_computo)

        promedio_general = sum(notas_finales) / 3

        resultado = "Aprobado" if promedio_general >= 6.0 else "Reprobado"

        return render_template('resultado.html', notas_finales=notas_finales, promedio_general=promedio_general, resultado=resultado)

    except Exception as e:
        # Manejar cualquier error y mostrar un mensaje
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
