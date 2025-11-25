# sistema de empleados y proyectos

class empleado:
    contador_id = 1
    
    def __init__(self, nombre, salario_base):
        self._nombre = nombre
        self._id_empleado = empleado.contador_id
        self._salario_base = salario_base
        empleado.contador_id += 1
        self.proyectos = []
    
    def calcular_salario(self):
        return self._salario_base
    
    def asignar_proyecto(self, proyecto):
        if len(self.proyectos) >= self.limite_proyectos:
            print(f"error: {self._nombre} ya tiene {self.limite_proyectos} proyectos, no puede tener mas")
            return False
        
        if proyecto in self.proyectos:
            print(f"error: {self._nombre} ya esta en este proyecto")
            return False
            
        self.proyectos.append(proyecto)
        proyecto.agregar_empleado(self)
        return True
    
    def mostrar_informacion(self):
        print(f"nombre: {self._nombre}")
        print(f"id: {self._id_empleado}")
        print(f"salario: {self.calcular_salario()}")
        print(f"proyectos asignados: {len(self.proyectos)}")

class desarrollador(empleado):
    def __init__(self, nombre, salario_base, nivel, lenguajes):
        super().__init__(nombre, salario_base)
        self.lenguajes = lenguajes
        self.nivel = nivel
        self.limite_proyectos = 3
    
    def calcular_salario(self):
        salario_total = self._salario_base
        
        if self.nivel == "junior":
            salario_total += 200
        elif self.nivel == "semisenior":
            salario_total += 500
        elif self.nivel == "senior":
            salario_total += 1000
            
        return salario_total

class diseñador(empleado):
    def __init__(self, nombre, salario_base, herramientas, especialidad):
        super().__init__(nombre, salario_base)
        self.herramientas = herramientas
        self.especialidad = especialidad
        self.limite_proyectos = 2
    
    def calcular_salario(self):
        salario_total = self._salario_base
        
        if "figma" in self.herramientas:
            salario_total += 300
        elif "photoshop" in self.herramientas or "illustrator" in self.herramientas:
            salario_total += 200
            
        if len(self.herramientas) >= 3:
            salario_total += 400
            
        return salario_total

class gerente(empleado):
    def __init__(self, nombre, salario_base, departamento):
        super().__init__(nombre, salario_base)
        self.departamento = departamento
        self.equipo = []
        self.limite_proyectos = 0
    
    def calcular_salario(self):
        total_equipo = 0
        for empleado in self.equipo:
            total_equipo += empleado.calcular_salario()
            
        bono = total_equipo * 0.15
        return self._salario_base + bono
    
    def agregar_al_equipo(self, empleado):
        if isinstance(empleado, (desarrollador, diseñador)):
            if empleado not in self.equipo:
                self.equipo.append(empleado)
                print(f"{empleado._nombre} agregado al equipo de {self._nombre}")
            else:
                print(f"{empleado._nombre} ya esta en el equipo")
        else:
            print("solo se pueden agregar desarrolladores o diseñadores al equipo")
    
    def asignar_proyecto(self, proyecto):
        print(f"error: los gerentes como {self._nombre} no pueden asignarse a proyectos")
        return False

class proyecto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        if empleado in self.empleados:
            print(f"error: {empleado._nombre} ya esta en el proyecto {self.nombre}")
            return False
            
        self.empleados.append(empleado)
        print(f"{empleado._nombre} agregado al proyecto {self.nombre}")
        return True
    
    def costo_total(self):
        total = 0
        for emp in self.empleados:
            total += emp.calcular_salario()
        return total
    
    def viabilidad(self):
        costo = self.costo_total()
        presupuesto_70 = self.presupuesto * 0.7
        
        if costo <= presupuesto_70:
            return True
        else:
            return False

def procesar_empleados(lista_empleados):
    print("informacion de empleados:")
    for emp in lista_empleados:
        emp.mostrar_informacion()

# prueba del sistema
print("=== creando empleados ===")

# crear gerente
gerente1 = gerente("nestor charris", 4000, "desarrollo")

# crear desarrolladores
dev1 = desarrollador("cristian rodriguez", 3000, "senior", ["python", "go"])
dev2 = desarrollador("maria martinez", 2500, "junior", ["php"])

# crear diseñador
dis1 = diseñador("laura silvio", 1900, ["figma", "photoshop"], "ui")

print("\n=== construyendo equipo ===")
# agregar empleados al equipo del gerente
gerente1.agregar_al_equipo(dev1)
gerente1.agregar_al_equipo(dev2)
gerente1.agregar_al_equipo(dis1)

print("\n=== creando proyectos ===")
# crear proyectos
proyecto1 = proyecto("ia", 10000)
proyecto2 = proyecto("telecomunicaciones", 8000)

print("\n=== asignando empleados a proyectos ===")
# asignar empleados a proyectos
dev1.asignar_proyecto(proyecto1)
dev2.asignar_proyecto(proyecto1)
dis1.asignar_proyecto(proyecto1)

dev1.asignar_proyecto(proyecto2)
dis1.asignar_proyecto(proyecto2)

print("\n=== viabilidad de proyectos ===")
# mostrar viabilidad
print(f"proyecto '{proyecto1.nombre}':")
print(f"  costo total: {proyecto1.costo_total()}")
print(f"  presupuesto (70%): {proyecto1.presupuesto * 0.7}")
print(f"  ¿es viable? {'si' if proyecto1.viabilidad() else 'no'}")

print(f"proyecto '{proyecto2.nombre}':")
print(f"  costo total: {proyecto2.costo_total()}")
print(f"  presupuesto (70%): {proyecto2.presupuesto * 0.7}")
print(f"  ¿es viable? {'si' if proyecto2.viabilidad() else 'no'}")

print("\n=== intentando asignar cuarto proyecto a desarrollador ===")
# intentar asignar un cuarto proyecto al desarrollador
proyecto3 = proyecto("proyecto extra 1", 5000)
proyecto4 = proyecto("proyecto extra 2", 4000)
proyecto5 = proyecto("proyecto extra 3", 3000)

dev1.asignar_proyecto(proyecto3)
dev1.asignar_proyecto(proyecto4) 

print("\n=== informacion final ===")
# procesar todos los empleados
todos_empleados = [gerente1, dev1, dev2, dis1]
procesar_empleados(todos_empleados)

# intentar asignar gerente a proyecto
print("=== intentando asignar gerente a proyecto ===")
gerente1.asignar_proyecto(proyecto1)