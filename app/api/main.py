from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.generation.rag import generate_answer


app = FastAPI(
    title="Enterprise Knowledge and Policy Assistant",
    description="RAG-based enterprise policy assistant",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Enterprise Knowledge and Policy Assistant is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        answer, metadatas = generate_answer(request.question)

        sources = list({
            metadata["source"]
            for metadata in metadatas
        })

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing question: {str(error)}"
        )