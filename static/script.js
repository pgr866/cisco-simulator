// script.js - Lógica principal del quiz
let currentQuestionIndex = 0;
let totalQuestions = 0;
let answers = {}; // Guardar respuestas por índice
let answered = {};  // Guardar si fue respondida
let currentQuestion = null;
let userAnswer = null;
let selectedLeftIndex = null;

// Inicializar
function initQuiz() {
    fetch('/quiz_info')
        .then(response => response.json())
        .then(data => {
            totalQuestions = data.total_questions;
            currentQuestionIndex = 0;
            displayCurrentQuestion();
        })
        .catch(error => {
            console.error('Error initializing quiz:', error);
            document.getElementById('question-text').textContent = 'Error cargando el quiz';
        });
}

function displayCurrentQuestion() {
    fetch(`/get_question?index=${currentQuestionIndex}`)
        .then(response => response.json())
        .then(data => {
            if (data.completed) {
                window.location.href = '/results';
                return;
            }
            currentQuestion = data;
            renderQuestion(data);
            updateNavigationButtons();
        })
        .catch(error => {
            console.error('Error loading question:', error);
            document.getElementById('question-text').textContent = 'Error cargando pregunta';
        });
}

function renderQuestion(question) {
    document.getElementById('question-text').textContent = question.question;
    document.getElementById('options-container').innerHTML = '';
    document.getElementById('feedback-container').style.display = 'none';

    // Actualizar progreso
    const percentage = ((currentQuestionIndex + 1) / totalQuestions) * 100;
    document.getElementById('progress-fill').style.width = percentage + '%';
    document.getElementById('question-counter').textContent = `Pregunta ${currentQuestionIndex + 1} de ${totalQuestions}`;

    // Mostrar/ocultar imagen
    if (question.image) {
        document.getElementById('question-image').src = question.image;
        document.getElementById('image-container').style.display = 'block';
    } else {
        document.getElementById('image-container').style.display = 'none';
    }

    // Renderizar según tipo
    if (question.type === 'radio') {
        renderRadio(question, document.getElementById('options-container'));
    } else if (question.type === 'checkbox') {
        renderCheckbox(question, document.getElementById('options-container'));
    } else if (question.type === 'matching') {
        renderMatching(question, document.getElementById('options-container'));
    }

    // Restaurar respuesta guardada si existe
    if (answers[currentQuestionIndex] !== undefined) {
        restoreAnswer(question.type, answers[currentQuestionIndex]);
    }

    // Restaurar feedback si ya fue respondida
    if (answered[currentQuestionIndex]) {
        showFeedback(question);
        document.getElementById('next-btn').style.display = 'none';
    } else {
        document.getElementById('next-btn').textContent = 'Responder';
        document.getElementById('next-btn').style.display = 'block';
    }
}

function renderRadio(question, container) {
    const div = document.createElement('div');
    div.className = 'radio-option';
    question.options.forEach((option, index) => {
        const label = document.createElement('label');
        label.style.display = 'block';
        label.style.marginBottom = '0.5rem';
        label.style.cursor = 'pointer';
        label.innerHTML = `
            <input type="radio" name="option" value="${index}" style="margin-right: 0.5rem;">
            ${option}
        `;
        label.addEventListener('click', () => {
            userAnswer = index;
        });
        div.appendChild(label);
    });
    container.appendChild(div);
}

function renderCheckbox(question, container) {
    // Añadir instrucción sobre cuántas opciones marcar
    const instruction = document.createElement('p');
    instruction.style.fontStyle = 'italic';
    instruction.style.color = '#666';
    instruction.style.marginBottom = '1rem';
    
    // Obtener el número de respuestas correctas desde el backend (si viene en la pregunta)
    // O mostrarlo genérico
    instruction.textContent = '(Selecciona todas las opciones correctas)';
    container.appendChild(instruction);
    
    const div = document.createElement('div');
    div.className = 'checkbox-group';
    question.options.forEach((option, index) => {
        const label = document.createElement('label');
        label.className = 'checkbox-item';
        label.innerHTML = `
            <input type="checkbox" value="${index}" style="margin-right: 0.5rem;">
            <span>${option}</span>
        `;
        const checkbox = label.querySelector('input');
        checkbox.addEventListener('change', () => {
            const checkboxes = container.querySelectorAll('input[type="checkbox"]:checked');
            userAnswer = Array.from(checkboxes).map(cb => parseInt(cb.value));
            console.log('Checkbox answer:', userAnswer); // Debug
        });
        div.appendChild(label);
    });
    container.appendChild(div);
}

function renderMatching(question, container) {
    // Añadir instrucción
    const instruction = document.createElement('p');
    instruction.style.fontStyle = 'italic';
    instruction.style.color = '#666';
    instruction.style.marginBottom = '1rem';
    instruction.textContent = '(Haz clic en un concepto de la izquierda, luego en "Enlazar" junto a su definición correcta en la derecha)';
    container.appendChild(instruction);
    
    const div = document.createElement('div');
    div.className = 'matching-container';

    // Inicializar userAnswer como objeto vacío
    userAnswer = {};

    // Columna izquierda
    const leftDiv = document.createElement('div');
    leftDiv.className = 'matching-column';
    leftDiv.innerHTML = '<h4>Conceptos:</h4>';
    question.left_items.forEach((item, index) => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'matching-item';
        itemDiv.textContent = item;
        itemDiv.dataset.leftIndex = index; // Guardar índice
        itemDiv.addEventListener('click', () => {
            document.querySelectorAll('.matching-item').forEach(el => el.classList.remove('selected'));
            itemDiv.classList.add('selected');
            selectedLeftIndex = index;
        });
        leftDiv.appendChild(itemDiv);
    });
    div.appendChild(leftDiv);

    // Columna derecha
    const rightDiv = document.createElement('div');
    rightDiv.className = 'matching-column';
    rightDiv.innerHTML = '<h4>Definiciones:</h4>';
    question.right_items.forEach((item, index) => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'matching-right-item';
        itemDiv.innerHTML = item;
        itemDiv.dataset.rightIndex = index; // Guardar índice
        
        const enlazarBtn = document.createElement('button');
        enlazarBtn.className = 'enlazar-btn';
        enlazarBtn.textContent = 'Enlazar';
        enlazarBtn.addEventListener('click', () => {
            if (selectedLeftIndex === null) {
                alert('Selecciona un concepto primero');
                return;
            }
            // Guardar el emparejamiento
            userAnswer[selectedLeftIndex] = index;
            console.log('Matching answer:', userAnswer); // Debug
            itemDiv.classList.add('matched');
            
            // Mostrar indicador visual en el concepto
            const leftItem = document.querySelector(`.matching-item[data-left-index="${selectedLeftIndex}"]`);
            if (leftItem) {
                leftItem.style.backgroundColor = '#4CAF50';
                leftItem.style.color = 'white';
            }
            
            document.querySelectorAll('.matching-item').forEach(el => el.classList.remove('selected'));
            selectedLeftIndex = null;
        });
        itemDiv.appendChild(enlazarBtn);
        rightDiv.appendChild(itemDiv);
    });
    div.appendChild(rightDiv);
    container.appendChild(div);
}

function restoreAnswer(type, savedAnswer) {
    if (type === 'radio') {
        const radio = document.querySelector(`input[type="radio"][value="${savedAnswer}"]`);
        if (radio) {
            radio.checked = true;
            userAnswer = savedAnswer;
        }
    } else if (type === 'checkbox') {
        savedAnswer.forEach(index => {
            const checkbox = document.querySelector(`input[type="checkbox"][value="${index}"]`);
            if (checkbox) checkbox.checked = true;
        });
        userAnswer = savedAnswer;
    } else if (type === 'matching') {
        userAnswer = savedAnswer;
        // Marcar los emparejamientos restaurados
        Object.entries(savedAnswer).forEach(([leftIdx, rightIdx]) => {
            const rightItems = document.querySelectorAll('.matching-right-item');
            if (rightItems[rightIdx]) {
                rightItems[rightIdx].classList.add('matched');
            }
            
            // Marcar el concepto de izquierda también
            const leftItem = document.querySelector(`.matching-item[data-left-index="${leftIdx}"]`);
            if (leftItem) {
                leftItem.style.backgroundColor = '#4CAF50';
                leftItem.style.color = 'white';
            }
        });
    }
}

function updateNavigationButtons() {
    const prevBtn = document.getElementById('prev-btn');
    const skipBtn = document.getElementById('skip-btn');
    const nextBtn = document.getElementById('next-btn');

    prevBtn.style.display = currentQuestionIndex > 0 ? 'block' : 'none';
    skipBtn.style.display = currentQuestionIndex < totalQuestions - 1 ? 'block' : 'none';
    
    if (currentQuestionIndex === totalQuestions - 1) {
        skipBtn.style.display = 'none';
    }
    
    // Cambiar estado del botón según si está respondida
    if (answered[currentQuestionIndex]) {
        nextBtn.style.display = 'none';
    } else {
        nextBtn.textContent = 'Responder';
        nextBtn.disabled = false;
        nextBtn.style.opacity = '1';
        nextBtn.style.display = 'block';
    }
}

function previousQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        userAnswer = null;
        selectedLeftIndex = null;
        displayCurrentQuestion();
    }
}

function nextQuestion() {
    // Permitir avanzar sin responder
    currentQuestionIndex++;
    if (currentQuestionIndex >= totalQuestions) {
        window.location.href = '/results';
    } else {
        userAnswer = null;
        selectedLeftIndex = null;
        displayCurrentQuestion();
    }
}

function saveAnswer() {
    answers[currentQuestionIndex] = userAnswer;
}

function submitAnswer() {
    // Si ya fue respondida, no permitir cambiar
    if (answered[currentQuestionIndex]) {
        alert('Esta pregunta ya ha sido respondida. Usa los botones de navegación para continuar.');
        return;
    }

    if (userAnswer === null || userAnswer === undefined || (typeof userAnswer === 'object' && Object.keys(userAnswer).length === 0)) {
        alert('Por favor selecciona una respuesta');
        return;
    }

    saveAnswer();
    answered[currentQuestionIndex] = true;

    fetch('/check_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            selected: userAnswer,
            type: currentQuestion.type 
        })
    })
    .then(response => response.json())
    .then(data => {
        showFeedback(currentQuestion, data.correct);
        
        // Obtener contadores actuales del servidor
        fetch('/quiz_info')
            .then(res => res.json())
            .then(info => {
                document.getElementById('correct-count').textContent = info.correct_answers;
                document.getElementById('incorrect-count').textContent = info.incorrect_answers;
            });

        // Ocultar botón después de responder
        document.getElementById('next-btn').style.display = 'none';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al verificar respuesta');
    });
}

function showFeedback(question, isCorrect = null) {
    const feedbackContainer = document.getElementById('feedback-container');
    const feedbackText = document.getElementById('feedback-text');
    const explanationText = document.getElementById('explanation-text');

    feedbackContainer.style.display = 'block';
    if (isCorrect !== null) {
        feedbackContainer.className = isCorrect ? 'feedback correct' : 'feedback incorrect';
        feedbackText.textContent = isCorrect ? '✅ Correcto' : '❌ Incorrecto';
    }
    explanationText.textContent = question.explanation || '';
}

function exitQuiz() {
    const modal = document.getElementById('exit-modal');
    document.getElementById('modal-correct').textContent = document.getElementById('correct-count').textContent;
    document.getElementById('modal-incorrect').textContent = document.getElementById('incorrect-count').textContent;
    document.getElementById('modal-answered').textContent = Object.keys(answered).length;
    document.getElementById('modal-total').textContent = totalQuestions;
    modal.classList.add('show');
}

function confirmExit() {
    window.location.href = '/';
}

function cancelExit() {
    document.getElementById('exit-modal').classList.remove('show');
}

// Iniciar
initQuiz();