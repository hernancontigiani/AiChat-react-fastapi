#!/usr/bin/env python

from fastapi import APIRouter

from . import controller

router = APIRouter()


router.get("/", status_code = 200)(controller.getAll)
router.post("/", status_code = 201)(controller.create)
router.get("/{id}", status_code = 200)(controller.get)
router.post("/{id}/message", status_code = 201)(controller.create_message)

