from django.contrib.auth.models import User
from apps.tasks import models as tasks_models
from django.utils.translation import gettext as _



def create_task(user: User, data:dict) -> tasks_models.Task:
    """
        service to create task

        :param user: user
        :type user: Model User
        :param data: information of task
        :type data: dict
        :return: list of tasks
    """
    try:
        task = tasks_models.Task.objects.create(
            user=User.objects.get(id = user.id),
            title=data.get('title'),
            description=data.get('description'),
            )
    except Exception as e:
        raise ValueError(str(_("An error occurred while saving the task")))
    return task

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
        if(len(task) == 0): 
            raise NameError(str(_("Not found")))
    except tasks_models.Task.DoesNotExist as e:
        raise NameError(str(_("Not found")))
    return task


def delete_task(user: User, id: int) -> str:
    """
        service to delete task

        :param user: user
        :type user: Model User
        :param id: id
        :type id: int
        :return: list tasks update
    """
    try:
        task = tasks_models.Task.objects.get(id=id, user__id=user.id)
        task.delete()
    except tasks_models.Task.DoesNotExist as e:
        raise NameError(str(_("error to delete")))
    return str(_("the task was deleted successfully"))


def update_task(user: User, data: dict ,id: int) -> tasks_models.Task:
    """
        service to update task

        :param data: information of task
        :type data: dict
        :param user: user
        :type user: Model User
        :return: task
        :raises: ValueError
    """

    try:
        task = tasks_models.Task.objects.get(id=id, user__id=user.id)
        task.title = data.get('title')
        task.description = data.get('description')
        task.save()
    except DatabaseError as e:
        raise NameError(str(_("error to update task")))
    return task