#!/usr/bin/env python
from fastapi import Depends, Response, HTTPException
from pydantic import BaseModel

from .models import Chat, Message

from sqlalchemy.orm import Session
from back.database import get_database

from back.auth.AuthHandler import auth_handler

class ChatDetails(BaseModel):
    name: str

class MessageDetails(BaseModel):
    message: str


async def getAll(user_id = Depends(auth_handler.auth_wrapper), db: Session = Depends(get_database)):
    chats = db.query(Chat).filter(Chat.user_id == user_id)
    return [chat.serialize() for chat in chats]


async def create(user_id = Depends(auth_handler.auth_wrapper), db: Session = Depends(get_database), chat_detail: ChatDetails = Depends()):
    chat = Chat(user_id = user_id, name = chat_detail.name)
    db.add(chat)
    db.commit()

    return Response(status_code = 201)


async def get(chat_id: int, user_id = Depends(auth_handler.auth_wrapper), db: Session = Depends(get_database)):
    messages = db.query(Message).join(Message.chat).filter(Message.chat_id == chat_id, Chat.user_id == user_id)
    return [message.serialize() for message in messages]


async def create_message(chat_id: int, user_id = Depends(auth_handler.auth_wrapper), db: Session = Depends(get_database), message_detail: MessageDetails = Depends()):
    chat = db.query(Chat).filter(Chat.id == chat_id, Chat.user_id == user_id).first()
    if chat is None:
        raise HTTPException(status_code = 404, detail = "Chat not found")

    message = Message(
        chat_id = chat_id,
        user_message = message_detail.message,
        bot_message = f"Bot: {message_detail.message}"
    )
    db.add(message)
    db.commit()

    return Response(status_code = 201)



