# registro_usuarios.py - Sistema de registro que usa validaciones.py

import validaciones as val
import json
import os
from datetime import datetime

def registrar_usuario():
    """Función para registrar un nuevo usuario usando las validaciones"""
    print("\n" + "="*50)
    print("📝 REGISTRO DE NUEVO USUARIO")
    print("="*50)
    
    # Validar nombre
    while True:
        nombre = input("\n👤 Nombre completo: ")
        if val.validar_no_vacio(nombre):
            break
        print("❌ El nombre no puede estar vacío")
    
    # Validar email
    while True:
        email = input("📧 Email: ")
        if val.validar_email(email):
            break
        print("❌ Email inválido (debe contener @ y .)")
    
    # Validar edad
    while True:
        edad = input("🎂 Edad: ")
        if val.validar_edad(edad):
            edad = int(edad)
            break
        print("❌ Edad inválida (debe estar entre 0 y 120)")
    
    # Validar teléfono
    while True:
        telefono = input("📱 Teléfono: ")
        if val.validar_telefono(telefono):
            break
        print("❌ Teléfono inválido (mínimo 8 dígitos, solo números)")
    
    # Validar calificación (ejemplo de rango)
    while True:
        calificacion = input("⭐ Calificación (1-10): ")
        if val.validar_rango(calificacion, 1, 10):
            calificacion = int(calificacion)
            break
        print("❌ Calificación inválida (debe ser entre 1 y 10)")
    
    # Mostrar resumen
    print("\n" + "="*50)
    print("✅ DATOS VALIDADOS CORRECTAMENTE")
    print("="*50)
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Edad: {edad}")
    print(f"Teléfono: {telefono}")
    print(f"Calificación: {calificacion}")
    
    return {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "telefono": telefono,
        "calificacion": calificacion,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    """Función principal del programa"""
    while True:
        print("\n" + "="*50)
        print("📋 MENÚ PRINCIPAL")
        print("="*50)
        print("1. Registrar nuevo usuario")
        print("2. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            usuario = registrar_usuario()
            print("\n🎉 ¡Usuario registrado exitosamente!")
        elif opcion == "2":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    main()