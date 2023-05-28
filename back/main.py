#!/usr/bin/env python

import os
import requests
import json
import logging

from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi import FastAPI, Depends, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .settings import settings
from .routes import router as api_router
from .database import Base, engine

# Logging
log = logging.getLogger("fastapi")

# Create database
Base.metadata.create_all(bind=engine)

# Create server
app = FastAPI(debug=True, docs_url="/index.html")

# CORS config
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
# app.middleware("http")(response_handler)

log.info("Starting server")

# docs endpoint
app.add_api_route("/", endpoint=lambda: RedirectResponse(url="/index.html"), include_in_schema=False)
app.add_api_route("/docs", endpoint=lambda: RedirectResponse(url="/index.html"), include_in_schema=False)

# api routes
app.include_router(api_router, prefix = "/api")

# router.include_router(auth_user, prefix="/auth", tags=["auth"])

# @app.post("/sigu`", status_code=201, tags = ["auth"])
# def register(auth_details: schemas.RegisterAuthDetails, db: Session = Depends(get_database)):
#     if auth_user.get_auth_user_by_username(db, auth_details.username):
#         raise HTTPException(status_code=400, detail="Username is taken")

#     hashed_password = auth_handler.get_password_hash(auth_details.password)
    
#     auth_user.create_auth_user(db, {
#         "username": auth_details.username,
#         "password": hashed_password    
#     })

#     return Response(status_code = 200)


# @app.post("/users/validate", tags = ["users"])
# async def validate(auth = Depends(auth_handler.auth_wrapper), user_data: schemas.UnverifiedUser = None, db: Session = Depends(get_database)):
#     """# validate
#     Iniciar proceso de validación de un usuario de discord. 
#     Recibe vía post un usuario que recién ingresa al servidor, y aún no validó su usuario de discord,
#     se encarga de notificar a administración para que maneje este evento.

#     endpoint data
#     -----------
#     route: /user/validate \n
#     allowed methods: POST \n

#     responses
#     -----------
#     400
#         Bad request
#     401 
#         Unauthorized
#     422
#         No existe el usuario en la base de datos de administración
#     500
#         Internal server error
#     """

#     log.info(f"Validando usuario {user_data.discord_tag}...")

#     # Notificar a administracion
#     admin_response = requests.post(url = ADMIN_URL + f"/perfil/chat/user/reset/", 
#                                    headers = ADMIN_HEADERS, 
#                                    json = dict(user_data))

#     if admin_response.status_code >= 400:
#         if admin_response.status_code == 422 or admin_response.status_code == 400:
#             log.error("Error - El mail no está registrado en inove")
#             return JSONResponse(status_code = 422, content = {"message": "El usuario no existe en la base de datos de administración"})
#         else:
#             log.error(f"Error: {[admin_response.status_code]} - {admin_response.text}")
#             return JSONResponse(status_code = 500, content = {"message": "Internal server error"})

#     log.info(f"Valid email, user: {admin_response.text}")
#     already_registered_user = user.get_user_by_discord_id(db, user_data.chat_user)

#     if already_registered_user:
#         if already_registered_user.verified:
#             log.info(f"El usuario {user_data.chat_user} ya estaba registrado y verificado (ya tiene acceso a todos los canales")
#             return JSONResponse(status_code = 209, content = {"message": "El usuario ya está registrado"})

#         log.info(f"El usuario {user_data.chat_user} ya estaba registrado, pero no verificado (no tiene acceso a los canales")
#         return JSONResponse(status_code = 200, content = {"message": "El usuario ya estaba registrado, de todas se le envió un mail de validación"})
    
#     # Guardar datos de nuevo usuario de discord
#     db_user = user.create_user(db, False, **dict(user_data))

#     log.info(f"Se creó el usuario de discord {user_data.discord_tag} exitosamente")

#     return JSONResponse(status_code = 201, content = model_to_dict(db_user))



