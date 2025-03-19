from models import User, db


class UserRepository:
    def create_user(
        self,
        name: str,
        email: str
    ) -> int:
        """
            Creates a new user in the database.
        """
        user = User(
            name=name,
            email=email
        )
        
        db.session.add(user)
        db.session.commit()
        
        return user.id
    
    
    def fetch_all_users(self) -> list:
        """
            Fetches all users from the database.
        """
        return User.query.all()
    
    
    def get_user_by_id(self, user_id: int) -> User:
        """
            Fetches a user by their ID.
        """
        return User.query.filter_by(id=user_id).first()
    
    
    def update_user_by_id(
        self,
        user_id: int,
        name: str,
        email: str
    ) -> None:
        """
            Updates a user's details by their ID.
        """
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
    
    
    def delete_user_by_id(self, user_id: int) -> None:
        """
            Deletes a user by their ID.
        """
        user = self.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()

    
    
    def get_user_by_email(self, email: str) -> User:
        """
            Fetches a user by their email address.
        """
        return User.query.filter_by(email=email).first()
