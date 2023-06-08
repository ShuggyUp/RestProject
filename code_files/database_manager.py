from sqlalchemy import insert
from sqlalchemy.orm import Session
from datetime import datetime
from abc import ABC, abstractmethod
from sqlalchemy import Engine
from models.models import Base
from typing import Optional


class DatabaseManager(ABC):
    """Интерфейс взаимодействия с базой данных"""

    def __init__(self, engine: Engine, model: Base):
        """Инициализирует базовые значения"""
        self._engine = engine
        self._model = model

    @abstractmethod
    def get_data(self, limit_record: int, keywords: str):
        """Возвращает записи из базы данных"""

    @abstractmethod
    def append_data(self, data_dict):
        """Добавляет новые записи в базу данных"""


class VacanciesDatabaseManager(DatabaseManager):
    """Интерфейс взаимодействия с таблицей Vacancies"""

    def get_data(self, limit_record: int, keywords: str) -> list[Base]:
        """Возвращает записи из базы данных"""
        with Session(bind=self._engine) as session:
            valid_data: list[Base] = session.query(self._model).filter(self._model.vacancy_name.like(
                keywords)).order_by(self._model.published_at.desc()).limit(limit_record).all()

        return valid_data

    def append_data(self, data: list[dict]) -> None:
        """Добавляет новые записи в базу данных"""
        with Session(bind=self._engine) as session:
            session.execute(insert(self._model), data)
            session.commit()

    def get_last_record_date(self) -> datetime:
        """Возвращает дату публикации последней вакансии"""
        with Session(bind=self._engine) as session:
            last_record_date: Optional[tuple] = session.query(self._model.published_at).order_by(
                self._model.published_at.desc()).first()

            last_record_date_datetime_form: datetime
            if last_record_date is None:
                last_record_date_datetime_form = datetime.strptime('2000-01-01 01:01:01', '%Y-%m-%d %H:%M:%S')
            else:
                last_record_date_datetime_form = last_record_date[0]

        return last_record_date_datetime_form
