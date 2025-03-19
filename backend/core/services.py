from repositories import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    
    def create_user(self, name: str, email: str):
        self.user_repository.create_user(name, email)
    
    
    def fetch_all_users(self):
        return self.user_repository.fetch_all_users()
    
    
    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)
    
    
    def update_user_by_id(
        self,
        user_id: int,
        name: str,
        email: str
    ):
        self.user_repository.update_user_by_id(
            user_id,
            name,
            email
        )
    
    
    def delete_user_by_id(self, user_id: int):
        self.user_repository.delete_user_by_id(user_id)



user_service = UserService()