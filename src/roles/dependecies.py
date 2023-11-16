from typing import Annotated

from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.auth_config import current_user
from src.database import get_async_session
from src.roles.models import Role
from src.roles.service import RoleService
from src.users.models import User


async def role_by_id(
    role_id: Annotated[int, Path],
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
) -> Role:
    role = await RoleService.get_role_by_id(session=session, role_id=role_id)

    if role is None:
        raise HTTPException(
            status_code=404, detail=f"Role id={role_id} not found!"
        )
    return role


async def role_by_name(
    role_name: Annotated[str, Path],
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
) -> Role:
    role = await RoleService.get_role_by_name(session=session, role_name=role_name)
    if role is None:
        raise HTTPException(
            status_code=404, detail=f"Role id={role_name} not found!"
        )
    return role
