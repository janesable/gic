from flask import Flask, render_template, request, jsonify
from typing import List

app = Flask(__name__)

def find_min_inversions(seq1, seq2):
    steps = []  # Список для записи каждого шага инверсии
    current_seq = seq1.copy()  # Копируем начальную последовательность

    for i in range(len(seq2)):
        if current_seq[i] != seq2[i]:
            try:
                target_index = current_seq.index(seq2[i])
            except ValueError:
                target_index = current_seq.index(-seq2[i])

            current_seq[i:target_index+1] = reversed([-x for x in current_seq[i:target_index+1]])
            steps.append(current_seq.copy())  # Записываем текущую последовательность после инверсии

    return steps

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    sequences = data["sequences"]
    names = data["names"]
    
    results = []
    for i in range(len(sequences) - 1):
        seq1 = sequences[i]
        seq2 = sequences[i + 1]
        steps = find_min_inversions(seq1, seq2)
        results.append({
            "from": names[i],
            "to": names[i + 1],
            "steps": steps,
            "min_inversions": len(steps)
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
