#В этом коде класс `User` инкапсулирует данные о пользователе,
# а класс `Admin` наследуется от `User` и добавляет дополнительную функциональность
# для администраторов. Атрибуты классов защищены от прямого доступа и изменения извне,
# а доступ к ним осуществляется через соответствующие методы

class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        super().__init__(user_id, name, access_level)
        self.__users_list = []

    def add_user(self, user):
        self.__users_list.append(user)
        print(f'Пользователь {user.get_name()} добавлен в список.')

    def remove_user(self, user):
        if user in self.__users_list:
            self.__users_list.remove(user)
            print(f'Пользователь {user.get_name()} удален из списка.')
        else:
            print(f'Пользователь {user.get_name()} не найден в списке.')

    def get_users_list(self):
            users = [user.get_name() for user in self.__users_list]
            return users


# Пример работы
user1 = User(1, 'Настя')
user2 = User(2, 'Вова')
user3 = User(3, 'Нина')
user4 = User(4, 'Никита')
admin = Admin(999, 'Админ')

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

print("\nТекущий список пользователей:")
print(admin.get_users_list())
print('-' *40)
admin.remove_user(user1)
admin.remove_user(user4)
print("\nТекущий список пользователей:")
print(admin.get_users_list())