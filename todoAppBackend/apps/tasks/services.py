from django.contrib.auth.models import User
from apps.tasks import models as tasks_models
from django.utils.translation import gettext as _


def get_list_tasks(user: User) -> tasks_models.Task:
    """
        service to get list or tasks

        :param user: user
        :type user: Model User
        :return: list of tasks
    """
    list_tasks = tasks_models.Task.objects.filter(user__id = user.id).order_by('-id')
    return list_tasks