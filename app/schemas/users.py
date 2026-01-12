from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="Почта пользователя")
    password: str = Field(..., min_length=8, max_length=64, description="Пароль пользователя")


class UserOut(BaseModel):
    id: int = Field(..., description="Индефикатор пользователя")
    email: EmailStr = Field(..., description="Почта пользователя")

    class Config:
        from_attributes = True
