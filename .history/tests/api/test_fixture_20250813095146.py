class User:
    def __init__(self):
        self.name = None
        self.second_name = None
    
    def create(self):
        self.name = "Sergii"
        self.second_name = "Butenko"
        
    def remove(self):
        self.name = ''
        self.second_name = ''
        
        
    def test_change_name(self):
        user = User()
        user.create()
    
        assert user.name == "Sergii"
        user.remove()
        
    def test_change_second_name(self):
        user = User()
        user.create()
        
        assert user.second_name == "Butenko"
        user.remove()