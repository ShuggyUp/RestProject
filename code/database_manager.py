from sqlalchemy import create_engine, insert, select
from sqlalchemy.orm import Session
from models.models import Vacancy
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS
from datetime import datetime


class DatabaseManager:

    __engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    __base_select_limit = 30

    def get_data(self):
        with Session(bind=self.__engine) as session:
            valid_data = session.execute(select('*').select_from(Vacancy).order_by(Vacancy.published_at.desc()).
                                         limit(self.__base_select_limit)).fetchall()

        return valid_data

    def get_filter_data(self, keywords):
        keywords_like_query = '%' + '%'.join(keywords.lower().split()) + '%'
        with Session(bind=self.__engine) as session:
            valid_data = session.execute(select('*').filter(Vacancy.vacancy_name.like(keywords_like_query))).fetchall()

        return valid_data

    def append_data_to_db(self, vacancy_data_dict):
        with Session(bind=self.__engine) as session:
            session.execute(insert(Vacancy), vacancy_data_dict)
            session.commit()

    def get_lust_record_date(self):
        with Session(bind=self.__engine) as session:
            lust_record = session.execute(select(Vacancy.published_at).order_by(Vacancy.published_at.desc()))
            lust_record_date = lust_record.fetchone()
            if lust_record_date is not None:
                lust_record_date = lust_record_date[0]
            else:
                lust_record_date = datetime.strptime('2000-01-01 01:01:01', '%Y-%m-%d %H:%M:%S')

        return lust_record_date
