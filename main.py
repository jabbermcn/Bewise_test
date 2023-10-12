from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import requests

app = FastAPI()

# Database settings
DATABASE_URL = "postgresql://postgres:postgres@my_postgres:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Database model
class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String)
    answer_text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


# Pydantic model for request
class QuestionRequest(BaseModel):
    questions_num: int


@app.post("/get_questions/")
def get_questions(request_data: QuestionRequest):
    questions = []
    while len(questions) < request_data.questions_num:
        # Make a request to the public quiz API
        response = requests.get("https://jservice.io/api/random?count=1")
        data = response.json()
        question_data = data[0]

        # Check if the same question already exists in the database
        with SessionLocal() as db:
            existing_question = db.query(Question).filter_by(question_text=question_data["question"]).first()
            if not existing_question:
                # If it's a new question, save it to the database
                new_question = Question(
                    question_text=question_data["question"],
                    answer_text=question_data["answer"]
                )
                db.add(new_question)
                db.commit()
                db.refresh(new_question)
                questions.append(new_question)
    return questions


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
