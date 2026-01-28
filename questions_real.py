# Banco de preguntas Cisco Network Security - REAL

questions_real = [
    {
        "id": 1001,
        "type": "radio",
        "question": "¿Cuál es el propósito principal de un firewall en la seguridad de red?",
        "image": "/static/images/carlitos.jpg",
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
        "id": 1002,
        "type": "radio",
        "question": "¿Qué protocolo se utiliza comúnmente para establecer conexiones VPN seguras?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "HTTP",
            "FTP",
            "IPsec",
            "SMTP"
        ],
        "correct": [2],
        "explanation": "IPsec (Internet Protocol Security) es un conjunto de protocolos diseñado para asegurar las comunicaciones IP mediante autenticación y encriptación, ampliamente utilizado en VPNs."
    },
    {
        "id": 1003,
        "type": "radio",
        "question": "¿Qué tipo de ataque implica enviar paquetes malformados a un sistema para causar su fallo?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "Phishing",
            "Man-in-the-middle",
            "DoS (Denial of Service)",
            "SQL Injection"
        ],
        "correct": [2],
        "explanation": "Un ataque de Denegación de Servicio (DoS) busca hacer que un sistema o servicio no esté disponible sobrecargándolo con tráfico malicioso o explotando vulnerabilidades."
    },
    {
        "id": 1004,
        "type": "radio",
        "question": "¿Cuál de las siguientes NO es una característica de los IDS (Intrusion Detection Systems)?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "Monitorear el tráfico de red",
            "Bloquear automáticamente ataques",
            "Detectar patrones sospechosos",
            "Generar alertas de seguridad"
        ],
        "correct": [1],
        "explanation": "Los IDS detectan y alertan sobre actividades sospechosas, pero no bloquean activamente. Para bloqueo automático se utilizan IPS (Intrusion Prevention Systems)."
    },
    {
        "id": 1005,
        "type": "radio",
        "question": "¿Qué significa AAA en el contexto de seguridad de redes Cisco?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "Access, Administration, Audit",
            "Authentication, Authorization, Accounting",
            "Automatic, Active, Available",
            "Advanced, Adaptive, Analysis"
        ],
        "correct": [1],
        "explanation": "AAA representa Authentication (autenticación), Authorization (autorización) y Accounting (contabilidad), un framework fundamental para el control de acceso en redes Cisco."
    },
    {
        "id": 1006,
        "type": "radio",
        "question": "¿Qué puerto utiliza por defecto el protocolo HTTPS?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "80",
            "443",
            "8080",
            "22"
        ],
        "correct": [1],
        "explanation": "HTTPS utiliza el puerto 443 por defecto para establecer conexiones seguras mediante SSL/TLS, mientras que HTTP utiliza el puerto 80."
    },
    {
        "id": 1007,
        "type": "radio",
        "question": "¿Cuál es la diferencia principal entre cifrado simétrico y asimétrico?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "El simétrico es más rápido pero menos seguro",
            "El simétrico usa la misma clave para cifrar y descifrar",
            "El asimétrico solo funciona con números",
            "No hay diferencia significativa"
        ],
        "correct": [1],
        "explanation": "El cifrado simétrico usa la misma clave para cifrar y descifrar, mientras que el asimétrico usa un par de claves (pública y privada)."
    },
    {
        "id": 1008,
        "type": "radio",
        "question": "¿Qué tecnología se utiliza para segmentar una red en dominios de broadcast más pequeños?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "Hub",
            "VLAN",
            "Repeater",
            "Firewall"
        ],
        "correct": [1],
        "explanation": "Las VLANs (Virtual Local Area Networks) permiten segmentar lógicamente una red física en múltiples redes virtuales, mejorando la seguridad y el rendimiento."
    },
    {
        "id": 1009,
        "type": "radio",
        "question": "¿Qué protocolo proporciona autenticación segura para el acceso remoto a dispositivos de red?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "Telnet",
            "SSH",
            "HTTP",
            "SNMP v1"
        ],
        "correct": [1],
        "explanation": "SSH (Secure Shell) proporciona un canal seguro y cifrado para el acceso remoto, reemplazando a Telnet que transmite información en texto plano."
    },
    {
        "id": 1010,
        "type": "radio",
        "question": "¿Cuál es el propósito de un DMZ (Demilitarized Zone) en una arquitectura de red?",
        "image": "/static/images/carlitos.jpg",
        "options": [
            "Aumentar la velocidad de Internet",
            "Aislar servidores públicos de la red interna",
            "Almacenar backups de seguridad",
            "Gestionar direcciones IP"
        ],
        "correct": [1],
        "explanation": "Una DMZ es una subred que aísla servidores de acceso público (web, email) de la red interna, agregando una capa adicional de seguridad."
    }
]