from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from src.base_model import Base


class Wallet(Base):
    balance: Mapped[Decimal] = mapped_column(default='0.0',
                                             server_default='0.0')
