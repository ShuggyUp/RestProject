from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from models.models import Vacancies
from config import settings
from datetime import datetime


class DatabaseManager:

    __engine = create_engine(f'postgresql://{settings.DB_USER}:{settings.DB_PASS}@'
                             f'{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}')
    __select_limit = 30

    def get_data(self, keywords=None):
        with Session(bind=self.__engine) as session:
            if keywords is None:
                valid_data = session.query(Vacancies).order_by(Vacancies.published_at.desc()).limit(
                    self.__select_limit).all()
            else:
                keywords_like_query = '%' + '%'.join(keywords.lower().split()) + '%'
                valid_data = session.query(Vacancies).filter(Vacancies.vacancy_name.like(keywords_like_query)).all()

        return valid_data

    def append_data_to_db(self, vacancy_data_dict):
        with Session(bind=self.__engine) as session:
            session.execute(insert(Vacancies), vacancy_data_dict)
            session.commit()

    def get_last_record_date(self):
        with Session(bind=self.__engine) as session:
            lust_record = session.query(Vacancies.published_at).order_by(Vacancies.published_at.desc()).first()
            lust_record_date = lust_record.fetchone()
            if lust_record_date is not None:
                lust_record_date = lust_record_date[0]
            else:
                lust_record_date = datetime.strptime('2000-01-01 01:01:01', '%Y-%m-%d %H:%M:%S')

        return lust_record_date


    def test(self):
        print(settings.DB_USER)