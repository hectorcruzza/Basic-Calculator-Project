import tkinter as tk
import math as m

class Calculator:
    def __init__(self):
        self.root = tk.Tk() #Iniciar ventana
        self.root.configure(bg = "#F2F4F4") #Configurar el color de la ventana
        self.root.geometry("350x527") #El tamaño de la ventana
        self.root.title("Calculator") #El titulo de la ventana

        #Variables requeridas durante la ejecucion del programa
        self.number_str = tk.StringVar() #Variable de texto especial modificable durante la ejecucion
        self.number_str.set("0") #Valor tipo string mostrado en la pantalla establecido a 0
        self.number_n = 0 #Primer valor numerico establecido a 0
        self.number_n2 = 0 #Segundo valor numerico establecido a 0
        self.replace_number_n2 = False #Valor logico referente a cuando el segundo numero esta siendo escrito
        self.assign_number_n = False #Valor logico referente a cuando el primer valor es asignado a su variable numerica
        self.assign_number_n2 = False #Valor logico referente a cuando el segundo valor es asignado a su variable numerica
        self.suma_c = False #Valor logico referente a cuando el boton de suma es presionado (Aplica para todas las operaciones binarias este concepto)
        self.resta_c = False  # Valor logico referente a cuando el boton de resta es presionado
        self.multiplicacion_c = False  # Valor logico referente a cuando el boton de multiplicacion es presionado
        self.division_c = False  # Valor logico referente a cuando el boton de division es presionado
        self.modulo_c = False  # Valor logico referente a cuando el boton de modulo es presionado
        self.raiz_c = False #Valor logico referente a cuando el boton de raiz es presionado (Aplica para todas las operaciones unarias este concepto)
        self.potencia_cuadrado_c = False #Valor logico referente a cuando el boton de potencia al cuadrado es presionado
        self.numero_entre_uno_c = False #Valor logico referente a cuando el boton de division de uno entre un numero es presionado
        self.sen_c = False #Valor logico referente a cuando el boton de seno es presionado
        self.cos_c = False #Valor logico referente a cuando el boton de coseno es presionado
        self.tan_c = False #Valor logico referente a cuando el boton de tangente es presionado
        self.mas_menos_c = False #Valor logico referente a cuando el boton de mas/menos es presionado
        self.equal_c = False #Valor logico referente a cuando el boton de igual es presionado
        self.operation_finished = False  #Valor logico referente a que una operación ha terminado

        #Bloque de codigo para la pantalla donde se muestra el numero en curso
        self.frame_display = tk.Frame(self.root, borderwidth = 5, relief = "sunken" , bg = "#FFFFFF")
        self.frame_display.pack(fill = tk.X, padx = 15, pady = 15)
        self.label_display_number = tk.Label(self.frame_display, textvariable = self.number_str, bg = "#FFFFFF", font = ("Helvetica", 31))
        self.label_display_number.pack(side = tk.RIGHT, padx = 13)

        #Bloque de codigo para la creación del frame con las respectivas columnas y botones
        self.frame_btns = tk.Frame(self.root)
        self.frame_btns.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight = 1, minsize = 60)
        self.frame_btns.columnconfigure([0, 1, 2, 3], weight = 1, minsize = 80)
        self.frame_btns.pack()

        self.btn_1 = tk.Button(self.frame_btns, text = "OFF", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.apagar)
        self.btn_1.grid(row = 0, column = 0, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_2 = tk.Button(self.frame_btns, text = "CE", bg = "#E67E22", font = ("Helvetica", 16), command = self.reset)
        self.btn_2.grid(row = 0, column = 1, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_3 = tk.Button(self.frame_btns, text = "C", bg = "#99A3A4", font = ("Helvetica", 16), command = self.clear_number)
        self.btn_3.grid(row = 0, column = 2, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_4 = tk.Button(self.frame_btns, text = "⌫", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.erase_number)
        self.btn_4.grid(row = 0, column = 3, sticky = "nsew", padx = 3, pady = 3)

        self.btn_5 = tk.Button(self.frame_btns, text = "sin", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.seno)
        self.btn_5.grid(row = 1, column = 0, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_6 = tk.Button(self.frame_btns, text = "cos", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.coseno)
        self.btn_6.grid(row = 1, column = 1, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_7 = tk.Button(self.frame_btns, text = "tan", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.tangente)
        self.btn_7.grid(row = 1, column = 2, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_8 = tk.Button(self.frame_btns, text = "MOD", bg = "#99A3A4", font = ("Helvetica", 16), command = self.modulo)
        self.btn_8.grid(row = 1, column = 3, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_9 = tk.Button(self.frame_btns, text = "1/x", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.numero_entre_uno)
        self.btn_9.grid(row = 2, column = 0, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_10 = tk.Button(self.frame_btns, text = "x²", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.potencia_cuadrado)
        self.btn_10.grid(row = 2, column = 1, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_11 = tk.Button(self.frame_btns, text = "√x", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.raiz)
        self.btn_11.grid(row = 2, column = 2, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_12 = tk.Button(self.frame_btns, text = "÷", bg = "#99A3A4", font = ("Helvetica", 16), command = self.division)
        self.btn_12.grid(row = 2, column = 3, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_13 = tk.Button(self.frame_btns, text = "7", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_13.cget("text")))
        self.btn_13.grid(row = 3, column = 0, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_14 = tk.Button(self.frame_btns, text = "8", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_14.cget("text")))
        self.btn_14.grid(row = 3, column = 1, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_15 = tk.Button(self.frame_btns, text = "9", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_15.cget("text")))
        self.btn_15.grid(row = 3, column = 2, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_16 = tk.Button(self.frame_btns, text = "×", bg = "#99A3A4", font = ("Helvetica", 16), command = self.multiplicacion)
        self.btn_16.grid(row = 3, column = 3, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_17 = tk.Button(self.frame_btns, text = "4", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_17.cget("text")))
        self.btn_17.grid(row = 4, column = 0, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_18 = tk.Button(self.frame_btns, text = "5", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_18.cget("text")))
        self.btn_18.grid(row = 4, column = 1, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_19 = tk.Button(self.frame_btns, text = "6", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_19.cget("text")))
        self.btn_19.grid(row = 4, column = 2, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_20 = tk.Button(self.frame_btns, text = "-", bg = "#99A3A4", font = ("Helvetica", 16), command = self.resta)
        self.btn_20.grid(row = 4, column = 3, sticky = "nsew", padx = 3, pady = 3)

        self.btn_21 = tk.Button(self.frame_btns, text = "1", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_21.cget("text")))
        self.btn_21.grid(row = 5, column = 0, sticky = "nsew", padx = 3, pady = 3)
    
        self.btn_22 = tk.Button(self.frame_btns, text = "2", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_22.cget("text")))
        self.btn_22.grid(row = 5, column = 1, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_23 = tk.Button(self.frame_btns, text = "3", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_23.cget("text")))
        self.btn_23.grid(row = 5, column = 2, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_24 = tk.Button(self.frame_btns, text = "+", bg = "#99A3A4", font = ("Helvetica", 16), command = self.suma)
        self.btn_24.grid(row = 5, column = 3, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_25 = tk.Button(self.frame_btns, text = "±", bg = "#E5E8E8", font = ("Helvetica", 16), command = self.mas_menos)
        self.btn_25.grid(row = 6, column = 0, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_26 = tk.Button(self.frame_btns, text = "0", bg = "#E5E8E8", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_26.cget("text")))
        self.btn_26.grid(row = 6, column = 1, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_27 = tk.Button(self.frame_btns, text = ".", bg = "#99A3A4", font = ("Helvetica", 16), command = lambda: self.get_input(self.btn_27.cget("text")))
        self.btn_27.grid(row = 6, column = 2, sticky = "nsew", padx = 3, pady = 3)
        
        self.btn_28 = tk.Button(self.frame_btns, text = "=", bg = "#99A3A4", font = ("Helvetica", 16), command = self.equal)
        self.btn_28.grid(row = 6, column = 3, sticky = "nsew", padx = 3, pady = 3)

        self.root.mainloop() #Fin del ciclo

    #Funcion para obtener el input del usuario
    def get_input(self, text):
        self.n_text = text #Variable para almacenar el input del usuario
        self.make_numbers() #Se llama a la funcion que hace uso del input del usuario

    #Funcion para la escritura de los valores numericos
    def make_numbers(self):
        #Si la operacion ha terminado, entonces:
        if self.operation_finished:
            self.reset() #Se reinician las variables

        #Si el texto en pantalla es "0" y el boton presionado es distinto del punto decimal o si el primer valor va a ser escrito o si el segundo valor va a ser escrito o si el boton de igual es presionado, entonces:
        if (self.number_str.get() == "0" and self.n_text != ".") or self.replace_number_n2 or self.raiz_c or self.potencia_cuadrado_c or self.numero_entre_uno_c or self.cos_c or self.sen_c or self.tan_c or self.mas_menos_c:
            self.number_str.set(self.n_text)  #Se reemplaza el texto dependiendo del input del usuario
            self.raiz_c = False #El valor logico de cuando el boton de raiz se presionado se vuelve falso
            self.potencia_cuadrado_c = False #El valor logico referente a cuando el boton de potencia al cuadrado es presionado se vuelve falso
            self.numero_entre_uno_c = False #El valor logico referente a cuando el boton de division de uno entre un numero es presionado se vuelve falso
            self.cos_c = False #El valor logico referente a cuando el boton de coseno es presionado se vuelve falso
            self.sen_c = False #El valor logico referente a cuando el boton de seno es presionado se vuelve falso
            self.tan_c = False #El valor logico referente a cuando el boton de tangente es presionado se vuelve falso
            self.mas_menos_c = False #El valor logico referente a cuando el boton de mas/menos es presionado se vuelve falso
            self.replace_number_n2 = False #El valor logico de cuando el segundo numero empieza a ser escrito se vuelve falso
        else:
            #Si el input del usuario es igual a un punto, entonces:
            if self.n_text == ".":
                if self.n_text not in self.number_str.get():  #Verificar si no hay un punto en la cadena
                    self.number_str.set(self.number_str.get() + self.n_text) #Se concatena el valor en pantalla con el nuevo dependiendo del input del usuario
            else: #Sino
                if len(self.number_str.get()) <= 11:  # Limitar el número de caracteres en pantalla
                    self.number_str.set(self.number_str.get() + self.n_text) #Se concatena el valor en pantalla con el nuevo dependiendo del input del usuario

    #Funcion para asigar el primer valor base
    def assign_base_value(self):
        #Si el boton de igual no es presionado, entonces:
        if not self.equal_c:
            self.assign_number_n = True #El valor logico de cuando el primer numero es asignado se vuelve verdadero
            self.replace_number_n2 = True #El valor logico de cuando el segundo numero va a ser escrito se vuelve verdadero
        self.number_n = float(self.number_str.get()) #El valor en pantalla es asignado al primer valor numerico
        self.number_str.set(str(self.number_n)) #Se muestra la asignacion

    #Funcion para asigar el segundo valor
    def assign_second_value(self):
        self.assign_number_n2 = True #El valor logico de cuando el sehundo numero es asignado se vuelve verdadero
        self.number_n2 = float(self.number_str.get()) #El valor en pantalla es asignado al segundo valor numerico

    #Funcion para borrar un numero
    def erase_number(self): 
        #Si no se ha asignado el primer numero, o el primer numero ya ha sido asignado y el segundo numero esta siendo escrito y no se ha presionado el boton de igual, entonces:
        if not self.assign_number_n or (self.assign_number_n and not self.replace_number_n2 and not self.equal_c):
            if len(self.number_str.get()) == 1: #Si la longitud del valor en pantalla es igual 1, entonces:
                self.number_str.set("0") #El valor en pantalla se vuelve "0"
            else: #Sino
                self.number_str.set(self.number_str.get()[:-1]) #Se elimina el ultimo valor del valor en pantalla

    #Funcion para borrar el numero en curso
    def clear_number(self):
        #Si no se ha asignado el primer numero, o el primer numero ya ha sido asignado y el segundo numero esta siendo escrito y no se ha presionado el boton de igual, entonces:
        if not self.assign_number_n or (self.assign_number_n and not self.replace_number_n2 and not self.equal_c):
            self.number_str.set("0") #El valor en pantalla se vuelve "0"

    #Funcion para resetear la calculadora
    def reset(self):
        self.number_str.set("0") #Valor tipo string mostrado en la pantalla establecido a 0
        self.number_n = 0 #Primer valor numerico establecido a 0
        self.number_n2 = 0 #Segundo valor numerico establecido a 0
        self.replace_number_n2 = False #Valor logico referente a cuando el segundo numero esta siendo escrito
        self.assign_number_n = False #Valor logico referente a cuando el primer valor es asignado a su variable numerica
        self.assign_number_n2 = False #Valor logico referente a cuando el segundo valor es asignado a su variable numerica
        self.suma_c = False #Valor logico referente a cuando el boton de suma es presionado (Aplica para todas las operaciones binarias este concepto)
        self.resta_c = False  # Valor logico referente a cuando el boton de resta es presionado
        self.multiplicacion_c = False  # Valor logico referente a cuando el boton de multiplicacion es presionado
        self.division_c = False  # Valor logico referente a cuando el boton de division es presionado
        self.modulo_c = False  # Valor logico referente a cuando el boton de modulo es presionado
        self.raiz_c = False #Valor logico referente a cuando el boton de raiz es presionado (Aplica para todas las operaciones unarias este concepto)
        self.potencia_cuadrado_c = False #Valor logico referente a cuando el boton de potencia al cuadrado es presionado
        self.numero_entre_uno_c = False #Valor logico referente a cuando el boton de division de uno entre un numero es presionado
        self.sen_c = False #Valor logico referente a cuando el boton de seno es presionado
        self.cos_c = False #Valor logico referente a cuando el boton de coseno es presionado
        self.tan_c = False #Valor logico referente a cuando el boton de tangente es presionado
        self.mas_menos_c = False #Valor logico referente a cuando el boton de mas/menos es presionado
        self.equal_c = False #Valor logico referente a cuando el boton de igual es presionado
        self.operation_finished = False #Valor logico referente a que una operación ha terminado

    #Funcion de cuando se presiona el boton de igual (Lo descrito aplica solo para las operaciones binarias)
    def equal(self):
        self.equal_c = True #El valor logico de cuando el boton de igual es presionado se vuelve verdadero
        #Si no esta asignado el primer numero, entonces:
        if not self.assign_number_n: 
            self.assign_base_value() #Se ejecuta la funcion para asignar el primer numero base
        #Si no esta asignado el segundo numero, entonces:
        elif not self.assign_number_n2:
            self.assign_second_value() #Se ejecuta la funcion para asignar el segundo numero
        #Si el valor logico de cuando el boton de suma es presionado es verdadero, entonces:
        if self.suma_c:
            self.suma() #Se ejecuta la funcion de suma
        elif self.resta_c:
            self.resta()
        elif self.multiplicacion_c:
            self.multiplicacion()
        elif self.division_c:
            self.division()
        elif self.modulo_c:
            self.modulo()
        self.operation_finished = True #El valor logico referente a que una operación ha terminado se vuelve verdadero

    #Funcion de cuando se presiona el boton de suma (Lo descrito aplica solo para las operaciones binarias)
    def suma(self):
        #Si no esta asignado el primer numero, entonces:
        if not self.assign_number_n:
            self.suma_c = True #El valor logico de cuando el boton de suma es presionado se vuelve verdadero
            self.assign_base_value() #Se ejecuta la funcion para asignar el primer numero base
        #Si el valor logico de cuando el boton de igual es presionado es verdadero, entonces:
        elif self.equal_c:
            self.number_n += self.number_n2 #Se efectua la operacion
            self.number_str.set(str(self.number_n)[:12]) #Se muestra en pantalla el resultado de la operacion
        #Si no esta asignado el segundo numero, entonces:
        elif not self.assign_number_n2:
            self.assign_second_value() #Se ejecuta la funcion para asignar el segundo numero
            self.equal() #Se ejecuta la funcion del boton igual
            self.assign_number_n2 = False #El valor logico de cuando el segundo numero es asignado se vuelve falso
            self.equal_c = False #El valor logico de cuando el boton de igual es presionado se vuelve falso
            self.operation_finished = False #El valor logico referente a que una operación ha terminado se vuelve falso
            self.replace_number_n2 = True #El valor logico de cuando el segundo numero va a ser escrito se vuelve verdadero

    # Función para la resta
    def resta(self):
        # Si no está asignado el primer número, entonces:
        if not self.assign_number_n:
            self.resta_c = True  # El valor lógico de cuando el botón de resta es presionado se vuelve verdadero
            self.assign_base_value()  # Se ejecuta la función para asignar el primer número base
        # Si el valor lógico de cuando el botón de igual es presionado es verdadero, entonces:
        elif self.equal_c:
            self.number_n -= self.number_n2  # Se efectúa la operación
            self.number_str.set(str(self.number_n)[:12])  # Se muestra en pantalla el resultado de la operación
        # Si no está asignado el segundo número, entonces:
        elif not self.assign_number_n2:
            self.assign_second_value()  # Se ejecuta la función para asignar el segundo número
            self.equal()  # Se ejecuta la función del botón igual
            self.assign_number_n2 = False  # El valor lógico de cuando el segundo número es asignado se vuelve falso
            self.equal_c = False  # El valor lógico de cuando el botón de igual es presionado se vuelve falso
            self.operation_finished = False  # El valor lógico referente a que una operación ha terminado se vuelve falso
            self.replace_number_n2 = True  # El valor lógico de cuando el segundo número va a ser escrito se vuelve verdadero

    # Función para la multiplicación
    def multiplicacion(self):
        # Si no está asignado el primer número, entonces:
        if not self.assign_number_n:
            self.multiplicacion_c = True  # El valor lógico de cuando el botón de multiplicación es presionado se vuelve verdadero
            self.assign_base_value()  # Se ejecuta la función para asignar el primer número base
        # Si el valor lógico de cuando el botón de igual es presionado es verdadero, entonces:
        elif self.equal_c:
            self.number_n *= self.number_n2  # Se efectúa la operación
            self.number_str.set(str(self.number_n)[:12])  # Se muestra en pantalla el resultado de la operación
        # Si no está asignado el segundo número, entonces:
        elif not self.assign_number_n2:
            self.assign_second_value()  # Se ejecuta la función para asignar el segundo número
            self.equal()  # Se ejecuta la función del botón igual
            self.assign_number_n2 = False  # El valor lógico de cuando el segundo número es asignado se vuelve falso
            self.equal_c = False  # El valor lógico de cuando el botón de igual es presionado se vuelve falso
            self.operation_finished = False  # El valor lógico referente a que una operación ha terminado se vuelve falso
            self.replace_number_n2 = True  # El valor lógico de cuando el segundo número va a ser escrito se vuelve verdadero

    # Función para la división
    def division(self):
        # Si no está asignado el primer número, entonces:
        if not self.assign_number_n:
            self.division_c = True  # El valor lógico de cuando el botón de división es presionado se vuelve verdadero
            self.assign_base_value()  # Se ejecuta la función para asignar el primer número base
        # Si el valor lógico de cuando el botón de igual es presionado es verdadero, entonces:
        elif self.equal_c:
            if self.number_n2 != 0:  # Verificar si el divisor no es cero
                self.number_n /= self.number_n2  # Se efectúa la operación
                self.number_str.set(str(self.number_n)[:12])  # Se muestra en pantalla el resultado de la operación
            else:
                self.number_str.set("Error")  # Mostrar error si se intenta dividir entre cero
        # Si no está asignado el segundo número, entonces:
        elif not self.assign_number_n2:
            self.assign_second_value()  # Se ejecuta la función para asignar el segundo número
            self.equal()  # Se ejecuta la función del botón igual
            self.assign_number_n2 = False  # El valor lógico de cuando el segundo número es asignado se vuelve falso
            self.equal_c = False  # El valor lógico de cuando el botón de igual es presionado se vuelve falso
            self.operation_finished = False  # El valor lógico referente a que una operación ha terminado se vuelve falso
            self.replace_number_n2 = True  # El valor lógico de cuando el segundo número va a ser escrito se vuelve verdadero

    # Función para el modulo
    def modulo(self):
        # Si no está asignado el primer número, entonces:
        if not self.assign_number_n:
            self.modulo_c = True  # El valor lógico de cuando el botón de módulo es presionado se vuelve verdadero
            self.assign_base_value()  # Se ejecuta la función para asignar el primer número base
        # Si el valor lógico de cuando el botón de igual es presionado es verdadero, entonces:
        elif self.equal_c:
            if self.number_n2 != 0:
                self.number_n %= self.number_n2
                self.number_str.set(str(self.number_n)[:12])
            else:
                self.number_str.set("Error")
        # Si no está asignado el segundo número, entonces:
        elif not self.assign_number_n2:
            self.assign_second_value()  # Se ejecuta la función para asignar el segundo número
            self.equal()  # Se ejecuta la función del botón igual
            self.assign_number_n2 = False  # El valor lógico de cuando el segundo número es asignado se vuelve falso
            self.equal_c = False  # El valor lógico de cuando el botón de igual es presionado se vuelve falso
            self.operation_finished = False  # El valor lógico referente a que una operación ha terminado se vuelve falso
            self.replace_number_n2 = True  # El valor lógico de cuando el segundo número va a ser escrito se vuelve verdadero

    #Funcion de cuando se presiona el boton de raiz (Lo descrito aplica solo para las operaciones unarias)
    def raiz(self):
        self.raiz_c = True #El valor logico referente a cuando el boton de raiz es presionado se vuelve verdadero
        if float(self.number_str.get()) < 0:
            self.number_str.set("Error")
        else:
            self.number_str.set(str(float(self.number_str.get()) ** 0.5)[:12]) #Se efectua la operacion y es mostrada en pantalla

    #Funcion para la potencia al cuadrado
    def potencia_cuadrado(self):
        self.potencia_cuadrado_c = True #El valor logico referente a cuando el boton de potencia al cuadrado es presionado se vuelve verdadero
        self.number_str.set(str(float(self.number_str.get()) ** 2)[:12]) #Se efectua la operacion y es mostrada en pantalla

    #Funcion para la division de uno entre un numero
    def numero_entre_uno(self):
        self.numero_entre_uno_c = True #El valor logico referente a cuando el boton de division de uno entre un numero es presionado se vuelve verdadero
        self.number_str.set(str(1 / float(self.number_str.get()))[:12]) #Se efectua la operacion y es mostrada en pantalla

    #Funcion para el seno de un numero
    def seno(self):
        self.sen_c = True #El valor logico referente a cuando el boton de seno es presionado se vuelve verdadero
        self.number_str.set(str(m.sin(m.radians(float(self.number_str.get()))))[:12]) #Se efectua la operacion y es mostrada en pantalla

    #Funcion para el coseno de un numero
    def coseno(self):
        self.cos_c = True #El valor logico referente a cuando el boton de coseno es presionado se vuelve verdadero
        self.number_str.set(str(m.cos(m.radians(float(self.number_str.get()))))[:12]) #Se efectua la operacion y es mostrada en pantalla

    #Funcion para la tangente de un numero
    def tangente(self):
        self.tan_c = True #El valor logico referente a cuando el boton de tangente es presionado se vuelve verdadero
        self.number_str.set(str(m.tan(m.radians(float(self.number_str.get()))))[:12]) #Se efectua la operacion y es mostrada en pantalla

    #Funcion para el boton mas/menos
    def mas_menos(self):
        self.mas_menos_c = True #El valor logico referente a cuando el boton de mas/menos es presionado se vuelve verdadero
        if float(self.number_str.get()) != 0.0:
            self.number_str.set(str(-1 * float(self.number_str.get()))[:12]) #Se efectua la operacion y es mostrada en pantalla

    def apagar(self):
        self.root.destroy()

Calculator() #Instancia creada
