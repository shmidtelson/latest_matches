"""create match kind model

Revision ID: ffe4270c2bcb
Revises: 181c0d6ac9b6
Create Date: 2021-01-07 18:50:43.782617

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ffe4270c2bcb'
down_revision = '181c0d6ac9b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match_kind',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.add_column('match', sa.Column('match_kind_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_index(op.f('ix_match_match_kind_id'), 'match', ['match_kind_id'], unique=False)
    op.create_foreign_key(None, 'match', 'match_kind', ['match_kind_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'match', type_='foreignkey')
    op.drop_index(op.f('ix_match_match_kind_id'), table_name='match')
    op.drop_column('match', 'match_kind_id')
    op.drop_table('match_kind')
    # ### end Alembic commands ###