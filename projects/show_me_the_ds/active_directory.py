class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # matching against users in current group
    for group_user in group.get_users():
        if group_user == user:
            return True

    # matching against users in sub groups using recursion
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True

    return False


# unit testing code
software_engineers = Group("software_engineers")
developers = Group("developers")
testers = Group("testers")

software_engineers.add_group(developers)
software_engineers.add_group(testers)

frontend_developer = Group("frontend_developers")
fullstack_developer = Group("fullstack_developers")

developers.add_group(frontend_developer)
developers.add_group(fullstack_developer)

frontend_developer.add_user("me")
frontend_developer.add_user("my_friend")

fullstack_developer.add_user("you")
fullstack_developer.add_user("your_friend")


print("Pass" if not is_user_in_group("you", testers) else "Fail")
print("Pass" if not is_user_in_group("me", fullstack_developer) else "Fail")
print("Pass" if is_user_in_group("me", frontend_developer) else "Fail")
print("Pass" if not is_user_in_group("udacity", software_engineers) else "Fail")
