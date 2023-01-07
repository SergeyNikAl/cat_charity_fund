from sqlalchemy import Column, ForeignKey, Integer, Text

from .base import CharityDonationBase


class Donation(CharityDonationBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self) -> str:
        return (
            f'Благотворитель: {self.user_id}, '
            f'{self.comment[:15]} , '
            f'{super().__repr__()}'
        )
