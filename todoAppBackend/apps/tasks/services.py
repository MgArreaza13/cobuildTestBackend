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


def get_detail_task(user: User, id: int) -> tasks_models.Task:
    """
        service to get detail from task

        :param user: user
        :type user: Model User
        :param id: id
        :type id: int
        :return: one task
    """
    try:
        task = tasks_models.Task.objects.filter(id=id, user__id=user.id)
    except tasks_models.Task.DoesNotExist as e:
        raise NameError(str(_("Not found")))
    return task