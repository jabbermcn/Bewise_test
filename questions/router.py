from fastapi import APIRouter
import requests

from questions.models import QuestionRequest, Question, SessionLocal

router = APIRouter()


@router.post("/get_questions/")
def get_questions(request_data: QuestionRequest):
    questions = []
    while len(questions) < request_data.questions_num:
        response = requests.get("https://jservice.io/api/random?count=1")
        data = response.json()
        question_data = data[0]

        with SessionLocal() as db:
            existing_question = db.query(Question).filter_by(question_text=question_data["question"]).first()
            if not existing_question:
                new_question = Question(
                    question_text=question_data["question"],
                    answer_text=question_data["answer"]
                )
                db.add(new_question)
                db.commit()
                db.refresh(new_question)
                questions.append(new_question)
    return questions
