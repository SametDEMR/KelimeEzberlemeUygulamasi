import sqlite3
import random

conn = sqlite3.connect("database/Kelimeler.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM kelimeler ORDER BY RANDOM() LIMIT 5")
rows = cursor.fetchall()
conn.close()

questions = []
for row in rows:
    id, word, translation, sentence_en, sentence_tr, image_path = row
    correct_answer = translation
    other_answers = [r[2] for r in rows if r[0] != id]  # Diğer doğru cevapları al
    wrong_answers = random.sample(other_answers, 2)  # Rastgele 2 yanlış cevap seç
    random_number = random.randint(1, 3)

    choices = {}
    if random_number == 1:
        choices = {
            "şık1": correct_answer,
            "şık2": wrong_answers[0],
            "şık3": wrong_answers[1]
        }
    elif random_number == 2:
        choices = {
            "şık1": wrong_answers[0],
            "şık2": correct_answer,
            "şık3": wrong_answers[1]
        }
    else:
        choices = {
            "şık1": wrong_answers[0],
            "şık2": wrong_answers[1],
            "şık3": correct_answer
        }

    question = {
        "word": word,
        "sentence": sentence_tr,
        "choices": choices
    }
    questions.append(question)

for idx, question in enumerate(questions, 1):
    print(f"{question['word']}")
    print(f"{question['sentence']}")
    for choice, answer in question['choices'].items():
        print(f"{answer}")
    print()
