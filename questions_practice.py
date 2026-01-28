# Banco de preguntas Cisco Network Security - PRÁCTICA

questions_practice = [
    {
        "id": 1,
        "type": "radio",
        "question": "¿Cuál es el propósito principal de un firewall en la seguridad de red?",
        "image": "/static/images/prueba.jpg",
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
        "question": "¿Qué protocolo se utiliza para establecer conexiones seguras en web?",
        "image": "/static/images/prueba.jpg",
        "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
        "correct": [2],
        "explanation": "HTTPS (HTTP Secure) es el protocolo utilizado para establecer conexiones seguras en la web, utilizando SSL/TLS para encriptar los datos."
    },
    {
        "id": 3,
        "type": "checkbox",
        "question": "¿Cuáles de las siguientes son capas del modelo OSI? (Selecciona todas las correctas)",
        "image": "/static/images/prueba.jpg",
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
        "question": "¿Cuáles son medidas efectivas de seguridad en Cisco? (Selecciona todas las correctas)",
        "image": "/static/images/prueba.jpg",
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
        "question": "Relaciona cada protocolo con su puerto por defecto",
        "image": "/static/images/prueba.jpg",
        "left_items": ["HTTP", "HTTPS", "SSH", "Telnet", "DNS"],
        "right_items": ["80", "443", "22", "23", "53"],
        "correct": [0, 1, 2, 3, 4],
        "explanation": "HTTP usa puerto 80, HTTPS 443, SSH 22, Telnet 23 y DNS 53."
    },
    {
        "id": 6,
        "type": "matching",
        "question": "Relaciona cada concepto de seguridad con su definición",
        "image": "/static/images/prueba.jpg",
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
        "question": "¿Qué es una ACL (Access Control List) en Cisco?",
        "image": "/static/images/prueba.jpg",
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
        "question": "¿Cuál es la principal diferencia entre VPN y Proxy?",
        "image": "/static/images/prueba.jpg",
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
        "question": "¿Cuál es el rango de direcciones IP privadas en la Clase A?",
        "image": "/static/images/prueba.jpg",
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
        "question": "¿Qué es IDS en seguridad de redes?",
        "image": "/static/images/prueba.jpg",
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