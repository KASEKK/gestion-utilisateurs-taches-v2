# app/main.py
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from app.config import URL_DB
from app.models import Base
from sqlalchemy.orm import sessionmaker
from app.models.services.menu import Menu
from app.init_db import session, db_connected


if db_connected:
    menu = Menu(session)
    menu.affichage()
else:
    print("❌ La base de données n'est pas connectée.")