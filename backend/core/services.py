from models import User
from core.repositories import UserRepository


class UserService:
    def __init__(self):
        """
            Initializes the UserService, which uses the UserRepository.
        """
        self.user_repository = UserRepository()
    
    
    def create_user(self, name: str, email: str) -> int:
        """
            Creates a new user by delegating to the UserRepository.
        """
        return self.user_repository.create_user(name, email)
    
    
    def fetch_all_users(self) -> list:
        """
            Retrieves all users by delegating to the UserRepository.
        """
        return self.user_repository.fetch_all_users()
    
    
    def get_user_by_id(self, user_id: int) -> User:
        """
            Retrieves a user by their ID by delegating to the UserRepository.
        """
        return self.user_repository.get_user_by_id(user_id)
    
    
    def get_user_by_email(self, email: str) -> User:
        """
            Retrieves a user by their email by delegating to the UserRepository.
        """
        return self.user_repository.get_user_by_email(email)
    
    
    def update_user_by_id(
        self,
        user_id: int,
        name: str,
        email: str
    ):
        """
            Updates a user's details by their ID by delegating to the UserRepository.
        """
        self.user_repository.update_user_by_id(
            user_id,
            name,
            email
        )
    
    
    def delete_user_by_id(self, user_id: int):
        """
            Deletes a user by their ID by delegating to the UserRepository.
        """
        self.user_repository.delete_user_by_id(user_id)



user_service = UserService()
