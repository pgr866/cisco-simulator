# Cisco Network Security - Simulador de Examen

Simulador de preguntas tipo test para la certificación Cisco Network Security. Soporta tres tipos de preguntas: selección única, múltiple y arrastrar (matching).

## 🚀 Características

### Tres modos de estudio:

- **Simulacro de Examen**: 40 preguntas seleccionadas aleatoriamente
- **Responde a Todas las Preguntas**: Practica con el pool completo de preguntas

### Tipos de preguntas:

1. **Radio (selección única)**: Elige una opción correcta
2. **Checkbox (múltiples opciones)**: Selecciona todas las opciones correctas
3. **Matching (arrastrar)**: Relaciona conceptos con definiciones

### Funcionalidades:

- ✅ Interfaz responsiva y moderna
- ✅ Imágenes en preguntas
- ✅ Feedback visual inmediato
- ✅ Barra de progreso
- ✅ Sistema de puntuación (0-10) sin castigos
- ✅ Explicaciones para cada pregunta
- ✅ Interfaz intuitiva con drag & drop

## 📋 Estructura del Proyecto

```
cisco-simulator/
├── app.py                  # Aplicación Flask principal
├── questions.py            # Base de datos de preguntas
├── requirements.txt        # Dependencias
├── static/
│   ├── style.css          # Estilos CSS
│   ├── script.js          # Lógica del cliente
│   └── images/            # Imágenes para preguntas
└── templates/
    ├── index.html         # Página de inicio
    └── quiz.html          # Interfaz del cuestionario
```

## 🛠️ Instalación y Ejecución

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación

```bash
python app.py
```

### 3. Abrir en el navegador

```
http://127.0.0.1:5000/
```

## 📝 Estructura de Preguntas

### Pregunta de Radio (una selección):

```python
{
    "id": 1,
    "type": "radio",
    "question": "¿Cuál es el propósito principal de un firewall?",
    "image": None,
    "options": [
        "Opción 1",
        "Opción 2",
        "Opción 3",
        "Opción 4"
    ],
    "correct": [1],  # Índice de la opción correcta
    "explanation": "Explicación..."
}
```

### Pregunta de Checkbox (múltiples opciones):

```python
{
    "id": 3,
    "type": "checkbox",
    "question": "¿Cuáles son correctas? (Selecciona todas)",
    "image": None,
    "options": ["Opción 1", "Opción 2", "Opción 3"],
    "correct": [0, 2],  # Índices de opciones correctas
    "explanation": "Explicación..."
}
```

### Pregunta de Matching (arrastrar):

```python
{
    "id": 5,
    "type": "matching",
    "question": "Relaciona cada concepto con su definición",
    "image": None,
    "left_items": ["HTTP", "HTTPS", "SSH"],
    "right_items": ["80", "443", "22"],
    "correct": [0, 1, 2],  # Mapeo correcto
    "explanation": "Explicación..."
}
```

## 🖼️ Agregar Imágenes

1. Coloca la imagen en `static/images/`
2. En la pregunta, usa:

```python
"image": "/static/images/router.png"
```

## 📊 Sistema de Puntuación

```
Puntuación = (Correctas / Total) * 10
```

**Nota:** Las respuestas incorrectas NO restan puntos.

## 🎨 Personalización

### Cambiar colores y estilos

Edita `static/style.css` para personalizar la interfaz.

### Agregar/Modificar preguntas

Edita `questions.py` y agrega nuevas preguntas en la lista.

## 🔧 Tecnologías

- **Flask** - Backend web
- **Python** - Lógica del servidor
- **HTML/CSS/JavaScript** - Frontend
- **Jinja2** - Motor de plantillas

## 📄 Licencia

MIT - Libre para usar y modificar

## 👨‍💻 Autor

Simulador desarrollado para estudiantes de Cisco Network Security
