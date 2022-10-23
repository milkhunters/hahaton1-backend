from models.schemas import User


class LoginResponse(User):
    pass


class RegisterResponse(str):
    pass
