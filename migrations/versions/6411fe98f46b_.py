"""empty message

Revision ID: 6411fe98f46b
Revises: b48801edfcd5
Create Date: 2019-05-20 15:16:49.099774

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "6411fe98f46b"
down_revision = "b48801edfcd5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "reports",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.String(), nullable=True),
        sa.Column("report_type", sa.Integer(), nullable=False),
        sa.Column("since", sa.DateTime(), nullable=True),
        sa.Column("until", sa.DateTime(), nullable=True),
        sa.Column("teacher_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["teacher_id"], ["teachers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("reports")
    # ### end Alembic commands ###
