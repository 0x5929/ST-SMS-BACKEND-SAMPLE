from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import LogoutView

# Create your views here.
class RefreshTokenView(get_refresh_view()):
    def get(self, request):

        # route to POST as it is default setforth by simple_jwt
        return super().post(request)


class AccountLogoutView(LogoutView):
    def post(self, request):
        response = super().post(request)

        # set cookies to be samesite and secure
        response.cookies['sms-auth']['samesite'] = 'None'
        response.cookies['sms-auth']['secure'] = True
        response.cookies['sms-auth']['httponly'] = True

        response.cookies['sms-refresh-token']['samesite'] = 'None'
        response.cookies['sms-refresh-token']['secure'] = True
        response.cookies['sms-refresh-token']['httponly'] = True
        return 