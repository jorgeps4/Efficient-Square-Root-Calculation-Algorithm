   # Método de Newton-Raphson estándar para calcular raíces cuadradas
def newton_raphson(a, tolerancia=1e-6):
    x = a / 2  # Estimación inicial
    while True:
        raiz = (x + a / x) / 2
        if abs(raiz - x) < tolerancia:
            return raiz
        x = raiz

# Tu algoritmo para calcular una aproximación de la raíz cuadrada
def tu_algoritmo(a, iteraciones=20):
    b = 1
    for i in range(1, iteraciones + 1):
        b = (b ** 3 + 3 * a * b) * i / ((a + 3 * b ** 2) * i)
    return b

# Número del cual queremos calcular la raíz cuadrada
a = 8

# Calcular la raíz cuadrada usando ambos métodos
raiz_estandar = newton_raphson(a)
raiz_tu_algoritmo = tu_algoritmo(a)

# Imprimir los resultados
print("Raíz cuadrada usando el método de Newton-Raphson estándar:", raiz_estandar)
print("Raíz cuadrada usando tu algoritmo:", raiz_tu_algoritmo)