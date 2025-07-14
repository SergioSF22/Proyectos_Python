# Importación de las librerias necesarias
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

# Varible que va acumulando las instrucciones de los botones precionados
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# Funcion llamada al pulsar los botones de la calculadora de los numeros y operaciones
def click_boton(numero):
    global operador
    operador += numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


# Función que asigna la función de borrado a botón 'B' de la calculadora
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


# Función que asigna la función de resultado a botón 'R' de la calculadora
def obtener_resultado():
    global operador
    try:
        resultado = str(eval(operador))
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(0, resultado)
    except SyntaxError:
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(0, 'SYNTAX ERROR')
    except ZeroDivisionError:
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(0, 'ZERO DIVISION ERROR')
    finally:
        operador = ''


# Función que revisa el estado de las checkbox de los productos y actua en consecuencia activando o desactivando los cuadros de texto a su lado
def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1
    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1


# Función que al pulsar el botón total, hace los calculos para los productos seleccionamos y los muestra en sus respectivos cuadros de texto
def total():
    sub_total_comida = 0
    indice = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[indice])
        indice += 1

    sub_total_bebida = 0
    indice = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[indice])
        indice += 1

    sub_total_postre = 0
    indice = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[indice])
        indice += 1

    sub_total = sub_total_postre + sub_total_bebida + sub_total_comida
    iva = sub_total * 0.07
    total = sub_total + iva

    var_precio_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_precio_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_precio_postre.set(f"$ {round(sub_total_postre, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_iva.set(f"$ {round(iva, 2)}")
    var_total.set(f"$ {round(total, 2)}")

# Función que al pulsar el botón 'Factura', genera una factura detallada de los productos consumidos
def factura():
    texto_recibo.delete(1.0, END)
    numero_factura = f"N#{random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_factura = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos: \t{numero_factura}\t\t{fecha_factura}\n")
    texto_recibo.insert(END, '*' * 48 + '\n')
    texto_recibo.insert(END, 'Productos\t\tCant.\tPrecio Productos\n')
    texto_recibo.insert(END, '-' * 55 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0' and comida.get() != '':
            texto_recibo.insert(END, f'{lista_comidas[x].title()}\t\t{comida.get()}\t$ {(int(comida.get()) * precios_comida[x]):.2f}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0' and bebida.get() != '':
            texto_recibo.insert(END, f'{lista_bebidas[x].title()}\t\t{bebida.get()}\t$ {(int(bebida.get()) * precios_bebida[x]):.2f}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0' and postre.get() != '':
            texto_recibo.insert(END, f'{lista_postres[x].title()}\t\t{postre.get()}\t$ {(int(postre.get()) * precios_postre[x]):.2f}\n')
        x += 1

    texto_recibo.insert(END, '-' * 55 + '\n')
    texto_recibo.insert(END, f'Precio de la comida: \t\t\t{var_precio_comida.get()}\n')
    texto_recibo.insert(END, f'Precio de las bebida: \t\t\t{var_precio_bebida.get()}\n')
    texto_recibo.insert(END, f'Precio de los postre: \t\t\t{var_precio_postre.get()}\n')
    texto_recibo.insert(END, '-' * 55 + '\n')
    texto_recibo.insert(END, f'Sub total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'IVA: \t\t\t{var_iva.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, '*' * 48 + '\n')
    texto_recibo.insert(END, 'Gracias, vuelva pronto!')

# Función que al pulsar el botón 'Guardar', guardara el recibo actual en un archivo txt
def guardar():
    info_factura = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_factura)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')

# Función que al pulsar el botón 'Resetear', se encarga de dejar por defecto de nuevo todo el programa
def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_precio_comida.set('')
    var_precio_bebida.set('')
    var_precio_postre.set('')
    var_subtotal.set('')
    var_iva.set('')
    var_total.set('')


# Iniciar TKinter
aplicacion = Tk()

# Definimos el tamaño de la ventana en 1020x630 pixeles
aplicacion.geometry('1020x630+0+0')

# Evitamos que el usuario pueda cambiar el tamaño de la ventana
aplicacion.resizable(False, False)

# Título de la ventana
aplicacion.title("Mi Restaurante - Sistema de cobro")

# Definimos el color del fondo de la ventana
aplicacion.config(bg='DodgerBlue4')

# Panel superior
panel_superior = Frame(aplicacion, bd=0, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta título panel superior
etiqueta_titulo = Label(panel_superior, text='SISTEMA DE COBRO', fg='white', font=('Chillen', 58), bg='DodgerBlue4',
                        width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel precios
panel_precios = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=55)
panel_precios.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='DodgerBlue4')
panel_calculadora.pack()

# Panel recibos
panel_recibos = Frame(panel_derecha, bd=1, relief=FLAT, bg='DodgerBlue4')
panel_recibos.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='DodgerBlue4')
panel_botones.pack()

# Listas de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'ternera', 'pasta', 'pizza', 'sopa']
lista_bebidas = ['Coca-Cola', 'Nestea', 'Fanta', 'limonada', 'Zumo', 'Cerveza', 'Vino', 'Agua']
lista_postres = ['helado', 'fruta', 'brownie', 'flan', 'tarta', 'mousse', 'batido', 'bizcocho']

# Generar items de las comidas
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for c in lista_comidas:
    # Crear los checkbuttons de las comidas
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=c.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)
    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Generar items de las bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for b in lista_bebidas:
    # Crear los checkbuttons de las comidas
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    comida = Checkbutton(panel_bebidas,
                         text=b.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)
    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Generar items de las postres
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for p in lista_postres:
    # Crear los checkbuttons de las comidas
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    comida = Checkbutton(panel_postres,
                         text=p.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)
    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Variables de las etiquetas de precios
var_precio_comida = StringVar()
var_precio_bebida = StringVar()
var_precio_postre = StringVar()
var_subtotal = StringVar()
var_total = StringVar()
var_iva = StringVar()

# Etiquetas de precios y campos de entrada
# Comidas
etiqueta_precio_comida = Label(panel_precios,
                               text='Precio comida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_comida.grid(row=0, column=0)

texto_precio_comida = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_comida)
texto_precio_comida.grid(row=0, column=1, padx=41)

# Bebidas
etiqueta_precio_bebida = Label(panel_precios,
                               text='Precio bebida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_bebida.grid(row=1, column=0)

texto_precio_bebida = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_bebida)
texto_precio_bebida.grid(row=1, column=1, padx=41)

# Postres
etiqueta_precio_postre = Label(panel_precios,
                               text='Precio postre',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_postre.grid(row=2, column=0)

texto_precio_postre = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_postre)
texto_precio_postre.grid(row=2, column=1, padx=41)

# Subtotal
etiqueta_subtotal = Label(panel_precios,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_precios,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# IVA
etiqueta_iva = Label(panel_precios,
                     text='IVA',
                     font=('Dosis', 12, 'bold'),
                     bg='azure4',
                     fg='white')
etiqueta_iva.grid(row=1, column=2)

texto_iva = Entry(panel_precios,
                  font=('Dosis', 12, 'bold'),
                  bd=1,
                  width=10,
                  state='readonly',
                  textvariable=var_iva)
texto_iva.grid(row=1, column=3, padx=41)

# Total
etiqueta_total = Label(panel_precios,
                       text='Total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_precios,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['total', 'factura', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

# Asignamos las funciones creadas a su botón correspondiente
botones_creados[0].config(command=total)
botones_creados[1].config(command=factura)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Area recibo
texto_recibo = Text(panel_recibos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=43,
                    height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
# Visor
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# Botones
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', 'R', 'B', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for b in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=b.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

# Asignamos cada función correspondiente a los botones de la calculadora
for i in range(0, 16):
    valor = botones_calculadora[i]
    if i != 12 and i != 13:
        # Aquí es necesario definir una variable local por cada lambda 'v' para almacenar el valor del botón en cada iteración debido a que lambda guarda una referencia a la variable utilizada y no el valor exacto, por lo que si no lo hacemos TODAS las lambda obtendrian el valor de la último iteración que sería '/'
        botones_guardados[i].config(command=lambda v=valor: click_boton(v))

botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)

# Evitar que la pantalla se cierre
aplicacion.mainloop()
