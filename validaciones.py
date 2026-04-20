# validaciones.py - Validaciones comunes en Python

def validar_no_vacio(texto):
    return len(texto.strip()) > 0

def validar_email(email):
    return "@" in email and "." in email

def validar_edad(edad):
    try:
        edad = int(edad)
        return 0 <= edad <= 120
    except:
        return False

def validar_telefono(tel):
    return tel.isdigit() and len(tel) >= 8

def validar_rango(valor, minimo, maximo):
    try:
        valor = int(valor)
        return minimo <= valor <= maximo
    except:
        return False

# EJEMPLOS DE USO
if __name__ == "__main__":
    print("=== VALIDADOR RÁPIDO ===\n")
    
    # Prueba 1: Campo vacío
    nombre = input("Nombre: ")
    print("✅ Válido" if validar_no_vacio(nombre) else "❌ No puede estar vacío")
    
    # Prueba 2: Email
    email = input("Email: ")
    print("✅ Válido" if validar_email(email) else "❌ Email inválido (falta @ o .)")
    
    # Prueba 3: Edad
    edad = input("Edad: ")
    print("✅ Válida" if validar_edad(edad) else "❌ Edad inválida (0-120)")
    
    # Prueba 4: Teléfono
    telefono = input("Teléfono (solo números): ")
    print("✅ Válido" if validar_telefono(telefono) else "❌ Mínimo 8 dígitos")