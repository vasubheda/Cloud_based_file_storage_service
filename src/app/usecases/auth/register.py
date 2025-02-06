from app.repositories.user_repository import UserRepository

async def register_user(user_data):
    return await UserRepository.create_user(user_data.dict())
