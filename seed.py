from database import questions

data = [
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "correct_answer": "4",
        "difficulty": 0.2,
        "topic": "Algebra",
        "tags": ["easy"]
    },
    {
        "question": "5 * 4 = ?",
        "options": ["30", "20", "25", "40"],
        "correct_answer": "20",
        "difficulty": 0.3,
        "topic": "Algebra",
        "tags": ["easy"]
    },
    {
        "question": "12 / 3 = ?",
        "options": ["2", "3", "4", "6"],
        "correct_answer": "4",
        "difficulty": 0.3,
        "topic": "Algebra",
        "tags": ["easy"]
    },
    {
        "question": "Capital of France?",
        "options": ["Paris", "Rome", "Berlin", "Madrid"],
        "correct_answer": "Paris",
        "difficulty": 0.4,
        "topic": "GK",
        "tags": ["medium"]
    },
    {
        "question": "7^2 = ?",
        "options": ["49", "42", "36", "56"],
        "correct_answer": "49",
        "difficulty": 0.5,
        "topic": "Algebra",
        "tags": ["medium"]
    },
    {
        "question": "15 * 3 = ?",
        "options": ["30", "35", "45", "50"],
        "correct_answer": "45",
        "difficulty": 0.5,
        "topic": "Algebra",
        "tags": ["medium"]
    },
    {
        "question": "Square root of 81?",
        "options": ["7", "8", "9", "10"],
        "correct_answer": "9",
        "difficulty": 0.6,
        "topic": "Algebra",
        "tags": ["medium"]
    },
    {
        "question": "Derivative of x^2?",
        "options": ["x", "2x", "x^2", "2"],
        "correct_answer": "2x",
        "difficulty": 0.7,
        "topic": "Math",
        "tags": ["hard"]
    },
    {
        "question": "Integral of 1 dx?",
        "options": ["x", "1", "0", "x^2"],
        "correct_answer": "x",
        "difficulty": 0.7,
        "topic": "Math",
        "tags": ["hard"]
    },
    {
        "question": "Speed formula?",
        "options": ["d/t", "t/d", "d*t", "t+d"],
        "correct_answer": "d/t",
        "difficulty": 0.4,
        "topic": "Physics",
        "tags": ["medium"]
    },
    {
        "question": "Force formula?",
        "options": ["m*a", "m/d", "a/m", "d*a"],
        "correct_answer": "m*a",
        "difficulty": 0.5,
        "topic": "Physics",
        "tags": ["medium"]
    },
    {
        "question": "H2O is?",
        "options": ["Water", "Oxygen", "Hydrogen", "Salt"],
        "correct_answer": "Water",
        "difficulty": 0.2,
        "topic": "Chemistry",
        "tags": ["easy"]
    },
    {
        "question": "NaCl is?",
        "options": ["Salt", "Water", "Acid", "Base"],
        "correct_answer": "Salt",
        "difficulty": 0.3,
        "topic": "Chemistry",
        "tags": ["easy"]
    },
    {
        "question": "Planet closest to Sun?",
        "options": ["Mercury", "Earth", "Mars", "Venus"],
        "correct_answer": "Mercury",
        "difficulty": 0.4,
        "topic": "GK",
        "tags": ["medium"]
    },
    {
        "question": "Largest planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": "Jupiter",
        "difficulty": 0.5,
        "topic": "GK",
        "tags": ["medium"]
    },
    {
        "question": "Binary of 2?",
        "options": ["10", "11", "01", "00"],
        "correct_answer": "10",
        "difficulty": 0.6,
        "topic": "CS",
        "tags": ["medium"]
    },
    {
        "question": "Binary of 3?",
        "options": ["10", "11", "01", "00"],
        "correct_answer": "11",
        "difficulty": 0.6,
        "topic": "CS",
        "tags": ["medium"]
    },
    {
        "question": "HTML stands for?",
        "options": ["HyperText Markup Language", "HighText", "Home Tool", "None"],
        "correct_answer": "HyperText Markup Language",
        "difficulty": 0.3,
        "topic": "CS",
        "tags": ["easy"]
    },
    {
        "question": "CPU means?",
        "options": ["Central Processing Unit", "Computer Unit", "Core Unit", "None"],
        "correct_answer": "Central Processing Unit",
        "difficulty": 0.3,
        "topic": "CS",
        "tags": ["easy"]
    },
    {
        "question": "RAM is?",
        "options": ["Memory", "Disk", "CPU", "GPU"],
        "correct_answer": "Memory",
        "difficulty": 0.4,
        "topic": "CS",
        "tags": ["easy"]
    },
    {
        "question":"The atomic number of which of the following element is more than that of iron?",
        "options":["Manganese","Cobalt","Calcium","Chromium"],
        "correct_answer":"Cobalt",
        "difficulty": 0.7,
        "topic":"Chemistry",
        "tags":["hard"]
    },
    {
        "question": "The number of maximum electrons in N shell is?",
        "options": ["2", "8", "18", "32"],
        "correct_answer": "32",
        "difficulty": 0.7,
        "topic": "Chemistry",
        "tags": ["hard"]
    },
    {  
        "question": "The basic principle of nuclear reactors is?",
        "options": ["fusion", "radioactivity", "fission", "none of these"],
        "correct_answer": "fission",
        "difficulty": 0.8,
        "topic": "Chemistry",
        "tags": ["hard"]
    },
    {
        "question": "Which of the following the unit of radioactivity?",
        "options": ["Angstrom", "Candela", "fermi", "Curie"],
        "correct_answer": "Curie",
        "difficulty": 0.9,
        "topic": "Chemistry",
        "tags": ["hard"]
    },
    {
        "question": "Light waves are?",
        "options": ["electric waves", "magnetic waves", "electromagnetic waves", "no option is correct"],
        "correct_answer": "electromagnetic waves",
        "difficulty": 0.8,
        "topic": "Phy",
        "tags": ["hard"]
    },
    { 
        "question": "Sound is produced due to?",
        "options": ["refraction", "vibration", "rotation", "reflection"],
        "correct_answer": "vibration",
        "difficulty": 0.8,
        "topic": "Phy",
        "tags": ["hard"]
    },
    {
        "question": "The visible portion of the electromagnetic spectrum is?",
        "options": ["infrared", "radio wave", "microwave", "light"],
        "correct_answer": "light",
        "difficulty": 1.0,
        "topic": "Phy",
        "tags": ["hard"]
    },
    {
        "question": "Which one of the following waves is used for detection forgery in currency notes?",
        "options": ["UV waves", "infrared waves", "radio waves", "microwaves"],
        "correct_answer": "UV waves",
        "difficulty": 1.0,
        "topic": "Phy",
        "tags": ["hard"]
    },
    {  
        "question": "The waves used in common TV remote control are?",
        "options": ["X-ray", "UV ray", "infrared ray", "gamma ray"],
        "correct_answer": "infrared ray",
        "difficulty": 1.0,
        "topic": "Phy",
        "tags": ["hard"]
    }
]

questions.insert_many(data)

print("Inserted questions")