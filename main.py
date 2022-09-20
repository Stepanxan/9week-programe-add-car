from models.addcar import Car
from models.models import Users
import json



class Controller(Users):
    file = 'users.json'

    def add_run(self):
        if __name__ == '__main__':

            while True:
                print("1. Add New Users\n"
                       + "2. Get All Users\n"
                       + "3. Search\n"
                       + "4. Update User By Id"
                      )
                menu_flag = int(input("Type your choose: "))

    @classmethod
    def user_add(self, menu_flag=1):
        if menu_flag == 1:
            email = int(input("email: "))
            password = input("password: ")
            first_name = input("first_name: ")
            last_name = int(input("last_name: "))
            address = int(input("address: "))
            users = Users(id, email, password, first_name, last_name, address)
            users.save()

    @classmethod
    def add_car(self, menu_flag=2):
        if menu_flag == 2:
            models = int(input("models: "))
            number = input("number: ")
            speed = input("speed: ")
            user = int(input("user: "))
            graduation = int(input("graduation: "))
            car = Car(models, number, speed, user, graduation)
            car.save()

    @classmethod
    def get_all(cls, menu_flag=3):
        global data
        if menu_flag == 3:
            data = cls.get_file_data(cls.file)
        return data

    @classmethod
    def search_by(search_str, what_to_search, menu_flag=4):
        if menu_flag == 4:
            with open('database/users.json', 'r') as file:
                users = json.loads(file.read())
                for user in users:
                    if str(user[what_to_search]).lower() == str(search_str).lower():
                        print("Email #" + str(user['email']))
                        print("Password: " + user['password'])
                        print("First_name: " + user['first_name'])
                        print("Last_name: " + user['last_name'])
                        print("Address: " + user['address'])

    @staticmethod
    def update_user(cls, menu_flag = 5):
        if menu_flag == 5:
            file = open('database/users.json', 'r')
            users = json.loads(file.read())
            file.close()
            email = input("Email: ")
            password = input("Password: ")
            first_name = input("First_name: ")
            last_name = input("Last_name: ")
            address = input("Address: ")
            for user in users:
                if user['email'] == email:
                    user['password'] = password
                    user['first_name'] = first_name
                    user['last_name'] = last_name
                    user['address'] = address

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    @staticmethod
    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()

