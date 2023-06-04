import uvicorn
from fastapi import FastAPI
from vacancies_manager import VacanciesManager


app = FastAPI()


@app.get('/')
def print_vacancies():
    vacancy_manager = VacanciesManager()
    return vacancy_manager.select_data_from_db(False)


@app.get('/search-vacancies')
def search_vacancies(search_text: str = 'Разработчик'):
    vacancy_manager = VacanciesManager()
    return vacancy_manager.select_data_from_db(True, search_text)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
