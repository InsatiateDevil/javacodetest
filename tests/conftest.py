import pytest
from httpx import ASGITransport, AsyncClient

from main import app


@pytest.fixture(scope='session')
async def async_client():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1:8000"
    ) as ac:
        yield ac
