from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import LogoutView

# Create your views here.
class RefreshTokenView(get_refresh_view()):
    def get(self, request):

        # route to POST as it is default setforth by simple_jwt
        return super().post(request)


class AccountLogoutView(LogoutView):
    def post(self, request):
        print('####################### request.user.access_token: ', request.user.access_token)
        print('####################### request.user.refresh_token: ', request.user.refresh_token)

        return super().post(request)