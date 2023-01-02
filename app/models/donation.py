from sqlalchemy import Column, ForeignKey, Integer, Text

from .base import CharityDonationBase


class Donation(CharityDonationBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self) -> str:
        super().__repr__()
        return f'Внесено {self.invested_amount}'
