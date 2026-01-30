from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from questions_practice import questions_practice
from questions_real import questions_real
import random

print(f"Preguntas de PRUEBA cargadas: {len(questions_practice)}")
print(f"Preguntas REAL cargadas: {len(questions_real)}")

app = Flask(__name__)
app.secret_key = "cisco_network_security_key_2025"

@app.route('/')
def index():
    """Home page with mode selection"""
    failed_questions = session.get('failed_questions', [])
    return render_template('index.html', failed_count=len(failed_questions))

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    """Initialize the quiz based on selected mode"""
    mode = request.form.get('mode')  # practice, real, combined, failed
    
    # IMPORTANTE: Guardar preguntas fallidas ANTES de limpiar la sesión
    failed_ids = session.get('failed_questions', [])
    
    # Reset session data
    session.clear()
    
    # Restaurar preguntas fallidas después de limpiar
    session['failed_questions'] = failed_ids
    
    # Select questions based on mode
    if mode == 'practice':
        question_pool = questions_practice.copy()
        session['mode'] = 'Examen de Práctica (64 preguntas)'
    elif mode == 'real':
        question_pool = questions_real.copy()
        session['mode'] = 'Examen Real (153 preguntas)'
    elif mode == 'combined':
        question_pool = (questions_practice + questions_real).copy()
        session['mode'] = 'Examen Combinado (217 preguntas)'
    elif mode == 'failed':
        # Preguntas que el usuario falló
        if not failed_ids:
            return redirect(url_for('index'))
        # Eliminar duplicados por ID - crear diccionario con ID como clave
        all_questions = {q['id']: q for q in (questions_practice + questions_real)}
        # Obtener solo las preguntas fallidas únicas
        question_pool = [all_questions[q_id] for q_id in failed_ids if q_id in all_questions]
        session['mode'] = f'Repasar Errores ({len(question_pool)} preguntas)'
    else:
        return redirect(url_for('index'))
    
    # Shuffle questions
    random.shuffle(question_pool)
    
    # Store question IDs instead of full questions
    session['question_ids'] = [q['id'] for q in question_pool]
    session['current_question'] = 0
    session['total_questions'] = len(question_pool)
    session['correct_answers'] = 0
    session['incorrect_answers'] = 0
    session['mode_type'] = mode
    
    print(f"Examen iniciado: {session['mode']}")
    print(f"Total de preguntas: {len(question_pool)}")
    print(f"Preguntas fallidas guardadas: {len(session['failed_questions'])}")
    
    session.modified = True
    return redirect(url_for('quiz'))

@app.route('/quiz_info')
def get_quiz_info():
    """Get current quiz info"""
    if 'question_ids' not in session:
        return jsonify({"error": "Quiz not initialized"}), 400
    
    return jsonify({
        "total_questions": session['total_questions'],
        "current_question": session['current_question'],
        "correct_answers": session['correct_answers'],
        "incorrect_answers": session.get('incorrect_answers', 0)
    })

@app.route('/quiz')
def quiz():
    """Show the quiz page"""
    if 'question_ids' not in session:
        return redirect(url_for('index'))
    
    return render_template('quiz.html', 
                          mode=session['mode'],
                          current=session['current_question'] + 1,
                          total=session['total_questions'],
                          correct=session['correct_answers'],
                          incorrect=session.get('incorrect_answers', 0))

@app.route('/get_question')
def get_question():
    """Return the current question data with randomized options"""
    if 'question_ids' not in session:
        return jsonify({"error": "Quiz not initialized"}), 400
    
    # Aceptar índice opcional desde query parameter
    index_param = request.args.get('index', type=int)
    current_idx = index_param if index_param is not None else session['current_question']
    
    # Actualizar current_question en la sesión
    session['current_question'] = current_idx
    
    # Check if we've reached the end of the quiz
    if current_idx >= session['total_questions']:
        return jsonify({
            "completed": True,
            "correct": session['correct_answers'],
            "incorrect": session.get('incorrect_answers', 0),
            "total": session['total_questions']
        })
    
    # Get question ID and fetch question
    question_id = session['question_ids'][current_idx]
    
    # Search question in both pools
    question_data = None
    for q in questions_practice + questions_real:
        if q['id'] == question_id:
            question_data = q
            break
    
    if not question_data:
        return jsonify({"error": "Question not found"}), 400
    
    question_type = question_data.get("type", "radio")
    
    response_data = {
        "id": question_data.get("id"),
        "type": question_type,
        "question": question_data["question"],
        "image": question_data.get("image"),
        "explanation": question_data.get("explanation", "")
    }
    
    # Handle different question types
    if question_type in ["radio", "checkbox"]:
        options = question_data["options"].copy()
        correct_indices = question_data["correct"]
        
        # Para ambos tipos (radio y checkbox), aleatorizar opciones
        # Crear pares de (opción, índice_original)
        option_pairs = [(options[i], i) for i in range(len(options))]
        random.shuffle(option_pairs)
        
        shuffled_options = [pair[0] for pair in option_pairs]
        # Mapear los índices correctos originales a los nuevos índices
        original_to_new = {pair[1]: new_idx for new_idx, pair in enumerate(option_pairs)}
        new_correct_indices = [original_to_new[orig_idx] for orig_idx in correct_indices]
        
        session[f'correct_idx_{current_idx}'] = new_correct_indices
        response_data["options"] = shuffled_options
        
        if question_type == "checkbox":
            response_data["num_correct"] = len(correct_indices)
    
    elif question_type == "matching":
        # Para matching, aleatorizar tanto left_items como right_items
        left_items = question_data["left_items"].copy()
        right_items = question_data["right_items"].copy()
        correct_mapping = question_data["correct"]
        
        # Aleatorizar left_items manteniendo el mapeo correcto
        left_pairs = list(enumerate(left_items))  # (índice_original, item)
        random.shuffle(left_pairs)
        
        shuffled_left_indices = [pair[0] for pair in left_pairs]
        shuffled_left_items = [pair[1] for pair in left_pairs]
        
        # Aleatorizar right_items
        right_pairs = list(enumerate(right_items))
        random.shuffle(right_pairs)
        
        shuffled_right_indices = [pair[0] for pair in right_pairs]
        shuffled_right_items = [pair[1] for pair in right_pairs]
        
        # Ajustar el mapeo correcto para los índices aleatorizados
        # Para cada posición nueva en left (0, 1, 2...), encontrar qué right_item debe corresponder
        adjusted_correct = []
        for new_left_idx in range(len(shuffled_left_indices)):
            original_left_idx = shuffled_left_indices[new_left_idx]
            original_right_idx = correct_mapping[original_left_idx]
            # Encontrar dónde quedó ese right_item en la lista aleatorizada
            new_right_idx = shuffled_right_indices.index(original_right_idx)
            adjusted_correct.append(new_right_idx)
        
        session[f'correct_idx_{current_idx}'] = adjusted_correct
        response_data["left_items"] = shuffled_left_items
        response_data["right_items"] = shuffled_right_items
    
    session.modified = True
    return jsonify(response_data)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    """Check if the answer is correct and allow changing answers"""
    if 'question_ids' not in session:
        return jsonify({"error": "Quiz not initialized"}), 400

    data = request.get_json()
    selected_options = data.get('selected')
    current_idx = session['current_question']

    # --- NUEVO: Verificar si ya fue respondida ---
    user_answers = session.get('user_answers', {})
    if str(current_idx) in user_answers:
        print(f"Question {current_idx} already answered - blocking duplicate")
        return jsonify({
            "error": "Esta pregunta ya ha sido respondida",
            "correct": False
        }), 400

    # Get the correct answer(s) from the session
    correct_options = session.get(f'correct_idx_{current_idx}')
    
    # Debug logging
    print(f"\n=== Checking Answer ===")
    print(f"Question Index: {current_idx}")
    print(f"Selected: {selected_options} (type: {type(selected_options)})")
    print(f"Correct: {correct_options} (type: {type(correct_options)})")

    # Handle different types of answers
    is_correct = False
    if isinstance(selected_options, dict):
        # Para matching: convertir dict a lista en orden
        # selected_options = {0: 1, 1: 0, 2: 2} -> [1, 0, 2]
        # Verificar que todos los índices estén presentes
        if isinstance(correct_options, list):
            num_items = len(correct_options)
            if len(selected_options) == num_items:
                selected_list = [selected_options.get(str(i)) if str(i) in selected_options else selected_options.get(i) for i in range(num_items)]
                print(f"Selected list: {selected_list}")
                is_correct = selected_list == correct_options
            else:
                print(f"Incomplete matching: {len(selected_options)} of {num_items} items matched")
                is_correct = False
        else:
            print(f"Error: Matching question but correct_options is not a list")
            is_correct = False
    elif isinstance(selected_options, list):
        # Para checkbox: comparar sets (correct_options debe ser lista)
        if isinstance(correct_options, list):
            print(f"Comparing checkbox: set({selected_options}) vs set({correct_options})")
            is_correct = set(selected_options) == set(correct_options)
        else:
            print(f"Error: Checkbox question but correct_options is not a list")
            is_correct = False
    else:
        # Para radio: comparación directa
        # Si correct_options es una lista de 1 elemento, extraerlo
        if isinstance(correct_options, list) and len(correct_options) == 1:
            correct_option = correct_options[0]
        else:
            correct_option = correct_options
        print(f"Comparing radio: {selected_options} vs {correct_option}")
        is_correct = selected_options == correct_option
    
    print(f"Is correct: {is_correct}")
    print("=" * 30)

    # Get the question ID and track failed questions
    question_id = session['question_ids'][current_idx]
    failed_questions = session.get('failed_questions', [])

    # Guardar la respuesta del usuario
    user_answers[str(current_idx)] = selected_options
    session['user_answers'] = user_answers

    # Actualizar contadores y fallidas
    if is_correct:
        session['correct_answers'] += 1
        # Si estaba en fallidas (de un test anterior), quitarla
        if question_id in failed_questions:
            failed_questions.remove(question_id)
            print(f"Question {question_id} removed from failed_questions (answered correctly)")
    else:
        session['incorrect_answers'] = session.get('incorrect_answers', 0) + 1
        # Agregar a fallidas solo si no está ya
        if question_id not in failed_questions:
            failed_questions.append(question_id)
            print(f"Question {question_id} added to failed_questions")
        else:
            print(f"Question {question_id} already in failed_questions")

    session['failed_questions'] = failed_questions
    session.modified = True

    print(f"Failed questions count: {len(failed_questions)}")
    print(f"Failed question IDs: {failed_questions}")

    return jsonify({
        "correct": is_correct,
        "correctOptions": correct_options,
        "nextQuestion": session['current_question'] < session['total_questions']
    })

@app.route('/results')
def results():
    """Show the final results"""
    if 'question_ids' not in session:
        return redirect(url_for('index'))
    
    # Calculate score (0-10 scale, NO PENALTIES for wrong answers)
    correct = session['correct_answers']
    total = session['total_questions']
    
    # Formula: (correct / total) * 10
    final_score = (correct / total) * 10
    failed_count = len(session.get('failed_questions', []))
    
    # Store failed questions in session for later use
    failed_ids = session.get('failed_questions', [])
    
    return render_template('quiz.html', 
                          mode=session['mode'],
                          current=session['total_questions'],
                          total=session['total_questions'],
                          correct=session['correct_answers'],
                          incorrect=session.get('incorrect_answers', 0),
                          failed_count=failed_count,
                          final_score=round(final_score, 2),
                          completed=True,
                          failed_ids=failed_ids)
if __name__ == '__main__':
    app.run(debug=True)