class Student:
    def set_attributes(self, sid, name, modlist=None):
        self.sid = sid
        self.name = name
        self.modlist = modlist

    def print_attributes(self):
        print('ID:', self.sid)
        print('Name:', self.name)
        print(f'Modules:', * self.modlist, end='\n')

    def add_module(self, addmod):
        if addmod not in self.modlist:
            self.modlist.append(addmod)

    def del_module(self, delmod):
        if delmod in self.modlist:
            self.modlist.remove(delmod)
