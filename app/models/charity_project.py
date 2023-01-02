from sqlalchemy import Column, String, Text

from .base import CharityDonationBase


class CharityProject(CharityDonationBase):

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self) -> str:
        super().__repr__()
        return f'Необходимо собрать: {self.full_amount}'
