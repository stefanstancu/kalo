"""change date to datetime

Revision ID: e88987dc560c
Revises: 
Create Date: 2018-06-27 12:08:44.432935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e88987dc560c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('meal_items', 'date', type_=sa.types.DateTime)
    pass


def downgrade():
    op.alter_column('meal_items', 'date', type_=sa.types.Date)
    pass
