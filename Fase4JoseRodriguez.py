import tkinter as tk
from tkinter import messagebox

CLAVE_ACCESO = "UNAD"


class NodoABB:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        self.cantidad_nodos = 0

    def limpiar(self):
        self.raiz = None
        self.cantidad_nodos = 0

    def existe(self, nodo, dato):
        if nodo is None:
            return False
        if dato == nodo.dato:
            return True
        if dato < nodo.dato:
            return self.existe(nodo.izq, dato)
        return self.existe(nodo.der, dato)

    def altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

    def supera_limite_niveles(self, nodo, dato, nivel=0):
        # El limite de 4 niveles corresponde a profundidades 0, 1, 2 y 3
        if nodo is None:
            return nivel >= 4
        if dato < nodo.dato:
            return self.supera_limite_niveles(nodo.izq, dato, nivel + 1)
        if dato > nodo.dato:
            return self.supera_limite_niveles(nodo.der, dato, nivel + 1)
        return False

    def _insertar_rec(self, nodo, dato):
        if nodo is None:
            self.cantidad_nodos += 1
            return NodoABB(dato)
        if dato < nodo.dato:
            nodo.izq = self._insertar_rec(nodo.izq, dato)
        elif dato > nodo.dato:
            nodo.der = self._insertar_rec(nodo.der, dato)
        return nodo

    def insertar(self, dato):
        if self.existe(self.raiz, dato):
            raise ValueError(f"El valor {dato} ya existe en el arbol.")

        if self.altura(self.raiz) >= 3 and self.supera_limite_niveles(self.raiz, dato, 0):
            raise ValueError("No se puede insertar: el arbol permite maximo 4 niveles.")

        self.raiz = self._insertar_rec(self.raiz, dato)

    def buscar(self, objetivo):
        ruta = []
        actual = self.raiz
        while actual is not None:
            ruta.append(actual.dato)
            if objetivo == actual.dato:
                return True, ruta
            if objetivo < actual.dato:
                actual = actual.izq
            else:
                actual = actual.der
        return False, ruta

    def preorden(self):
        lista = []
        self._pre(self.raiz, lista)
        return lista

    def _pre(self, nodo, lista):
        if nodo is not None:
            lista.append(nodo.dato)
            self._pre(nodo.izq, lista)
            self._pre(nodo.der, lista)

    def inorden(self):
        lista = []
        self._in(self.raiz, lista)
        return lista

    def _in(self, nodo, lista):
        if nodo is not None:
            self._in(nodo.izq, lista)
            lista.append(nodo.dato)
            self._in(nodo.der, lista)

    def postorden(self):
        lista = []
        self._post(self.raiz, lista)
        return lista

    def _post(self, nodo, lista):
        if nodo is not None:
            self._post(nodo.izq, lista)
            self._post(nodo.der, lista)
            lista.append(nodo.dato)


class PortalIngreso:
    def __init__(self, ventana, al_ingresar):
        self.ventana = ventana
        self.al_ingresar = al_ingresar
        self.intentos = 0
        self.max_intentos = 3

        self.ventana.title("Fase4JoseRodriguez - Secure Portal")
        self.ventana.geometry("500x640")
        self.ventana.configure(bg="#111111")
        self.ventana.resizable(False, False)

        self.marco = tk.Frame(self.ventana, bg="#111111", padx=30, pady=25)
        self.marco.pack(fill="both", expand=True)

        tk.Label(
            self.marco,
            text="BST Architecture Explorer",
            fg="#a855f7",
            bg="#111111",
            font=("Segoe UI", 20, "bold"),
        ).pack(pady=(15, 6))

        tk.Label(
            self.marco,
            text="Data Structures - Phase 4 Module",
            fg="#d1d5db",
            bg="#111111",
            font=("Segoe UI", 11),
        ).pack(pady=(0, 22))

        caja_datos = tk.Frame(
            self.marco,
            bg="#181818",
            highlightbackground="#2e2e2e",
            highlightthickness=1,
            padx=20,
            pady=16,
        )
        caja_datos.pack(fill="x", pady=(0, 28))

        datos = [
            "Application: Fase4JoseRodriguez",
            "Student: José Pastor Rodríguez Ahumada",
            "Course Code: 301305",
            "Date: November 2026",
        ]
        for texto in datos:
            tk.Label(
                caja_datos,
                text=texto,
                fg="#e5e7eb",
                bg="#181818",
                font=("Consolas", 10),
                anchor="w",
            ).pack(fill="x", pady=3)

        tk.Label(
            self.marco,
            text="Enter Security Password",
            fg="#f3f4f6",
            bg="#111111",
            font=("Segoe UI", 11, "bold"),
        ).pack(pady=(0, 10))

        self.campo_clave = tk.Entry(
            self.marco,
            show="*",
            bg="#ffffff",
            fg="#111111",
            insertbackground="#111111",
            font=("Segoe UI", 12),
            relief="flat",
            justify="center",
            width=24,
        )
        self.campo_clave.pack(ipady=6, pady=(0, 18))
        self.campo_clave.focus_set()
        self.campo_clave.bind("<Return>", lambda _e: self.validar_clave())

        tk.Button(
            self.marco,
            text="Authenticate & Access ->",
            command=self.validar_clave,
            bg="#a855f7",
            fg="#111111",
            activebackground="#9333ea",
            activeforeground="#111111",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
        ).pack(pady=(0, 20))

        tk.Label(
            self.marco,
            text="UNAD - ECBTI - Systems Engineering",
            fg="#9ca3af",
            bg="#111111",
            font=("Segoe UI", 9),
        ).pack(side="bottom", pady=(10, 0))

    def validar_clave(self):
        clave = self.campo_clave.get().strip()
        if clave == CLAVE_ACCESO:
            self.marco.destroy()
            self.al_ingresar()
            return

        self.intentos += 1
        restantes = self.max_intentos - self.intentos
        self.campo_clave.delete(0, tk.END)
        if restantes > 0:
            messagebox.showerror("Acceso denegado", f"Clave incorrecta. Intentos restantes: {restantes}")
            self.campo_clave.focus_set()
        else:
            messagebox.showerror("Acceso bloqueado", "Se supero el numero maximo de intentos.")
            self.ventana.destroy()


class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("BST Visualizer - Fase 4")
        self.ventana.geometry("1150x680")
        self.ventana.configure(bg="#181818")
        self.ventana.resizable(True, True)

        self.arbol = ArbolBinarioBusqueda()
        self.camino_marcado = set()

        panel_izq = tk.Frame(ventana, bg="#1e1e1e", width=270, padx=12, pady=12)
        panel_izq.pack(side="left", fill="y", padx=(10, 0), pady=10)
        panel_izq.pack_propagate(False)

        tk.Label(
            panel_izq,
            text="BST Controls",
            fg="#bb86fc",
            bg="#1e1e1e",
            font=("Segoe UI", 13, "bold"),
        ).pack(anchor="w", pady=(0, 10))

        self.entrada_valor = tk.Entry(
            panel_izq,
            bg="#2a2a2a",
            fg="#ffffff",
            insertbackground="#ffffff",
            font=("Segoe UI", 11),
            relief="flat",
        )
        self.entrada_valor.pack(fill="x", ipady=6, pady=(0, 10))
        self.entrada_valor.bind("<Return>", lambda _e: self.accion_insertar())

        tk.Button(
            panel_izq,
            text="Insert Node",
            command=self.accion_insertar,
            bg="#38bdf8",
            fg="#121212",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            pady=6,
        ).pack(fill="x", pady=(0, 6))

        tk.Button(
            panel_izq,
            text="Search Node",
            command=self.accion_buscar,
            bg="#bb86fc",
            fg="#121212",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            pady=6,
        ).pack(fill="x", pady=(0, 6))

        tk.Button(
            panel_izq,
            text="Clear Tree",
            command=self.accion_limpiar,
            bg="#cf6679",
            fg="#121212",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            pady=6,
        ).pack(fill="x", pady=(0, 16))

        self.lbl_nodos = tk.Label(
            panel_izq, text="Total Nodes: 0", fg="#e0e0e0", bg="#1e1e1e", font=("Segoe UI", 10)
        )
        self.lbl_nodos.pack(anchor="w", pady=2)

        self.lbl_altura = tk.Label(
            panel_izq, text="Tree Height: -1", fg="#e0e0e0", bg="#1e1e1e", font=("Segoe UI", 10)
        )
        self.lbl_altura.pack(anchor="w", pady=2)

        self.lbl_raiz = tk.Label(
            panel_izq, text="Root Value: -", fg="#e0e0e0", bg="#1e1e1e", font=("Segoe UI", 10)
        )
        self.lbl_raiz.pack(anchor="w", pady=2)

        area_grafica = tk.Frame(ventana, bg="#121212")
        area_grafica.pack(fill="both", expand=True, side="right", padx=10, pady=10)

        self.lienzo = tk.Canvas(
            area_grafica,
            width=750,
            height=320,
            bg="#121212",
            highlightthickness=1,
            highlightbackground="#2c2c2c",
        )
        self.lienzo.pack(fill="both", expand=True, pady=5)
        self.lienzo.bind("<Configure>", lambda _e: self.actualizar_vista())

        panel_recorridos = tk.Frame(area_grafica, bg="#121212", height=120)
        panel_recorridos.pack(fill="x", pady=5)

        self.vista_pre = self.crear_caja_recorrido(panel_recorridos, "Pre-order Sequence", 0)
        self.vista_in = self.crear_caja_recorrido(panel_recorridos, "In-order Sequence", 1)
        self.vista_post = self.crear_caja_recorrido(panel_recorridos, "Post-order Sequence", 2)

        self.actualizar_vista()

    def crear_caja_recorrido(self, padre, titulo, col):
        marco = tk.LabelFrame(
            padre,
            text=titulo,
            font=("Helvetica", 9, "bold"),
            fg="#bb86fc",
            bg="#181818",
            bd=1,
            relief="solid",
        )
        marco.grid(row=0, column=col, sticky="nsew", padx=3)
        padre.grid_columnconfigure(col, weight=1)

        etiqueta = tk.Label(
            marco, text="Empty Structure", fg="#cccccc", bg="#181818", font=("Helvetica", 9)
        )
        etiqueta.pack(fill="both", expand=True, padx=5, pady=5)
        return etiqueta

    def _leer_entero(self):
        texto = self.entrada_valor.get().strip()
        try:
            return int(texto)
        except ValueError:
            messagebox.showerror("Dato invalido", f"'{texto}' no es un numero entero valido.")
            return None

    def accion_insertar(self):
        valor = self._leer_entero()
        if valor is None:
            return

        try:
            self.arbol.insertar(valor)
            self.entrada_valor.delete(0, tk.END)
            self.camino_marcado.clear()
            self.actualizar_vista()
        except ValueError as err:
            messagebox.showerror("Validacion", str(err))

    def accion_buscar(self):
        valor = self._leer_entero()
        if valor is None:
            return

        encontrado, ruta = self.arbol.buscar(valor)
        self.camino_marcado = set(ruta)
        self.actualizar_vista()

        recorrido = " -> ".join(map(str, ruta))
        if encontrado:
            messagebox.showinfo("Busqueda", f"Nodo {valor} encontrado.\nRecorrido: {recorrido}")
        else:
            texto_ruta = recorrido if recorrido else "Arbol vacio"
            messagebox.showwarning("Busqueda", f"Nodo {valor} no encontrado.\nRecorrido: {texto_ruta}")

    def accion_limpiar(self):
        self.arbol.limpiar()
        self.entrada_valor.delete(0, tk.END)
        self.camino_marcado.clear()
        self.actualizar_vista()
        messagebox.showinfo("Reinicio", "El arbol se ha limpiado.")

    def actualizar_vista(self):
        total = self.arbol.cantidad_nodos
        alt = self.arbol.altura(self.arbol.raiz)
        val_raiz = self.arbol.raiz.dato if self.arbol.raiz else "-"

        self.lbl_nodos.config(text=f"Total Nodes: {total}")
        self.lbl_altura.config(text=f"Tree Height: {alt}")
        self.lbl_raiz.config(text=f"Root Value: {val_raiz}")

        self.vista_pre.config(
            text=", ".join(map(str, self.arbol.preorden())) if total > 0 else "Empty Structure"
        )
        self.vista_in.config(
            text=", ".join(map(str, self.arbol.inorden())) if total > 0 else "Empty Structure"
        )
        self.vista_post.config(
            text=", ".join(map(str, self.arbol.postorden())) if total > 0 else "Empty Structure"
        )

        self.lienzo.delete("all")
        if self.arbol.raiz:
            self.lienzo.update_idletasks()
            ancho = max(self.lienzo.winfo_width(), 650)
            self.dibujar_nodo(self.arbol.raiz, ancho // 2, 45, max(ancho // 5, 95))

    def dibujar_nodo(self, nodo, x, y, dx):
        radio = 20
        salto_y = 75
        marcado = nodo.dato in self.camino_marcado

        if nodo.izq:
            lx, ly = x - dx, y + salto_y
            rama_marcada = marcado and (nodo.izq.dato in self.camino_marcado)
            self.lienzo.create_line(
                x,
                y,
                lx,
                ly,
                fill="#facc15" if rama_marcada else "#bb86fc",
                width=4 if rama_marcada else 2,
            )
            self.dibujar_nodo(nodo.izq, lx, ly, max(dx // 2, 35))

        if nodo.der:
            rx, ry = x + dx, y + salto_y
            rama_marcada = marcado and (nodo.der.dato in self.camino_marcado)
            self.lienzo.create_line(
                x,
                y,
                rx,
                ry,
                fill="#facc15" if rama_marcada else "#bb86fc",
                width=4 if rama_marcada else 2,
            )
            self.dibujar_nodo(nodo.der, rx, ry, max(dx // 2, 35))

        self.lienzo.create_oval(
            x - radio,
            y - radio,
            x + radio,
            y + radio,
            fill="#854d0e" if marcado else "#1f2937",
            outline="#facc15" if marcado else "#38bdf8",
            width=3 if marcado else 2,
        )
        self.lienzo.create_text(
            x,
            y,
            text=str(nodo.dato),
            fill="#ffffff",
            font=("Segoe UI", 10, "bold"),
        )


def iniciar():
    raiz_tk = tk.Tk()
    PortalIngreso(raiz_tk, al_ingresar=lambda: VentanaPrincipal(raiz_tk))
    raiz_tk.mainloop()


if __name__ == "__main__":
    iniciar()