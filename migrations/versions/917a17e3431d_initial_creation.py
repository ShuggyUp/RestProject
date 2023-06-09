"""Initial creation

Revision ID: 917a17e3431d
Revises: 
Create Date: 2023-06-08 14:22:11.347543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '917a17e3431d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vacancies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.Text(), nullable=False),
    sa.Column('city', sa.Text(), nullable=False),
    sa.Column('vacancy_name', sa.Text(), nullable=False),
    sa.Column('salary_from', sa.Integer(), nullable=True),
    sa.Column('salary_to', sa.Integer(), nullable=True),
    sa.Column('salary_currency', sa.CHAR(length=3), nullable=True),
    sa.Column('work_experience', sa.Text(), nullable=False),
    sa.Column('employment', sa.Text(), nullable=True),
    sa.Column('published_at', sa.DateTime(), nullable=False),
    sa.Column('vacancy_url', sa.Text(), nullable=False),
    sa.Column('requirement', sa.Text(), nullable=True),
    sa.Column('responsibility', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancies')
    # ### end Alembic commands ###
