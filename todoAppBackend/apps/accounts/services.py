from django.contrib.auth import models as accounts_models
from django.db.models import Q
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group
from django.db import transaction, IntegrityError, DatabaseError
from django.core.exceptions import PermissionDenied
import datetime as datetime_modules


def login(data: dict) -> accounts_models.User:
    """
        Get access user 
        Raise exception if user or password are incorrect or user does not exist.

        :param data: username and password of user.
        :type: dict.
        :return: user.
        :raises: ValueError, PermissionDenied.
    """
    username = data.get("username", None)
    password = data.get("password", None)
    if username is None or not username:
        raise ValueError(str(_("The username cannot be empty")))
    if password is None or not password:
        raise ValueError(str(_("The password cannot be empty")))
    try:
        # Obtain user from database if exist
        user = accounts_models.User.objects.get(Q(username=username) | Q(email=username.lower()))
    except accounts_models.User.DoesNotExist as e:
        print(e)
        raise ValueError(str(_("The username or password is incorrect")))
    # Verify is user is active
    if not user.is_active:
        raise PermissionDenied(str(_("Account blocked, contact the administrators.")))
    # Verify if password match
    if not user.check_password(password):
        raise ValueError(str(_("The username or password is incorrect")))
    user = authenticate(username=user.username, password=password)
    return user



def logout(user: accounts_models.User) -> bool:
    """
        Remove token access to user
        Raises exception if user is inactive.

        :param user: User into app
        :type: Model User.
        :return: User.
        :raises: ValueError.
    """
    user.last_login = datetime_modules.datetime.now()
    user.save()
    user.auth_token.delete()
    return True