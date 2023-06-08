from fastapi import FastAPI
from code_files.vacancies_handler_api import VacanciesHandlerAPI
from code_files.database_manager import VacanciesDatabaseManager
from sqlalchemy import create_engine, Engine
from config import db_settings
from models.models import *
from models.api_models import *

app = FastAPI()


@app.get('/', response_model=VacanciesResponse)
def print_vacancies() -> dict:
    """Выводит все данные о вакансиях"""
    engine: Engine = create_engine(f'postgresql://{db_settings.db_user}:{db_settings.db_pass}@{db_settings.db_host}:'
                                   f'{db_settings.db_port}/{db_settings.db_name}')
    vacancies_db_manager: Base = VacanciesDatabaseManager(engine, Vacancies)
    vacancies_handler_api: VacanciesHandlerAPI = VacanciesHandlerAPI(vacancies_db_manager)

    return vacancies_handler_api.select_data_from_db(limit_record=30)


@app.get('/search-vacancies', response_model=VacanciesResponse)
def search_vacancies(search_text: str = 'Разработчик') -> dict:
    """Выводит все данные о вакансиях, в имени которых содержатся указанные ключевые слова"""
    engine: Engine = create_engine(f'postgresql://{db_settings.db_user}:{db_settings.db_pass}@{db_settings.db_host}:'
                                   f'{db_settings.db_port}/{db_settings.db_name}')
    vacancies_db_manager: Base = VacanciesDatabaseManager(engine, Vacancies)
    vacancies_handler_api: VacanciesHandlerAPI = VacanciesHandlerAPI(vacancies_db_manager)

    keywords_like_query: str = '%' + '%'.join(search_text.lower().split()) + '%'

    return vacancies_handler_api.select_data_from_db(keywords=keywords_like_query)


@app.post('/parse-new-vacancies')
def check_and_parse_new_vacancies() -> dict:
    """Проверяет наличие новых вакансий и добавляет их в базу данных"""
    engine: Engine = create_engine(f'postgresql://{db_settings.db_user}:{db_settings.db_pass}@{db_settings.db_host}:'
                                   f'{db_settings.db_port}/{db_settings.db_name}')
    vacancies_db_manager: Base = VacanciesDatabaseManager(engine, Vacancies)
    vacancies_handler_api: VacanciesHandlerAPI = VacanciesHandlerAPI(vacancies_db_manager)

    vacancies_handler_api.parse_vacancies_to_db()

    return {'code': 200, 'message': 'Данные успешно добавлены'}
