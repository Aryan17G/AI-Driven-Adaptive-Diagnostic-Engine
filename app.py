from fastapi import FastAPI
from bson import ObjectId
import uuid

from database import sessions, questions
from adaptive import get_next_question, update_ability
from ai import generate_plan

app = FastAPI()



@app.post("/start-test")
def start_test():

    sid = str(uuid.uuid4())

    sessions.insert_one({
        "session_id": sid,
        "ability": 0.5,
        "history": []
    })

    return {"session_id": sid}


@app.get("/next-question/{sid}")
def next_question(sid: str):

    s = sessions.find_one({"session_id": sid})

    q = get_next_question(s["ability"])

    return {
        "id": str(q["_id"]),
        "question": q["question"],
        "options": q["options"],
        "difficulty": q["difficulty"]
    }


@app.post("/submit-answer")
def submit_answer(
    session_id: str,
    question_id: str,
    answer: str
):

    s = sessions.find_one({"session_id": session_id})

    q = questions.find_one(
        {"_id": ObjectId(question_id)}
    )

    correct = answer == q["correct_answer"]

    ability = update_ability(
        s["ability"],
        correct
    )

    sessions.update_one(
        {"session_id": session_id},
        {
            "$set": {"ability": ability},
            "$inc": {"questions_answered": 1},
            "$push": {
                "history": {
                    "topic": q["topic"],
                    "correct": correct
                }
            }
        }
    )

    return {
        "correct": correct,
        "ability": ability
    }


@app.get("/finish/{sid}")
def finish(sid: str):

    s = sessions.find_one({"session_id": sid})

    plan = generate_plan(
        s["ability"],
        s["history"]
    )

    return {
        "ability": s["ability"],
        "study_plan": plan
    }