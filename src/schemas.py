import uuid
from decimal import Decimal

from pydantic import BaseModel, field_validator


class OperationIn(BaseModel):
    operation_type: str
    amount: Decimal

    @field_validator("operation_type")
    @classmethod
    def validate_operation_type(cls, value):
        if value not in ['DEPOSIT', 'WITHDRAW']:
            raise ValueError('Invalid operation type')
        return value

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value):
        if value <= 0:
            raise ValueError('Invalid amount')
        return value


class NewWallet(BaseModel):
    id: uuid.UUID
    balance: Decimal


class BalanceOut(BaseModel):
    balance: Decimal
