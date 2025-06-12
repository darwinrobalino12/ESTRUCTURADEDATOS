# Este código usaremos para guardar informacion del estudiante de X centro educativo.

# Primero, creamos la clase llamada Estudiante.

class Estudiante:
    """
    Esta es la clase Estudiante. sera nuestro contenedor de informacion y en la cual daremos atributos.
    """

    def __init__(self, id_estudiante, nombres, apellidos, direccion, telefonos):
        """
        Aquí guardamos los datos básicos del estudiante.

        Args:
            id_estudiante (str): Un número o código único para identificar al estudiante.
            nombres (str): El primer nombre y/o nombres del estudiante.
            apellidos (str): Los apellidos del estudiante.
            direccion (str): La dirección de su casa.
            telefonos (list): Una lista con los números de teléfono del estudiante.

        """
        self.id = id_estudiante  # Guardamos el ID del estudiante
        self.nombres = nombres  # Guardamos los nombres
        self.apellidos = apellidos  # Guardamos los apellidos
        self.direccion = direccion  # Guardamos la dirección

        # Para los teléfonos, usamos una "lista" de Python.
        # Una lista es como un array: puede guardar varios elementos.
        # Aquí tomamos solo los primeros 2 teléfonos que nos den.
        self.telefonos = list(telefonos[:2])  # Convertimos a lista y tomamos hasta 2 elementos.

    # Sirve para mostrar toda la información del estudiante en la pantalla.
    def mostrar_informacion(self):
        """
        Imprime en la pantalla toda la información del estudiante.
        """
        print(f"--- Información del Estudiante ---")
        print(f"ID: {self.id}")
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Dirección: {self.direccion}")

        # Unimos los números de teléfono con comas para que se vean bien.
        # Si no hay teléfonos, mostramos 'N/A'.
        telefonos_texto = ", ".join(self.telefonos) if self.telefonos else "N/A"
        print(f"Teléfonos: {telefonos_texto}")
        print(f"----------------------------------")

    # Este método nos permite añadir un nuevo número de teléfono.
    # Pero solo si el estudiante tiene menos de 2 teléfonos ya guardados.
    def agregar_telefono(self, nuevo_telefono):
        """
        Añade un nuevo teléfono a la lista del estudiante.
        Solo se permite si ya tiene menos de 2 teléfonos.

        Args:
            nuevo_telefono (str): El número de teléfono a añadir.
        """
        # Verificamos si el número de teléfonos actual es menor a 2
        if len(self.telefonos) < 2:
            self.telefonos.append(nuevo_telefono)  # Añadimos el nuevo teléfono a la lista
            print(f"Teléfono '{nuevo_telefono}' agregado correctamente.")
        else:
            print(f"¡Atención! Ya tienes 2 teléfonos. No se pueden agregar más.")

    # Este método nos permite cambiar un número de teléfono que ya existe.
    # Necesitamos saber qué número cambiar (su posición o 'índice').
    def actualizar_telefono(self, indice, nuevo_telefono):
        """
        Cambia un número de teléfono existente por uno nuevo.

        Args:
            indice (int): La posición del teléfono a cambiar (0 para el primero, 1 para el segundo, etc.).
            nuevo_telefono (str): El nuevo número de teléfono.
        """
        # Verificamos que el índice sea válido (que exista esa posición en la lista)
        if 0 <= indice < len(self.telefonos):
            self.telefonos[indice] = nuevo_telefono  # Cambiamos el teléfono en esa posición
            print(f"Teléfono en la posición {indice} actualizado a '{nuevo_telefono}'.")
        else:
            print(f"¡Error! La posición {indice} no existe en la lista de teléfonos. Intenta con 0 o 1.")


# --- probaremos el codigo clase estudiante
if __name__ == "__main__":
    print("--- Probando la Clase Estudiante ---")

    # 1. Creamos un estudiante llamado Darwin. Le damos su ID, nombres, dirección y 3 teléfonos.
    estudiante1 = Estudiante(
        id_estudiante="A001",
        nombres="Darwin Vladimir",
        apellidos="Robalino Bonilla",
        direccion="Calle Principal via Ambato",
        telefonos=["095759638", "032875536"]
    )

    # 2. Mostramos toda la información de Darwin para ver cómo se guardó.
    print("\nInformación inicial de Darwin:")
    estudiante1.mostrar_informacion()

    # 3. Intentamos añadir un tercer numero teléfono para Darwin.
    # Como el límite es 2, el sistema nos dirá que no se puede.
    print("\nIntentando añadir un tercer numero teléfonico a Darwin:")
    estudiante1.agregar_telefono("0999888777")
    estudiante1.mostrar_informacion()

    # 4. Ahora, cambiamos el primer teléfono de Darwin (el que está en la posición 0).
    print("\nCambiando el primer teléfono de Darwin:")
    estudiante1.actualizar_telefono(0, "095759638")
    estudiante1.mostrar_informacion()

    # 5. Creamos otro estudiante, Luis, pero esta vez con solo 2 teléfonos al inicio.
    estudiante2 = Estudiante(
        id_estudiante="L002",
        nombres="Luis",
        apellidos="Martínez Solís",
        direccion="Av. Siempre Viva 456, Villa Feliz",
        telefonos=["0955443322", "022334455"]
    )
    print("\nInformación inicial de Luis:")
    estudiante2.mostrar_informacion()

    # 6. Añadimos un tercer teléfono a Luis. Ahora sí se puede (because we allowed only 2 in init, so adding a 3rd would be the second phone)
    # Correction: The __init__ method limits phones to 2. So, 'telefonos=["0955443322", "022334455"]' already fills the list to 2.
    # Therefore, adding a third phone here will also hit the limit.
    print("\nAñadiendo un tercer teléfono a Luis:")
    estudiante2.agregar_telefono("0900112233")
    estudiante2.mostrar_informacion()

    # 7. Intentamos añadir un cuarto teléfono para Luis.
    # De nuevo, el sistema nos dirá que ya llegó al límite.
    print("\nIntentando añadir un cuarto teléfono a Luis (después de llenar):")
    estudiante2.agregar_telefono("0944556677")
    estudiante2.mostrar_informacion()