'''CÓDIGO DEL PROGRAMA FRIDGETRACK- Desarrollado por alumnos de 2º de Bachillerato del IES Murillo'''

#Importamos las distintas librerias que usaremos durante el programa
from tkinter import *
import tkinter.font as tkFont
import webbrowser #Para utilizar enlaces
from datetime import * #Para obtener la fecha actual


#Creamos la pantalla principal
root= Tk()
root.configure(bg="lightblue")
root.attributes("-fullscreen", True)
fuenteTitulo= tkFont.Font(root,family="Impacto", size=70)
titulo_principal = Label(root, text="FRIDGETRACK",font=fuenteTitulo, bg="lightblue", justify="center")      
bienvenida_label =Label(root, text="¡Bienvenido a la aplicación!", bg="lightblue", fg="#19284C", font=('Helvetica', 30))
titulo_principal.pack(pady=10)
bienvenida_label.pack()


#Lista para almacenar alimentos vacía
lista_alimentos = []


#Obtenemos la fecha de hoy
fecha_actual=datetime.today()
#Creamos una variable de la fecha en tres días que usaremos más adelante (Importante)
fecha_en_tres_dias = fecha_actual + timedelta(days=3)


#Creamos una funcion que abra los enlaces de distintas ubicaciones
def linkSevilla():
    webbrowser.open("https://admin.google.com/u/0/ServiceNotAllowed?service=local&hl=es&pli=1")
def linkMalaga():
    webbrowser.open("https://admin.google.com/u/0/ServiceNotAllowed?service=local&hl=es")
def linkAlmeria():
    webbrowser.open("https://www.google.com/maps/dir//C%C3%A1ritas+Diocesana,+C.+Alcalde+Mu%C3%B1oz,+10,+04004+Almer%C3%ADa/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0xd70760072c06c37:0x1b4cf6d2f10b1d2f?sa=X&ved=1t:57443&ictx=111")
def linkGranada():
    webbrowser.open("https://www.google.com/maps/dir//Hogar+y+Comedor+Social+del+Coraz%C3%B3n+de+Mar%C3%ADa,+C.+Colegios,+s%2Fn,+18001+Granada/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0xd71fceab67030c7:0xf8cafca369347ebf?sa=X&ved=1t:57443&ictx=111")
def linkCordoba():
    webbrowser.open("https://www.google.com/maps/place//data=!4m2!3m1!1s0xd6cdf632ef3d989:0xd1b4dd173124f144?sa=X&ved=1t:8290&ictx=111")
def linkCadiz():
    webbrowser.open("https://www.google.com/maps/place//data=!4m2!3m1!1s0xd0dd1601143cde9:0x23ac0172ecd146ed?sa=X&ved=1t:8290&ictx=111")
def linkJaen():
    webbrowser.open("https://www.google.com/maps/dir//comedores+sociales+jaen/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0xd6dd752f13b9d17:0xd7e2c808d62a862d?sa=X&ved=1t:3061&ictx=111")
def linkHuelva():
    webbrowser.open("https://www.google.com/maps/dir//Banco+de+Alimentos+de+Huelva,+C.+Almadraba,+5,+21002+Huelva/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0xd11cf31e7be6d83:0x481e7b1ef04d33c6?sa=X&ved=1t:57443&ictx=111")



#Metodo para la pagina de comedores sociales
def ir_comedores_sociales():
    # Crear una nueva ventana para la página "Comedores Sociales cerca de ti"
    ventana_comedores_sociales = Toplevel(bg="#ecf0f1")
    ventana_comedores_sociales.geometry("1500x900")
    ventana_comedores_sociales.configure(bg="lightyellow")
    #Mostramos un texto
    Advert= Label(ventana_comedores_sociales, text="!!Esto es una lista de comedores sociales a los que puedes donar comida que te sobre o esté a punto de caducar!!", bg="red", fg="black", font=("helvetica", 20))
    #La estructura será:
    #Título del sitio
    titulo_sevilla = Label(ventana_comedores_sociales, text="Comedores sociales en Sevilla:", bg="lightyellow",fg="black", font=('Helvetica', 19 ))
    #Boton que abre el enlace
    comedores_sevilla = Button(ventana_comedores_sociales, text="Nuestra señora del Rosario", command= linkSevilla, font=("helvetica", 20))
    titulo_malaga = Label(ventana_comedores_sociales, text="Comedores sociales en Malaga:", bg="lightyellow",fg="black", font=('Helvetica', 19 ))
    comedores_malaga = Button(ventana_comedores_sociales, text="Yo soy tu", command= linkMalaga, font=("helvetica", 20))
    titulo_Almeria = Label(ventana_comedores_sociales, text="Comedores sociales en Almería:", bg="lightyellow",fg="black", font=('Helvetica', 19 ))
    comedores_Almeria = Button(ventana_comedores_sociales, text="Caritas diocesanas", command= linkAlmeria, font=("helvetica", 20))
    titulo_Granada = Label(ventana_comedores_sociales, text="Comedores sociales en Granada:", bg="lightyellow",fg="black", font=('Helvetica', 19 ))
    comedores_Granada = Button(ventana_comedores_sociales, text="Hogar y comedor social del Corazón de María", command= linkGranada, font=("helvetica", 20))
    titulo_Cordoba = Label(ventana_comedores_sociales, text="Comedores sociales en Córdoba:", bg="lightyellow",fg="black", font=('Helvetica', 19 ))
    comedores_Cordoba = Button(ventana_comedores_sociales, text="Comedor Social Trinitario San Juan", command= linkCordoba, font=("helvetica", 20))
    titulo_Cadiz = Label(ventana_comedores_sociales, text="Comedores sociales en Cádiz:", bg="lightyellow",fg="black", font=('Helvetica', 19 ))
    comedores_Cadiz = Button(ventana_comedores_sociales, text="Comedor Virgen Poderosa", command= linkCadiz, font=("helvetica", 20))
    titulo_Jaen = Label(ventana_comedores_sociales, text="Comedores sociales en Jaén:", bg="lightyellow",fg="black", font=('Helvetica', 19 ))
    comedores_Jaen = Button(ventana_comedores_sociales, text="Comedor social de San Roque", command= linkJaen, font=("helvetica", 20))
    titulo_Huelva = Label(ventana_comedores_sociales, text="Comedores sociales en Huelva:", bg="lightyellow",fg="black", font=('Helvetica', 19 ))
    comedores_Huelva = Button(ventana_comedores_sociales, text="Banco de alimentos de Huelva ", command= linkHuelva, font=("helvetica", 20))
    #Mostramos por pantalla todos los botones
    Advert.pack(pady=5)
    titulo_sevilla.pack()
    comedores_sevilla.pack()
    titulo_malaga.pack()
    comedores_malaga.pack()
    titulo_Almeria.pack()
    comedores_Almeria.pack()
    titulo_Granada.pack()
    comedores_Granada.pack()
    titulo_Cordoba.pack()
    comedores_Cordoba.pack()
    titulo_Cadiz.pack()
    comedores_Cadiz.pack()
    titulo_Jaen.pack()
    comedores_Jaen.pack()
    titulo_Huelva.pack()
    comedores_Huelva.pack()
    boton_cerrar=Button(ventana_comedores_sociales,text="Cerrar",command=ventana_comedores_sociales.destroy, font=("Helvetica", 15 ))
    boton_cerrar.pack(pady=10)


#Funcion del boton de la pagina principal que te permite ver los alimentos que están registrados
def ir_a_tu_nevera():
        # Crear una nueva ventana para la página "Añadir alimentos"
    ventana_tu_nevera = Toplevel(bg="#ecf0f1")
    ventana_tu_nevera.geometry("1080x500")
    # Etiqueta de texto
    etiqueta_nevera = Label(ventana_tu_nevera, text="Alimentos registrados:", bg="#ecf0f1", fg="#2c3e50", font=('Helvetica', 20))
    etiqueta_nevera.pack(pady=5)
    #Bucle for que muestra tanto alimentos como se hayan registrado
    for alimento in lista_alimentos:
            alimentos_registrados=Label(ventana_tu_nevera, text=alimento, font=("Helvetica",15))
            alimentos_registrados.pack()


# Método para ir a la página "Añadir alimentos"
def ir_a_anadir_alimentos():
    # Crear una nueva ventana para la página
    ventana_anadir_alimentos = Toplevel(root)
    ventana_anadir_alimentos.geometry("500x750")
    ventana_anadir_alimentos.configure(bg="lightyellow")
    aviso_entrada_producto=Label(ventana_anadir_alimentos, text="Escriba el producto comprado", font=('Helvetica', 15))
    aviso_entrada_producto.pack(pady=5)
    #Creamos la entrada para que el usuario escriba el alimento
    entrada_producto = Entry(ventana_anadir_alimentos, font=('Helvetica', 15))
    entrada_producto.pack(pady=5)

    #Creamos un menú de opciones para que el usuario seleccione una categoría
    categoria_opciones= ["Carne", "Pescado", "Fruta", "Verdura", "Lácteos"]
    texto_menu_opciones=StringVar(ventana_anadir_alimentos)
    texto_menu_opciones.set("Seleccione la categoria de su producto")
    categoria_producto = OptionMenu(ventana_anadir_alimentos, texto_menu_opciones, *categoria_opciones )
    categoria_producto.config(font=("Helvetica", 15))
    categoria_producto.pack(pady=5)

    #Creamos una entrada con la fecha: el día, mes y año. Debemos forzar que sea tipo numérico
    #Para los días:
    fecha_días=Label(ventana_anadir_alimentos, text="Inserte el día de compra", font=('Helvetica', 15))
    fecha_días.pack(pady=5)
    fecha_dias_productos = Entry(ventana_anadir_alimentos,font=('Helvetica', 15))
    fecha_dias_productos.pack(pady=5)
    #Para el mes:
    aviso_fecha_mes=Label(ventana_anadir_alimentos, text="Inserte el mes de compra", font=('Helvetica', 15))
    aviso_fecha_mes.pack(pady=5)  
    fecha_mes_productos = Entry(ventana_anadir_alimentos,font=('Helvetica', 15))
    fecha_mes_productos.pack(pady=5)
    #Para el año
    aviso_fecha_año=Label(ventana_anadir_alimentos, text="Inserte el año de compra", font=('Helvetica', 15))
    aviso_fecha_año.pack(pady=5)  
    fecha_año_productos = Entry(ventana_anadir_alimentos,font=('Helvetica', 15))
    fecha_año_productos.pack(pady=5)
     
   
    #Función guardar alimento
    def guardar_alimento():
        alimento=str(entrada_producto.get())
        categoria_alimento= str(texto_menu_opciones.get())
        fecha_dias_compra=int(fecha_dias_productos.get())
        fecha_mes_compra=int(fecha_mes_productos.get())
        fecha_año_compra=int(fecha_año_productos.get())
       
        #Creamos una fecha de caducidad según la categoría del producto
        if categoria_alimento=="Fruta":
                fecha_dias_de_caducidad= fecha_dias_compra+7
           
        elif categoria_alimento=="Verdura":
                fecha_dias_de_caducidad= fecha_dias_compra+10
           
        elif categoria_alimento=="Carne":
                fecha_dias_de_caducidad= fecha_dias_compra+5
           
        elif categoria_alimento=="Pescado":
            fecha_dias_de_caducidad= fecha_dias_compra+1
    
        elif categoria_alimento=="Lácteos":
                fecha_dias_de_caducidad= fecha_dias_compra+10
       
        #Creamos un diccionario para almacenar los datos del alimento de forma ordenada
        alimento_guardado = {
        "Alimento": alimento,
        "Categoria": categoria_alimento,
        "Fecha de compra": (fecha_dias_compra, fecha_mes_compra, fecha_año_compra),
        "Fecha de caducidad": (fecha_dias_de_caducidad,fecha_mes_compra,fecha_año_compra)}

        lista_alimentos.append(alimento_guardado)

    #Creamos el boton que será el encargado de guardar los alimentos
    obtener_alimento_guardado=Button(ventana_anadir_alimentos, text="Aceptar", command= guardar_alimento)
    obtener_alimento_guardado.pack()
   #Creamos el boton que será el encargado de abrir la ventana "Tu nevera"
    boton_ir_a_tu_nevera = Button(ventana_anadir_alimentos, text="Tu nevera", command=ir_a_tu_nevera, font=("Helvetica",15))
    boton_ir_a_tu_nevera.pack(pady=15)
    #Creamos el boton que será el encargado de cerrar la ventana añadir alimentos
    boton_cerrar= Button(ventana_anadir_alimentos, text= "Cerrar", command= ventana_anadir_alimentos.destroy)
    boton_cerrar.pack(pady=5)




def productos_cercanos_a_caducar():
    #Creamos una nueva ventana con productos cercanos a su fecha de caducidad
    ventana_productos_casi_caducados= Toplevel(root)
    ventana_productos_casi_caducados.geometry("1400x750")
    ventana_productos_casi_caducados.configure(bg="lightyellow")
    contador = 0
     
   
   #Para todos los alimentos de la lista, establecemos el formate en el que queremos obtener la fecha de caducidad
    for alimento in lista_alimentos:
        fecha_formato_caducidad = ""
        fecha_caducidad_string = str(alimento["Fecha de caducidad"]) #Obtenemos del diccionario la fecha de caducidad de cada alimento
        formato_fecha = '(%d, %m, %Y)' #Definimos que el formato de la fecha es de DD/MM/YYYY
        fecha_formato_caducidad = datetime.strptime (fecha_caducidad_string, formato_fecha) #Establecemos el formato final de la fecha de caducidad
        

        #Imponemos las distintas condiciones, si la fecha de caducidad ya en un formato arreglado es menor qu ela actual el alimento está caducado
        if (fecha_formato_caducidad) < (fecha_actual):
            alimentos_caducados=Label(ventana_productos_casi_caducados, text=(alimento,"Está caducado"),fg="red",font=("Helvetica",15))
            alimentos_caducados.pack()
            contador= contador + 1
        #Si el alimento caduca en tres días o menos, se mostrará tambien con letras azules       
        elif (fecha_formato_caducidad) <= (fecha_en_tres_dias):
               
            alimentos_casi_caducados = Label(ventana_productos_casi_caducados, text=(alimento,"Esta a punto de caducar"),fg="blue",font=("Helvetica",15))
            alimentos_casi_caducados.pack()
            contador= contador + 1

    #Si no se ha sumado ningún punto al contador es que no se dan ninguna de las condiciones anteriores por lo que no hay alimentos caducados ni cercanos a caducar    
    if (contador == 0):
        nohay_alimentos_caducados=Label(ventana_productos_casi_caducados, text=("No hay alimentos próximos a caducar ni caducados"),fg="green",font=("Helvetica",15))
        nohay_alimentos_caducados.pack()


#Boton ir a añadir alimentos
boton_anadir_alimentos = Button(root, text="Añadir alimentos", command=ir_a_anadir_alimentos, font=("Helvetica", 25))
boton_anadir_alimentos.pack(pady=10)

#Boton ir a Tu nevera
boton_tu_nevera = Button(root, text="Alimentos en tu nevera", command= ir_a_tu_nevera, font= ("Helvetica", 25))
boton_tu_nevera.pack(pady=10)

#Boton alimentos cercanos a caducar
boton_alimentos_casi_caducados= Button(root, text="Listado alimentos próximos a caducar o caducados", command= productos_cercanos_a_caducar, font= ("Helvetica", 25))
boton_alimentos_casi_caducados.pack(pady=10)

#Boton ir a Comedores Sociales
boton_comedores_sociales = Button(root, text="Comedores Sociales cerca de ti", command= ir_comedores_sociales, font= ("Helvetica", 25))
boton_comedores_sociales.pack(pady=10)

#Boton cerrar programa
boton_cerrar=Button(root,text="Cerrar",command=root.destroy, font=("Helvetica", 15 ))
boton_cerrar.pack(pady=10)

#Ejecutamos el código
root.mainloop()
