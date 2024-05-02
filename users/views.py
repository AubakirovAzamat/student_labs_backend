from fastapi import APIRouter, Depends, HTTPException, status
from core.models import db_helper
from users.dependencies import user_by_id
from users.schemas import User
from users import crud
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def user_create(
    user: User,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    try:
        return await crud.user_create(session=session, user_in=user)
    except:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User already exists",
        )


@router.delete("/{user_id}")
async def user_delete(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.user_delete(session=session, user=user)
