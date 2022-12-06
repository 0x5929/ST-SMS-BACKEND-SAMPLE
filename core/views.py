import git
import os

from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings

BASE_DIR = getattr(settings, 'BASE_DIR')

class GitPullView(APIView):
    """
    GitPullView

    For CI/CD purpose
    called when remote main/master is updated 
    via merge or push

    """

    def get(self, request):
        """
        This route is only hit by githooks

        using default APIView permissions classes [AllowAny]

        """

        repo = git.Repo(os.path.join(BASE_DIR, '../.git'))
        repo.remotes.origin.pull()

        Response({"status" : "ok"}, status=status.HTTP_200_OK)