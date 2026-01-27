# Banco de preguntas Cisco Network Security
# Archivo único consolidado con metadatos

questions_all = [  # Todas las preguntas con metadatos
    {
        "id": 1,
        "type": "radio",
        "exam_type": ["practice", "real"],
        "question": "¿Cuál es el propósito principal de un firewall en la seguridad de red?",
        "image": None,
        "options": [
            "Aumentar la velocidad de la red",
            "Filtrar y controlar el tráfico de red basándose en reglas de seguridad",
            "Encriptar todas las contraseñas de los usuarios",
            "Eliminar todos los virus de la red"
        ],
        "correct": [1],
        "explanation": "Un firewall es una herramienta de seguridad que monitorea y controla el tráfico de red entrante y saliente basándose en reglas de seguridad predeterminadas."
    },
    {
        "id": 2,
        "type": "radio",
        "exam_type": ["practice", "real"],
        "question": "¿Qué protocolo se utiliza para establecer conexiones seguras en web?",
        "image": None,
        "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
        "correct": [2],
        "explanation": "HTTPS (HTTP Secure) es el protocolo utilizado para establecer conexiones seguras en la web, utilizando SSL/TLS para encriptar los datos."
    },
    {
        "id": 3,
        "type": "checkbox",
        "exam_type": ["practice", "real"],
        "question": "¿Cuáles de las siguientes son capas del modelo OSI? (Selecciona todas las correctas)",
        "image": None,
        "options": [
            "Capa de Aplicación",
            "Capa de Presentación",
            "Capa de Transformación",
            "Capa de Enlace de Datos",
            "Capa de Procesamiento"
        ],
        "correct": [0, 1, 3],
        "explanation": "El modelo OSI tiene 7 capas: Aplicación, Presentación, Sesión, Transporte, Red, Enlace de Datos y Física."
    },
    {
        "id": 4,
        "type": "checkbox",
        "exam_type": ["practice", "real"],
        "question": "¿Cuáles son medidas efectivas de seguridad en Cisco? (Selecciona todas las correctas)",
        "image": None,
        "options": [
            "Configurar contraseñas fuertes",
            "Deshabilitar servicios innecesarios",
            "Actualizar firmware regularmente",
            "No usar encriptación para acelerar"
        ],
        "correct": [0, 1, 2],
        "explanation": "Las medidas de seguridad efectivas incluyen contraseñas fuertes, deshabilitar servicios innecesarios y mantener el firmware actualizado."
    },
    {
        "id": 5,
        "type": "matching",
        "exam_type": ["practice", "real"],
        "question": "Relaciona cada protocolo con su puerto por defecto",
        "image": None,
        "left_items": ["HTTP", "HTTPS", "SSH", "Telnet", "DNS"],
        "right_items": ["80", "443", "22", "23", "53"],
        "correct": [0, 1, 2, 3, 4],
        "explanation": "HTTP usa puerto 80, HTTPS 443, SSH 22, Telnet 23 y DNS 53."
    },
    {
        "id": 6,
        "type": "matching",
        "exam_type": ["practice", "real"],
        "question": "Relaciona cada concepto de seguridad con su definición",
        "image": None,
        "left_items": ["Firewall", "VPN", "IDS", "SSL/TLS"],
        "right_items": [
            "Red Privada Virtual para conexiones seguras",
            "Sistema de Detección de Intrusiones",
            "Filtro de tráfico de red",
            "Protocolo de encriptación"
        ],
        "correct": [2, 0, 1, 3],
        "explanation": "Cada componente de seguridad tiene un rol específico en la protección de redes."
    },
    {
        "id": 7,
        "type": "radio",
        "exam_type": ["practice", "real"],
        "question": "¿Qué es una ACL (Access Control List) en Cisco?",
        "image": None,
        "options": [
            "Una lista de aplicaciones permitidas",
            "Un conjunto de reglas que permiten o deniegan tráfico de red",
            "Una copia de seguridad automática de datos",
            "Un protocolo de encriptación"
        ],
        "correct": [1],
        "explanation": "Una ACL es un conjunto de reglas que determina qué tráfico es permitido o denegado en una interfaz de red."
    },
    {
        "id": 8,
        "type": "radio",
        "exam_type": ["practice", "real"],
        "question": "¿Cuál es la principal diferencia entre VPN y Proxy?",
        "image": None,
        "options": [
            "VPN solo funciona en Windows",
            "VPN encripta todo el tráfico, Proxy solo redirige",
            "Proxy es más seguro que VPN",
            "No hay diferencia significativa"
        ],
        "correct": [1],
        "explanation": "VPN encripta todo el tráfico de red del usuario, mientras que un Proxy actúa como intermediario."
    },
    {
        "id": 9,
        "type": "radio",
        "exam_type": ["practice", "real"],
        "question": "¿Cuál es el rango de direcciones IP privadas en la Clase A?",
        "image": None,
        "options": [
            "10.0.0.0 a 10.255.255.255",
            "172.16.0.0 a 172.31.255.255",
            "192.168.0.0 a 192.168.255.255",
            "127.0.0.1 a 127.255.255.255"
        ],
        "correct": [0],
        "explanation": "El rango privado Clase A es 10.0.0.0 a 10.255.255.255."
    },
    {
        "id": 10,
        "type": "radio",
        "exam_type": ["practice", "real"],
        "question": "¿Qué es IDS en seguridad de redes?",
        "image": None,
        "options": [
            "Internet Data Service",
            "Intrusion Detection System",
            "Internal Diagnostic Server",
            "Integrated Directory Service"
        ],
        "correct": [1],
        "explanation": "IDS (Intrusion Detection System) es un sistema que monitorea el tráfico de red para detectar actividades maliciosas."
    }
]

# Funciones para filtrar preguntas
def get_questions_by_mode(mode):
    """Retorna preguntas según el modo seleccionado"""
    return [q for q in questions_all if mode in q.get('exam_type', [])]

# Crear alias para compatibilidad con app.py
questions_practice = get_questions_by_mode('practice')
questions_real = get_questions_by_mode('real')

print(f"Preguntas PRÁCTICA cargadas: {len(questions_practice)}")
print(f"Preguntas REAL cargadas: {len(questions_real)}")
print(f"Total de preguntas únicas: {len(questions_all)}")
