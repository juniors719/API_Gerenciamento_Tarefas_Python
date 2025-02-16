"""Exercício: created e updated nas tasks

Revision ID: 572f2ca5abf3
Revises: a3caac7a2820
Create Date: 2025-02-15 19:39:04.277836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '572f2ca5abf3'
down_revision: Union[str, None] = 'a3caac7a2820'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('todos') as batch_op:
        batch_op.add_column(
            sa.Column(
                'created_at',
                sa.DateTime(),
                server_default=sa.text('CURRENT_TIMESTAMP'),
                nullable=False,
            ),
        )
        batch_op.add_column(
            sa.Column(
                'updated_at',
                sa.DateTime(),
                server_default=sa.text('CURRENT_TIMESTAMP'),
                onupdate=sa.text('now()'),
                nullable=False,
            ),
        )


def downgrade() -> None:
    with op.batch_alter_table('todos') as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
