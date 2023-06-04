import requests
import json
from database_manager import DatabaseManager
from datetime import datetime


class VacanciesManager:

    __request_headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
    }
    __hh_api_params = {
        'text': 'developer',
        'area': '113',
        'page': 0,
        'per_page': 50,
        'professional_role': ['156', '160', '10', '12', '150', '25', '165', '34', '36', '73', '155', '96', '164',
                              '104', '157', '107', '112', '113', '148', '114', '116', '121', '124', '125', '126'],
        'order_by': 'publication_time'
    }
    __db_manager = DatabaseManager()

    def select_data_from_db(self, data_filter_flag, search_text=None):
        if data_filter_flag:
            vacancies = self.__db_manager.get_filter_data(search_text)
        else:
            vacancies = self.__db_manager.get_data()

        output_vacancies_json = {}
        counter = 0
        for vacancy in vacancies:
            output_vacancies_json[counter] = {
                'company_name': vacancy[1],
                'city': vacancy[2],
                'vacancy_name': vacancy[3],
                'salary_from': vacancy[4],
                'salary_to': vacancy[5],
                'salary_currency': vacancy[6],
                'work_experience': vacancy[7],
                'employment': vacancy[8],
                'published_at': vacancy[9],
                'vacancy_url': vacancy[10],
                'requirement': vacancy[11],
                'responsibility': vacancy[12]
            }
            counter += 1
        return output_vacancies_json

    def parse_vacancies_to_db(self):
        server_response = requests.get('https://api.hh.ru/vacancies', self.__hh_api_params, headers=self.__request_headers)
        vacancies_info = json.loads(server_response.content.decode())

        lust_date = self.__db_manager.get_lust_record_date()
        vacancy_data_for_save = []
        for vacancy_info in vacancies_info['items']:
            required_data = self.__select_required_data(vacancy_info)
            vacancy_date = datetime.strptime(required_data['published_at'], '%Y-%m-%d %H:%M:%S')
            if vacancy_date > lust_date:
                vacancy_data_for_save.append(required_data)
            else:
                break

        if len(vacancy_data_for_save) > 0:
            self.__db_manager.append_data_to_db(vacancy_data_for_save)

    def __select_required_data(self, vacancy_info):
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
