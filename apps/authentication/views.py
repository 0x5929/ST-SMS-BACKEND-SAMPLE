from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import LogoutView

# Create your views here.
class RefreshTokenView(get_refresh_view()):
    def get(self, request):

        # route to POST as it is default setforth by simple_jwt
        return super().post(request)


# NOTE: below is only needed for the sample site since its front and back ends are different domains
# and the lib code is buggy that samesite, secure and httponly is not altered in logout endpoint
# so we have to manually input them here
class LogoutView(LogoutView):
    def post(self, request):
        response = super().post(request)

        # set cookies to be samesite and secure
        response.cookies['sms-auth']['samesite'] = 'None'
        response.cookies['sms-auth']['secure'] = True
        response.cookies['sms-auth']['httponly'] = True

        response.cookies['sms-refresh-token']['samesite'] = 'None'
        response.cookies['sms-refresh-token']['secure'] = True
        response.cookies['sms-refresh-token']['httponly'] = True
        return response