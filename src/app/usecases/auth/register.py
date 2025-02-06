from app.repositories.user_repository import create_user

async def register_user(user_data):
    return await create_user(user_data.dict())
