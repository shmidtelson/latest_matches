"""Init project

Revision ID: 19e4dbb960df
Revises: 
Create Date: 2021-01-07 15:37:31.978069

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '19e4dbb960df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('country', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('match',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('team_won_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('team_lose_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('event_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('score_lose', sa.SmallInteger(), nullable=True),
    sa.Column('score_won', sa.SmallInteger(), nullable=True),
    sa.Column('stars', sa.SmallInteger(), nullable=True),
    sa.Column('type', sa.SmallInteger(), nullable=True),
    sa.Column('hltv_id', sa.Integer(), nullable=True),
    sa.Column('href', sa.VARCHAR(length=500), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['team_lose_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['team_won_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_match_event_id'), 'match', ['event_id'], unique=False)
    op.create_index(op.f('ix_match_team_lose_id'), 'match', ['team_lose_id'], unique=False)
    op.create_index(op.f('ix_match_team_won_id'), 'match', ['team_won_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_match_team_won_id'), table_name='match')
    op.drop_index(op.f('ix_match_team_lose_id'), table_name='match')
    op.drop_index(op.f('ix_match_event_id'), table_name='match')
    op.drop_table('match')
    op.drop_table('team')
    op.drop_table('event')
    # ### end Alembic commands ###