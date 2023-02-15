import strawberry
from gqlauth.user.queries import UserQueries, UserType
from django.contrib.auth import get_user_model
from gqlauth.user import arg_mutations as mutations

@strawberry.django.type(model=get_user_model())
class MyQueries:
    me: UserType = UserQueries.me
    public: UserType = UserQueries.public_user

@strawberry.type
class Mutation:

    # include what-ever mutations you want.
    verify_token = mutations.VerifyToken.field
    update_account = mutations.UpdateAccount.field
    archive_account = mutations.ArchiveAccount.field
    delete_account = mutations.DeleteAccount.field
    password_change = mutations.PasswordChange.field
    token_auth = mutations.ObtainJSONWebToken.field
    register = mutations.Register.field
    verify_account = mutations.VerifyAccount.field
    resend_activation_email = mutations.ResendActivationEmail.field
    send_password_reset_email = mutations.SendPasswordResetEmail.field
    password_reset = mutations.PasswordReset.field
    password_set = mutations.PasswordSet.field
    refresh_token = mutations.RefreshToken.field
    revoke_token = mutations.RevokeToken.field


schema = strawberry.Schema(query=MyQueries, mutation=Mutation)