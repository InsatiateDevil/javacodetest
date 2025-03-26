import pytest
from httpx import AsyncClient

WALLET_ID = ''


@pytest.mark.asyncio(loop_scope="session")
async def test_create_wallet(async_client: AsyncClient):
    global WALLET_ID
    response = await async_client.get("/api/v1/wallet/create_wallet")
    assert response.status_code == 200
    WALLET_ID = response.json()['id']


@pytest.mark.asyncio(loop_scope="session")
async def test_get_wallet_info(async_client: AsyncClient):
    response = await async_client.get(f"/api/v1/wallet/{WALLET_ID}")
    assert response.json() == {'balance': '0.0'}
    assert response.status_code == 200


@pytest.mark.asyncio(loop_scope="session")
async def test_perform_deposit(async_client: AsyncClient):
    data = {
        "operation_type": "DEPOSIT",
        "amount": 200.05
    }
    response = await async_client.post(f"/api/v1/wallets/{WALLET_ID}/operation", json=data)
    assert response.json() == {'balance': '200.05'}
    assert response.status_code == 200


@pytest.mark.asyncio(loop_scope="session")
async def test_get_balance(async_client: AsyncClient):
    response = await async_client.get(f"/api/v1/wallets/{WALLET_ID}")
    assert response.json() == {'balance': '200.05'}
    assert response.status_code == 200


@pytest.mark.asyncio(loop_scope="session")
async def test_perform_withdraw(async_client: AsyncClient):
    data = {
        "operation_type": "WITHDRAW",
        "amount": 200
    }
    response = await async_client.post(f"/api/v1/wallets/{WALLET_ID}/operation", json=data)
    assert response.json() == {'balance': '0.05'}
    assert response.status_code == 200


@pytest.mark.asyncio(loop_scope="session")
async def test_perform_failed_withdraw(async_client: AsyncClient):
    data = {
        "operation_type": "WITHDRAW",
        "amount": 200
    }
    response = await async_client.post(f"/api/v1/wallets/{WALLET_ID}/operation", json=data)
    assert response.json()['detail'] == 'Для проведения операции недостаточно средств'
    assert response.status_code == 409
