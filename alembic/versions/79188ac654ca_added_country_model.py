"""Added country model

Revision ID: 79188ac654ca
Revises: 8974e0fbb97c
Create Date: 2021-01-07 18:04:34.746275

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '79188ac654ca'
down_revision = '8974e0fbb97c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=True),
    sa.Column('short', sa.VARCHAR(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.add_column('team', sa.Column('country_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_index(op.f('ix_team_country_id'), 'team', ['country_id'], unique=False)
    op.create_foreign_key(None, 'team', 'country', ['country_id'], ['id'])
    op.drop_column('team', 'country')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('country', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'team', type_='foreignkey')
    op.drop_index(op.f('ix_team_country_id'), table_name='team')
    op.drop_column('team', 'country_id')
    op.drop_table('country')
    # ### end Alembic commands ###