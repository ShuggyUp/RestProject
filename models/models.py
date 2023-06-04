from sqlalchemy import MetaData, Table, Column, Integer, Text, DateTime, CHAR
from sqlalchemy.orm import declarative_base

# metadata = MetaData()
# vacancies = Table(
#     'vacancy',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('company_name', Text, nullable=False),
#     Column('city', Text, nullable=False),
#     Column('vacancy_name', Text, nullable=False),
#     Column('salary_from', Integer),
#     Column('salary_to', Integer),
#     Column('salary_currency', CHAR(3)),
#     Column('work_experience', Text, nullable=False),
#     Column('employment', Text),
#     Column('published_at', DateTime, nullable=False),
#     Column('vacancy_url', Text, nullable=False),
#     Column('requirement', Text),
#     Column('responsibility', Text)
# )

Base = declarative_base()


class Vacancy(Base):

    __tablename__ = 'vacancy'

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
