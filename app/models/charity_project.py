from sqlalchemy import Column, String, Text

from .base import CharityDonationBase


class CharityProject(CharityDonationBase):

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return (
            f'Проект: {self.name[:15]}, '
            f'{self.description[:15]}, '
            f'{super().__repr__()}'
        )
