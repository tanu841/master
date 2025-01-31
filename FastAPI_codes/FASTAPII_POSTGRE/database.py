from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE='postgresql://postgres:password@localhost:5432/QuizApplicationYT'
#URL_DATABASE='postgresql://postgres:password@localhost:5432/QuizApplicationYT'

engine=create_engine(URL_DATABASE)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
#pip install psycopg2-binary
#cd FASTAPII_POSTGRE
#uvicorn main:app --reload