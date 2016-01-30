from security.users_repository import usersRepository
import uuid

class users(object):
    def __init__(self):
        self.users_repository = usersRepository()

    def get_all_users(self):
        return self.users_repository.get_all_users()

    def get_user(self, uuid):
        return self.users_repository.get_user(uuid)

    def create_user(self, user):
        user['uuid'] = str(uuid.uuid4())
        return self.users_repository.create_user(user)

    def delete_user(self, uuid):
        return self.users_repository.delete_user(uuid)

    def update_user(self, uuid, user):
        return self.users_repository.update_user(uuid, user)