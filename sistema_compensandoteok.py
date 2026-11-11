import tkinter as tk
from tkinter import messagebox, ttk

# 1. Definición de la Clase Affiliate (Buenas prácticas de POO)
class Affiliate:
    def __init__(self, id_type, id_number, full_name, income, service, employment_type, affiliation_fee, date):
        self.id_type = id_type
        self.id_number = id_number
        self.full_name = full_name
        self.income = float(income)
        self.service = service
        self.employment_type = employment_type
        self.affiliation_fee = float(affiliation_fee)
        self.date = date

    def obtener_detalles(self):
        return f"{self.full_name} | Doc: {self.id_number} | Serv: {self.service} | Ingreso: ${self.income:,.2f}"

class CompensandoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Afiliaciones - Compensándote")
        self.root.geometry("800x650")

        # Estructuras de Datos Lineales
        self.pila_afiliados = []   # LIFO
        self.cola_afiliados = []   # FIFO
        self.lista_afiliados = []  # Lista dinámica

        self.crear_interfaz()

    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.root, text="Gestión de Afiliaciones - Compensándote", font=("Arial", 14, "bold"))
        titulo.pack(pady=10)

        # Frame de Formulario
        form_frame = tk.LabelFrame(self.root, text=" Formulario de Registro ", font=("Arial", 10, "bold"))
        form_frame.pack(fill="x", padx=15, pady=5)

        # Campos
        tk.Label(form_frame, text="Tipo ID:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.combo_id_type = ttk.Combobox(form_frame, values=["Cédula de Ciudadanía", "Tarjeta de Identidad", "Cédula de Extranjería"], state="readonly", width=22)
        self.combo_id_type.grid(row=0, column=1, padx=5, pady=5)
        self.combo_id_type.current(0)

        tk.Label(form_frame, text="Número ID:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.entry_id_number = tk.Entry(form_frame, width=25)
        self.entry_id_number.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Nombre Completo:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_full_name = tk.Entry(form_frame, width=25)
        self.entry_full_name.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Ingresos ($):").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self.entry_income = tk.Entry(form_frame, width=25)
        self.entry_income.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Servicio:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.combo_service = ttk.Combobox(form_frame, values=["Salud", "Subsidio Familiar", "Crédito", "Recreación"], state="readonly", width=22)
        self.combo_service.grid(row=2, column=1, padx=5, pady=5)
        self.combo_service.current(0)

        tk.Label(form_frame, text="Tipo Empleo:").grid(row=2, column=2, sticky="w", padx=5, pady=5)
        self.combo_employment = ttk.Combobox(form_frame, values=["Dependiente", "Independiente"], state="readonly", width=22)
        self.combo_employment.grid(row=2, column=3, padx=5, pady=5)
        self.combo_employment.current(0)

        tk.Label(form_frame, text="Fecha (AAAA-MM-DD):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_date = tk.Entry(form_frame, width=25)
        self.entry_date.grid(row=3, column=1, padx=5, pady=5)

        # Botones de Acción
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Registrar (Pila/Cola/Lista)", bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Limpiar", bg="#ff9800", fg="white", font=("Arial", 9, "bold"), command=self.limpiar).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Atender Cola (FIFO)", bg="#2196F3", fg="white", font=("Arial", 9, "bold"), command=self.atender_cola).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Desapilar Pila (LIFO)", bg="#9c27b0", fg="white", font=("Arial", 9, "bold"), command=self.desapilar_pila).grid(row=0, column=3, padx=5)

        # Registro de Recorrido de Estructuras (Log visual exigido por el tutor)
        log_frame = tk.LabelFrame(self.root, text=" Registro de Eventos y Recorrido de Estructuras (Trazabilidad) ", font=("Arial", 10, "bold"))
        log_frame.pack(fill="both", expand=True, padx=15, pady=5)

        self.text_log = tk.Text(log_frame, height=12, state="normal", bg="#1e1e1e", fg="#00ff00", font=("Consolas", 9))
        self.text_log.pack(fill="both", expand=True, padx=5, pady=5)
        self.text_log.insert("end", ">> Sistema inicializado. Esperando registros de afiliados...\n")

    def registrar(self):
        # Validar campos vacíos (Buenas prácticas)
        if not self.entry_id_number.get() or not self.entry_full_name.get() or not self.entry_income.get() or not self.entry_date.get():
            messagebox.showerror("Error", "Por favor complete todos los campos obligatorios.")
            return

        try:
            income = float(self.entry_income.get())
        except ValueError:
            messagebox.showerror("Error", "El campo de ingresos debe ser numérico.")
            return

        # Calcular tarifa de afiliación de ejemplo según ingresos
        fee = income * 0.02

        # Crear objeto de la clase Affiliate
        nuevo_afiliado = Affiliate(
            id_type=self.combo_id_type.get(),
            id_number=self.entry_id_number.get(),
            full_name=self.entry_full_name.get(),
            income=income,
            service=self.combo_service.get(),
            employment_type=self.combo_employment.get(),
            affiliation_fee=fee,
            date=self.entry_date.get()
        )

        # Inserción en las 3 estructuras de datos solicitadas
        self.pila_afiliados.append(nuevo_afiliado)   # PUSH en Pila (LIFO)
        self.cola_afiliados.append(nuevo_afiliado)   # ENQUEUE en Cola (FIFO)
        self.lista_afiliados.append(nuevo_afiliado)  # Inserción en Lista

        # Escribir el recorrido y trazabilidad en la consola visual (Log)
        log_msg = (
            f"[REGISTRO EXITOSO]\n"
            f" -> [PILA - LIFO]: Se agregó '{nuevo_afiliado.full_name}' al tope de la pila. Total en pila: {len(self.pila_afiliados)}\n"
            f" -> [COLA - FIFO]: Se encoló '{nuevo_afiliado.full_name}' al final de la cola. Total en cola: {len(self.cola_afiliados)}\n"
            f" -> [LISTA]: Se añadió '{nuevo_afiliado.full_name}' a la lista dinámica. Total en lista: {len(self.lista_afiliados)}\n"
            f"--------------------------------------------------------------------------------\n"
        )
        self.text_log.insert("end", log_msg)
        self.text_log.see("end")

        messagebox.showinfo("Éxito", f"Afiliado registrado correctamente.\nTarifa calculada: ${fee:,.2f}")
        self.limpiar()

    def limpiar(self):
        self.entry_id_number.delete(0, "end")
        self.entry_full_name.delete(0, "end")
        self.entry_income.delete(0, "end")
        self.entry_date.delete(0, "end")
        self.combo_id_type.current(0)
        self.combo_service.current(0)
        self.combo_employment.current(0)

    def atender_cola(self):
        if len(self.cola_afiliados) == 0:
            messagebox.showwarning("Cola Vacía", "No hay elementos en la cola para atender.")
            return
        
        # Atiende el primero que entró (FIFO)
        atendido = self.cola_afiliados.pop(0)
        log_msg = f"[ATENCIÓN COLA - FIFO]: Salió el afiliado '{atendido.full_name}'. Quedan {len(self.cola_afiliados)} en cola.\n"
        self.text_log.insert("end", log_msg)
        self.text_log.see("end")
        messagebox.showinfo("Cola FIFO", f"Se atendió a: {atendido.full_name}")

    def desapilar_pila(self):
        if len(self.pila_afiliados) == 0:
            messagebox.showwarning("Pila Vacía", "No hay elementos en la pila para retirar.")
            return
        
        # Saca el último que entró (LIFO)
        retirado = self.pila_afiliados.pop()
        log_msg = f"[DESAPILAR - LIFO]: Se retiró el elemento del tope: '{retirado.full_name}'. Quedan {len(self.pila_afiliados)} en pila.\n"
        self.text_log.insert("end", log_msg)
        self.text_log.see("end")
        messagebox.showinfo("Pila LIFO", f"Se desapiló a: {retirado.full_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompensandoteApp(root)
    root.mainloop()