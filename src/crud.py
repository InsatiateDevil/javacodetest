import uuid

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.exceptions import ObjectNotFound, NotEnoughMoney
from src.model import Wallet
from src.schemas import OperationIn


class WalletCRUD:
    model = Wallet

    @classmethod
    async def add(
            cls,
            db_session: AsyncSession
    ):
        new_wallet = cls.model()
        db_session.add(new_wallet)
        try:
            await db_session.commit()
            await db_session.refresh(new_wallet)
        except SQLAlchemyError as e:
            await db_session.rollback()
            raise e
        return new_wallet

    @classmethod
    async def get(
            cls,
            wallet_id: uuid.UUID,
            db_session: AsyncSession
    ):
        wallet = await db_session.get(cls.model, wallet_id)
        return wallet

    @classmethod
    async def update(
            cls,
            wallet_id: uuid.UUID,
            operation_in: OperationIn,
            db_session: AsyncSession
    ):
        wallet = await db_session.get(cls.model,
                                      wallet_id,
                                      with_for_update=True)
        if not wallet:
            return ObjectNotFound()
        if operation_in.operation_type == "DEPOSIT":
            wallet.balance += operation_in.amount
        else:
            wallet.balance -= operation_in.amount
            if wallet.balance < 0:
                raise NotEnoughMoney()
        try:
            await db_session.commit()
            await db_session.refresh(wallet)
        except SQLAlchemyError as e:
            await db_session.rollback()
            raise e
        return wallet
