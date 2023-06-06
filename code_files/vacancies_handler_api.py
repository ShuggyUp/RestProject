import requests
import json
from code_files.database_manager import VacanciesDatabaseManager
from datetime import datetime


class VacanciesHandlerAPI:
    """Обработчик взаимодействий с API"""

    __request_headers: dict = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
    }
    __hh_api_params: dict = {
        'text': 'developer',
        'area': '113',
        'page': 0,
        'per_page': 50,
        'professional_role': ['156', '160', '10', '12', '150', '25', '165', '34', '36', '73', '155', '96', '164',
                              '104', '157', '107', '112', '113', '148', '114', '116', '121', '124', '125', '126'],
        'order_by': 'publication_time'
    }

    def __init__(self, db_manager: VacanciesDatabaseManager) -> None:
        """Инициализирует базовые значения"""
        self._db_manager = db_manager

    def select_data_from_db(self, limit_record: int = None, keywords: str = '%') -> dict:
        """Возвращает записи из базы данных"""
        vacancies = self._db_manager.get_data(limit_record, keywords)

        output_vacancies = {}
        counter = 0
        for vacancy in vacancies:
            output_vacancies[counter] = {
                'company_name': vacancy.company_name,
                'city': vacancy.city,
                'vacancy_name': vacancy.vacancy_name,
                'salary_from': vacancy.salary_from,
                'salary_to': vacancy.salary_to,
                'salary_currency': vacancy.salary_currency,
                'work_experience': vacancy.work_experience,
                'employment': vacancy.employment,
                'published_at': vacancy.published_at,
                'vacancy_url': vacancy.vacancy_url,
                'requirement': vacancy.requirement,
                'responsibility': vacancy.responsibility
            }
            counter += 1
        output_vacancies = {'vacancies': output_vacancies}
        return output_vacancies

    def parse_vacancies_to_db(self) -> None:
        """Запрашивает данные с API Head Hunter и добавляет их в базу данных"""
        server_response = requests.get('https://api.hh.ru/vacancies', self.__hh_api_params,
                                       headers=self.__request_headers)
        vacancies_info = json.loads(server_response.content.decode())

        last_date = self._db_manager.get_last_record_date()
        vacancy_data_for_save = []
        for vacancy_info in vacancies_info['items']:
            required_data = self.__select_required_data(vacancy_info)
            vacancy_date = datetime.strptime(required_data['published_at'], '%Y-%m-%d %H:%M:%S')
            if vacancy_date > last_date:
                vacancy_data_for_save.append(required_data)
            else:
                break

        if len(vacancy_data_for_save) > 0:
            self._db_manager.append_data(vacancy_data_for_save)

    def __select_required_data(self, vacancy_info: dict) -> dict:
        """Выбирает полезные данные из вакансии и формирует из них словарь"""
        company_name = vacancy_info['employer']['name']
        city = vacancy_info['area']['name']
        vacancy_name = vacancy_info['name'].lower()

        salary_from, salary_to, salary_currency = None, None, None
        if vacancy_info['salary'] is not None:
            salary_from = vacancy_info['salary']['from']
            salary_to = vacancy_info['salary']['to']
            salary_currency = vacancy_info['salary']['currency']

        work_experience = vacancy_info['experience']['name']
        employment = vacancy_info['employment']['name']
        published_at = vacancy_info['published_at'].split('+')[0].replace('T', ' ')
        vacancy_url = vacancy_info['alternate_url']

        requirement, responsibility = None, None
        if vacancy_info['snippet'] is not None:
            requirement = vacancy_info['snippet']['requirement']
            if requirement is not None:
                requirement = requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')
            responsibility = vacancy_info['snippet']['responsibility']
            if responsibility is not None:
                responsibility = responsibility.replace('<highlighttext>', '').replace('</highlighttext>', '')

        required_data = {
            'company_name': company_name,
            'city': city,
            'vacancy_name': vacancy_name,
            'salary_from': salary_from,
            'salary_to': salary_to,
            'salary_currency': salary_currency,
            'work_experience': work_experience,
            'employment': employment,
            'published_at': published_at,
            'vacancy_url': vacancy_url,
            'requirement': requirement,
            'responsibility': responsibility
        }
        return required_data
