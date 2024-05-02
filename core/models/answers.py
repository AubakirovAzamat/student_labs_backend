from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
from .option_Answer_association import checkbox_answers_association

if TYPE_CHECKING:
    from .option import Option

class AnswerText(Base):
    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id", ondelete="CASCADE")
    )
    text: Mapped[str]


class AnswerRadio(Base):
    option_id: Mapped[int] = mapped_column(ForeignKey("options.id", ondelete="CASCADE"))


class AnswerCheckbox(Base):
    __tablename__ = "checkboxanswers"
    options: Mapped[list["Option"]] = relationship(
        secondary=checkbox_answers_association, back_populates="checkbox_answers"
    )
