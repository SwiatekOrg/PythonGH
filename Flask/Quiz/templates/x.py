DATA = {
    0: {
        "question": "Which one is correct team name in NBA?",
        "options": ["New York Bulls", "Los Angeles Kings", "Golden State Warriros", "Huston Rocket"],
        "answer": "Huston Rocket"},
    1: {
        "question": "5 + 7 = ?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    2: {
        "question": "12 - 8 = ?",
        "options": ["1", "2", "3", "4"]
        , "answer": "4"}}

for i in DATA.items():
    print(DATA[i]['question'])
    for a in DATA[i].items():
        print(DATA[i]['options'][a])