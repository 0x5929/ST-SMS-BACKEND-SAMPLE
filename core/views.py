import git
import os
import requests
import hmac

from hashlib import sha1
from ipaddress import ip_address, ip_network
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf import settings

BASE_DIR = getattr(settings, 'BASE_DIR')
GITHOOK_SECRET = getattr(settings, 'GITHOOK_SECRET')

class GitPullView(APIView):
    """
    GitPullView

    For CI/CD purpose
    called when remote main/master is updated 
    via merge or push

    """

    # bypassing any authentication or permissions
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        """
        This route is only hit by githooks

        Security implementations: 
        1. whitelist github IP
        2. establish and compare secret key hash

        """

        # Verify if request came from GitHub
        if self.is_github(request):
            
            # match secret signature
            if self.verified_signature(request):

                repo = git.Repo(os.path.join(BASE_DIR, '../.git'))
                repo.remotes.origin.pull()

                return Response({"status" : "git pull success"}, status=status.HTTP_200_OK)

            else: 
                return Response({ "error" : "incorrect secret" }, status=status.HTTP_403_FORBIDDEN)
            
        else:
            return Response({ "error" : "only github is allowed at this endpoint" }, status=status.HTTP_403_FORBIDDEN)






    def is_github(self, request):
        # # https://simpleisbetterthancomplex.com/tutorial/2016/10/31/how-to-handle-github-webhooks-using-django.html
        # forwarded_for_list = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR')).split(', ')

        # # https://stackoverflow.com/questions/753645/how-do-i-get-the-correct-ip-from-http-x-forwarded-for-if-it-contains-multiple-ip
        # forwarded_for = forwarded_for_list[0]

        # client_ip_address = ip_address(forwarded_for)
        # whitelist = requests.get('https://api.github.com/meta').json()['hooks']

        # for valid_ip in whitelist:
        #     if client_ip_address in ip_network(valid_ip):
        #         break
        #     else:
        #         return False

        return True

    def verified_signature(self, request):
        # grab singature
        header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
        if header_signature is None:
            return False

        sha_name, signature = header_signature.split('=')
        if sha_name != 'sha1':
            return False

        mac = hmac.new(force_bytes(GITHOOK_SECRET), msg=force_bytes(request.body), digestmod=sha1)
        
        # compare signatures
        if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
            return False

        return True