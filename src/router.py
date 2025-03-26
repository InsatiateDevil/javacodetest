import uuid

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud import WalletCRUD
from src.database import db_helper
from src.schemas import OperationIn, BalanceOut, NewWallet

router = APIRouter(
    tags=["Wallet"]
)


@router.get(
    "/create_wallet",
    response_model=NewWallet,
    summary="Запрос нового кошелька"
)
async def get_new_wallet(
        db_session: AsyncSession = Depends(db_helper.get_db_session),
):
    new_wallet = await WalletCRUD.add(db_session=db_session)
    return new_wallet


@router.post(
    "/{wallet_id}/operations",
    response_model=BalanceOut,
    summary="Проведение операций с кошельком"
)
async def post_operation(
        wallet_id: uuid.UUID,
        operation_in: OperationIn,
        db_session: AsyncSession = Depends(db_helper.get_db_session)
):
    new_balance = await WalletCRUD.update(wallet_id, operation_in, db_session)
    return new_balance


@router.get(
    "/{wallet_id}",
    response_model=BalanceOut,
    summary="Получение баланса кошелька по его ID"
)
async def get_balance(
        wallet_id: uuid.UUID,
        db_session: AsyncSession = Depends(db_helper.get_db_session)
):
    wallet = await WalletCRUD.get(wallet_id, db_session)
    return wallet
