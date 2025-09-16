
class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False

class AppStore:
    APPLICATIONS = {}

    def add_application(self, app: Application):
        self.APPLICATIONS[app.name] = app.blocked

    def remove_application(self, app):
        if app.name in self.APPLICATIONS:
            self.APPLICATIONS.pop(app.name)

    def block_application(self, app: Application):
        self.APPLICATIONS[app.name] = True

    def total_apps(self):
        return len(self.APPLICATIONS)

store = AppStore()
app_ret = Application('RuTube')
app_yuo = Application('YuoTube')
store.add_application(app_ret)
store.add_application(app_yuo)
store.block_application(app_yuo)
print(app_yuo.blocked)
print(store.total_apps())
store.remove_application(app_ret)
print(store.total_apps())

