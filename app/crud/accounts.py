from sqlalchemy.ext.asyncio import AsyncSession
from app.database import models


async def create_account(
    session: AsyncSession,
    user_id: int
) -> models.Account:
    account = models.Account(
        user_id=user_id,
        balance=0
    )
    session.add(account)
    await session.flush()
    return account
