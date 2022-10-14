from dj_rest_auth.jwt_auth import get_refresh_view

# Create your views here.
class RefreshTokenView(get_refresh_view()):
    def get(self, request):

        # route to POST as it is default setforth by simple_jwt
        return super().post(request)
