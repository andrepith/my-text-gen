from fastapi import APIRouter
from app.models.pydantic_schemas import ChatRequest, ChatResponse
from app.services.inference import get_chat_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = await get_chat_response(request.prompt)
    return ChatResponse(response=reply)
