from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Vacancy(BaseModel):
    """Модель для проверки записей, считанных с базы данных"""

    company_name: str
    city: str
    vacancy_name: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    salary_currency: Optional[str]
    work_experience: str
    employment: Optional[str]
    published_at: datetime
    vacancy_url: str
    requirement: Optional[str]
    responsibility: Optional[str]


class VacanciesResponse(BaseModel):
    """Модель для проверки ответа сервера на запрос предоставления записей из базы данных"""

    vacancies: dict[int, Vacancy]
