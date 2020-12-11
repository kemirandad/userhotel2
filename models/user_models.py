from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    usersurname: str
    userdocument: int
    usermail: EmailStr
    userphone: int 