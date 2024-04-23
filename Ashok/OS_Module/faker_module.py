from faker import Faker

faker_module = Faker()   # instance for Faker

for i in range(10):
    print("name :", faker_module.name())
    print("last name :", faker_module.last_name())
    print("email :", faker_module.email())
    print("username :", faker_module.user_name())
    print("password :", faker_module.password())

print(dir(faker_module))
