from models import User, db


class UserRepository:
    def create_user(
        self,
        name: str,
        email: str
    ) -> int:
        user = User(
            name=name,
            email=email
        )
        
        db.session.add(user)
        db.session.commit()
        
        return user.id
    
    
    def fetch_all_users(self) -> list:
        return User.query.all()
    
    
    def get_user_by_id(self, user_id: int) -> User:
        return User.query.filter_by(id=user_id).first()
    
    
    def update_user_by_id(
        self,
        user_id: int,
        name: str,
        email: str
    ) -> None:
        
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
    
    
    def delete_user_by_id(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()

    
    
    def get_user_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()