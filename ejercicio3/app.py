from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/',methods=['get'])
def index():
    return render_template('index.html')





@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        #obtener datos
        nombre =request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros'])
        precio_tarro=9000
        total_sin_descuento= round(precio_tarro * tarros_pintura)

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = round( total_sin_descuento * (1-descuento))
        rebaja = total_sin_descuento-total_con_descuento
        return render_template('resultadoej1.html',nombre = nombre, total_sin_descuento=total_sin_descuento,total_con_descuento=total_con_descuento, rebaja = rebaja)
    return render_template('ejercicio1.html')


 #

usuarios_registrados = {'juan': 'admin', 'pepe': 'user'}
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario_ingresado = request.form['usuario']
        contraseña_ingresada = request.form['pass']
        if usuario_ingresado in usuarios_registrados and usuarios_registrados[usuario_ingresado] == contraseña_ingresada:
            mensaje = f"Bienvenido {'administrador' if usuario_ingresado == 'juan' else 'usuario'} {usuario_ingresado}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('resultadoej2.html', mensaje=mensaje)
    return render_template('ejercicio2.html')




if __name__ == '__main__':
    app.run(debug=True)
