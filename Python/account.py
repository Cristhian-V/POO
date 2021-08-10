class Account:
    id: int
    name: str
    document: str
    password: str
    email: str

    def __init__(self, id, name, document, password, email) -> None:
        self.id = id
        self.name = name
        self. document =  document
        self.password = password
        self.email = email

    def getAccount(self):
        print(f'El usuario {self.id}\nNombre: {self.name}\nDocumento: {self.document}\nEmail: {self.email}')