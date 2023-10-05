from tkinter import *

# Crear una instancia de la ventana principal
ventana = Tk()

# Configurar el título de la ventana
ventana.title("Mi Ventana Tkinter")

# Configurar las dimensiones de la ventana
ventana.geometry("400x300")  # Ancho x Alto

# Pantallas
def home():
    home_label = Label(ventana, text="Inicio")
    home_label.config(
        fg="white",
        bg="black",
        font="Arial 30",
        padx=20,
        pady=20
    )    
    home_label.grid(row=0, column=0)
    return True

def add():
    add_label = Label(ventana, text="añadir Producto")
    add_label.config(
        fg="white",
        bg="black",
        font="Arial 30",
        padx=20,
        pady=20
    )    
    add_label.grid(row=0, column=0)
    return True

def info():
    info_label = Label(ventana, text="informacion de Producto")
    info_label.config(
        fg="white",
        bg="black",
        font="Arial 30",
        padx=20,
        pady=20
    )    
    info_label.grid(row=1, column=0)
    return True
#definicion de los label
home_label = Label(ventana, text="Inicio")
add_label = Label(ventana, text="Añadir Producto")
info_label = Label(ventana, text="informacion de Producto")
#ocultar pantalla     
home_label.grid_remove
add_label.grid_remove
info_label.grid_remove

#Pantalla de Inicio
home()


# Agregar contenido a la ventana (widgets, etiquetas, botones, etc.)
menu_superior=Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="añadir", command=add)
menu_superior.add_command(label="Informacion", command=info )
menu_superior.add_command(label="Salir", command=ventana.quit)

#cargar ventana
ventana.config(menu=menu_superior)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()

