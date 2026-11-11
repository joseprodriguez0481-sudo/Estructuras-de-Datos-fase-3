import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk


class Affiliate:

  def __init__(
      self,
      id_type,
      id_number,
      nombre_afiliado,
      income,
      service,
      employment_type,
      affiliation_fee,
  ):
    self.id_type = id_type
    self.id_number = id_number
    self.full_name = full_name
    self.income = income
    self.service = service
    self.employment_type = employment_type
    self.affiliation_fee = affiliation_fee
    self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class CompensandoteApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Sistema Compensándote - Login")
    self.root.geometry("400x300")
    self.root.config(bg="#f0f2f5")

    # Estructuras de datos lineales
    self.stack = []  # Pila
    self.queue = []  # Cola
    self.list_data = []  # Lista

    # Pantalla de Login
    self.create_login_widgets()

  def create_login_widgets(self):
    # Limpiar ventana si ya existe algo
    for widget in self.root.winfo_children():
      widget.destroy()

    self.root.title("Login - Compensándote")
    self.root.geometry("400x350")

    frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
    frame.pack(expand=True, fill="both", padx=15, pady=15)

    tk.Label(
        frame,
        text="Caja Compensándote",
        font=("Arial", 14, "bold"),
        bg="#ffffff",
        fg="#2c3e50",
    ).pack(pady=10)

    tk.Label(frame, text="Usuario:", bg="#ffffff").pack(anchor="w")
    self.user_entry = tk.Entry(frame, width=25)
    self.user_entry.pack(pady=5)
    self.user_entry.insert(0, "admin")

    tk.Label(frame, text="Contraseña:", bg="#ffffff").pack(anchor="w")
    self.pass_entry = tk.Entry(frame, width=25, show="*")
    self.pass_entry.pack(pady=5)

    btn_login = tk.Button(
        frame,
        text="Ingresar",
        bg="#27ae60",
        fg="white",
        width=15,
        command=self.validate_login,
    )
    btn_login.pack(pady=10)

    btn_about = tk.Button(
        frame,
        text="Acerca de",
        bg="#2980b9",
        fg="white",
        width=15,
        command=self.show_about,
    )
    btn_about.pack(pady=5)

  def validate_login(self):
    user = self.user_entry.get()
    password = self.pass_entry.get()

    # Contraseña genérica solicitada por la guía
    if password == "Caja":
      self.open_main_window()
    else:
      messagebox.showerror(
          "Error de Autenticación", "Contraseña incorrecta. (Use: Caja)"
      )

  def show_about(self):
    messagebox.showinfo(
        "Acerca de",
        "Aplicación: Componente Práctico Fase 3\nEstudiante: José Pastor"
        " Rodríguez\nPrograma: Ingeniería en Inteligencia Artificial\nUniversidad"
        " UNAD",
    )

  def open_main_window(self):
    for widget in self.root.winfo_children():
      widget.destroy()

    self.root.title("Módulo de Afiliaciones - CajaCompensándote(José)")
    self.root.geometry("920x660")

    # Contenedor Principal
    main_frame = tk.Frame(self.root, padx=10, pady=10)
    main_frame.pack(fill="both", expand=True)

    # Frame Izquierdo: Formulario
    form_frame = tk.LabelFrame(
        main_frame, text=" Registro de Afiliado ", padx=10, pady=10
    )
    form_frame.pack(side="left", fill="y", padx=5, pady=5)

    tk.Label(form_frame, text="Tipo ID:").grid(
        row=0, column=0, sticky="w", pady=2
    )
    self.combo_id = ttk.Combobox(
        form_frame, values=["CC", "TI", "CE"], width=18, state="readonly"
    )
    self.combo_id.grid(row=0, column=1, pady=2)
    self.combo_id.current(0)

    tk.Label(form_frame, text="No. Identificación:").grid(
        row=1, column=0, sticky="w", pady=2
    )
    self.entry_id_num = tk.Entry(form_frame, width=20)
    self.entry_id_num.grid(row=1, column=1, pady=2)

    tk.Label(form_frame, text="Nombre Completo:").grid(
        row=2, column=0, sticky="w", pady=2
    )
    self.entry_name = tk.Entry(form_frame, width=20)
    self.entry_name.grid(row=2, column=1, pady=2)

    tk.Label(form_frame, text="Ingresos (Salarios M.):").grid(
        row=3, column=0, sticky="w", pady=2
    )
    self.entry_income = tk.Entry(form_frame, width=20)
    self.entry_income.grid(row=3, column=1, pady=2)

    tk.Label(form_frame, text="Servicio:").grid(
        row=4, column=0, sticky="w", pady=2
    )
    self.combo_service = ttk.Combobox(
        form_frame,
        values=[
            "Recreacion",
            "Curso formacion",
            "Paquete viaje",
            "Medicina preventiva",
        ],
        width=18,
        state="readonly",
    )
    self.combo_service.grid(row=4, column=1, pady=2)
    self.combo_service.current(0)

    tk.Label(form_frame, text="Tipo Afiliado:").grid(
        row=5, column=0, sticky="w", pady=2
    )
    self.combo_employment = ttk.Combobox(
        form_frame, values=["Dependiente", "Independiente"], width=18, state="readonly"
    )
    self.combo_employment.grid(row=5, column=1, pady=2)
    self.combo_employment.current(0)

    tk.Label(form_frame, text="Estructura Lineal:").grid(
        row=6, column=0, sticky="w", pady=2
    )
    self.combo_structure = ttk.Combobox(
        form_frame, values=["Pila (Stack)", "Cola (Queue)", "Lista (List)"], width=18, state="readonly"
    )
    self.combo_structure.grid(row=6, column=1, pady=2)
    self.combo_structure.current(0)

    # Botones de Acción
    btn_register = tk.Button(
        form_frame,
        text="Registrar",
        bg="#27ae60",
        fg="white",
        width=18,
        command=self.register_data,
    )
    btn_register.grid(row=7, column=0, columnspan=2, pady=5)

    btn_clear = tk.Button(
        form_frame,
        text="Limpiar",
        bg="#f39c12",
        fg="white",
        width=18,
        command=self.clear_form,
    )
    btn_clear.grid(row=8, column=0, columnspan=2, pady=5)

    btn_report = tk.Button(
        form_frame,
        text="Reporte / Mostrar",
        bg="#2980b9",
        fg="white",
        width=18,
        command=self.show_report,
    )
    btn_report.grid(row=9, column=0, columnspan=2, pady=5)

    btn_delete = tk.Button(
        form_frame,
        text="Eliminar Registro",
        bg="#c0392b",
        fg="white",
        width=18,
        command=self.delete_data,
    )
    btn_delete.grid(row=10, column=0, columnspan=2, pady=5)

    # Frame Derecho: Tabla Visual (Treeview)
    table_frame = tk.LabelFrame(main_frame, text=" Datos Almacenados ", padx=5, pady=5)
    table_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    columns = ("Tipo", "ID", "Nombre", "Ingresos", "Servicio", "TipoAfi", "Tarifa", "Fecha")
    self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)

    for col in columns:
      self.tree.heading(col, text=col)
      self.tree.column(col, width=90)

    self.tree.pack(fill="both", expand=True)

  def calculate_fee(self, income, service):
    # Cálculo dinámico de la tarifa base según el servicio elegido por el afiliado
    base = 50000
    if service == "Paquete viaje":
      base = 120000
    elif service == "Curso formacion":
      base = 80000
    elif service == "Medicina preventiva":
      base = 60000
    return base + (income * 5000)

  def register_data(self):
    try:
      id_type = self.combo_id.get()
      id_num = self.entry_id_num.get()
      name = self.entry_name.get()
      income = float(self.entry_income.get())
      service = self.combo_service.get()
      emp_type = self.combo_employment.get()
      structure_type = self.combo_structure.get()

      if not id_num or not name:
        messagebox.showwarning("Advertencia", "Por favor complete los campos obligatorios.")
        return

      fee = self.calculate_fee(income, service)
      new_affiliate = Affiliate(id_type, id_num, name, income, service, emp_type, fee)

      # Almacenar según la estructura lineal elegida
      if "Pila" in structure_type:
        self.stack.append(new_affiliate)
      elif "Cola" in structure_type:
        self.queue.append(new_affiliate)
      else:
        self.list_data.append(new_affiliate)

      messagebox.showinfo("Éxito", "¡Registro guardado con éxito!")
      self.clear_form()
      self.update_table()

    except ValueError:
      messagebox.showerror("Error", "Los ingresos deben ser un valor numérico válido.")

  def clear_form(self):
    self.entry_id_num.delete(0, tk.END)
    self.entry_name.delete(0, tk.END)
    self.entry_income.delete(0, tk.END)

  def update_table(self):
    for row in self.tree.get_children():
      self.tree.delete(row)

    # Mostrar todos los elementos combinados o según se requiera
    all_records = self.stack + self.queue + self.list_data
    for item in all_records:
      self.tree.insert(
          "",
          tk.END,
          values=(
              item.id_type,
              item.id_number,
              item.full_name,
              item.income,
              item.service,
              item.employment_type,
              item.affiliation_fee,
              item.date,
          ),
      )

  def show_report(self):
    total_items = len(self.stack) + len(self.queue) + len(self.list_data)
    report_msg = (
        f"--- REPORTE DE ESTRUCTURAS ---\n"
        f"Elementos en Pila (Stack): {len(self.stack)}\n"
        f"Elementos en Cola (Queue): {len(self.queue)}\n"
        f"Elementos en Lista (List): {len(self.list_data)}\n"
        f"Total Registros: {total_items}"
    )
    messagebox.showinfo("Reporte del Sistema", report_msg)

  def delete_data(self):
    structure_type = self.combo_structure.get()
    if "Pila" in structure_type:
      if self.stack:
        self.stack.pop()
        messagebox.showinfo("Eliminar", "Se eliminó el último elemento de la Pila (LIFO).")
      else:
        messagebox.showwarning("Aviso", "La Pila está vacía.")
    elif "Cola" in structure_type:
      if self.queue:
        self.queue.pop(0)
        messagebox.showinfo("Eliminar", "Se eliminó el primer elemento de la Cola (FIFO).")
      else:
        messagebox.showwarning("Aviso", "La Cola está vacía.")
    else:
      if self.list_data:
        self.list_data.pop()
        messagebox.showinfo("Eliminar", "Se eliminó el último elemento de la Lista.")
      else:
        messagebox.showwarning("Aviso", "La Lista está vacía.")
    self.update_table()


if __name__ == "__main__":
  root = tk.Tk()
  app = CompensandoteApp(root)
  root.mainloop()