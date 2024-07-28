# user_management.py

class UserManagement:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, email):
        """Register a new user."""
        if username in self.users:
            return "Username already exists."
        self.users[username] = {
            'password': password,
            'email': email
        }
        return "User registered successfully."

    def login_user(self, username, password):
        """Log in a user."""
        user = self.users.get(username)
        if not user:
            return "User not found."
        if user['password'] != password:
            return "Incorrect password."
        return "Login successful."

    def view_profile(self, username):
        """View user profile."""
        user = self.users.get(username)
        if not user:
            return "User not found."
        return user

# Example usage
# if __name__ == "__main__":
#     um = UserManagement()
#     print(um.register_user('john_doe', 'password123', 'john@example.com'))
#     print(um.login_user('john_doe', 'password123'))
#     print(um.view_profile('john_doe'))
