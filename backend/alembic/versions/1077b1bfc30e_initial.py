"""initial

Revision ID: 1077b1bfc30e
Revises: 1d6665550334
Create Date: 2023-08-13 18:46:18.365858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1077b1bfc30e'
down_revision: Union[str, None] = '1d6665550334'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resources',
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('resource_title', sa.String(length=255), nullable=True),
    sa.Column('resource_subtitle', sa.String(length=255), nullable=True),
    sa.Column('resource_link', sa.String(length=255), nullable=True),
    sa.Column('resource_type', sa.String(length=255), nullable=True),
    sa.Column('resource_domain', sa.String(length=255), nullable=True),
    sa.Column('resource_img_path', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('resource_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email_id', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('resources')
    # ### end Alembic commands ###
