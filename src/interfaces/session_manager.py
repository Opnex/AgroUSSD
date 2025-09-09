class SessionManager:
    def __init__(self):
        self.current_user = None
        self.is_authenticated = False
        self.menu_history = []
        self.current_menu = None

    def login(self, user):
        """Set the current user and mark as authenticated"""
        self.current_user = user
        self.is_authenticated = True
        self.menu_history = []

    def logout(self):
        """Clear the current user and mark as not authenticated"""
        self.current_user = None
        self.is_authenticated = False
        self.menu_history = []
        self.current_menu = None

    def push_menu(self, menu):
        """Add a menu to the history stack"""
        if self.current_menu:
            self.menu_history.append(self.current_menu)
        self.current_menu = menu

    def pop_menu(self):
        """Remove the current menu and return to the previous one"""
        if self.menu_history:
            self.current_menu = self.menu_history.pop()
            return self.current_menu
        return None

    def get_current_menu(self):
        """Get the current menu"""
        return self.current_menu

    def set_current_menu(self, menu):
        """Set the current menu"""
        self.current_menu = menu

    def is_farmer(self):
        """Check if current user is a farmer"""
        return self.is_authenticated and self.current_user and self.current_user.get_user_type() == "Farmer"

    def is_buyer(self):
        """Check if current user is a buyer"""
        return self.is_authenticated and self.current_user and self.current_user.get_user_type() == "Buyer"

    def get_user_info(self):
        """Get current user information"""
        if not self.is_authenticated or not self.current_user:
            return None
        return {
            "name": self.current_user.name,
            "phone": self.current_user.phone_number,
            "location": self.current_user.location,
            "user_type": self.current_user.get_user_type()
        }
