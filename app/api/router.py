from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users import UserCreate, UserOut
from app.database.session import get_session
from app.core.security import hash_password
from app.crud.users import get_user_by_email, create_user
from app.crud.accounts import create_account

router = APIRouter(prefix="/api")


@router.post("/register", response_model=UserOut)
async def register_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    existing = await get_user_by_email(session, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    password_hash = hash_password(user_in.password)

    user = await create_user(session, user_in.email, password_hash)
    await create_account(session, user.id)

    await session.commit()
    return user
