from sqlalchemy import Column, Integer, Text, DateTime, CHAR
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Vacancies(Base):
    """Модель таблицы Vacancies базы данных"""

    __tablename__ = 'vacancies'

    id = Column(Integer, primary_key=True)
    company_name = Column(Text, nullable=False)
    city = Column(Text, nullable=False)
    vacancy_name = Column(Text, nullable=False)
    salary_from = Column(Integer)
    salary_to = Column(Integer)
    salary_currency = Column(CHAR(3))
    work_experience = Column(Text, nullable=False)
    employment = Column(Text)
    published_at = Column(DateTime, nullable=False)
    vacancy_url = Column(Text, nullable=False)
    requirement = Column(Text)
    responsibility = Column(Text)
