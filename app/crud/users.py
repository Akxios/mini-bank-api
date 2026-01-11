from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import models


async def get_user_by_email(
    session: AsyncSession,
    email: str
) -> Optional[models.User]:
    result = await session.execute(
        select(models.User).where(models.User.email == email)
    )
    return result.scalar_one_or_none()


async def create_user(
    session: AsyncSession,
    email: str,
    password_hash: str
) -> models.User:
    user = models.User(
        email=email,
        password_hash=password_hash
    )
    session.add(user)
    await session.flush()
    await session.refresh(user)
    return user
