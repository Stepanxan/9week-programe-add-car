import json


class Users():
    file = "users.json"

    def __init__(self, email, password, first_name, last_name, address):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def _generate_dict(self):
        return {
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address
        }

    def get_file_data(self, file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()

    def save(self):
        users_in_dict_format = self._generate_dict()
        users = self.get_file_data(self.file)
        users.append(users_in_dict_format)
        self.save_to_file(users)
