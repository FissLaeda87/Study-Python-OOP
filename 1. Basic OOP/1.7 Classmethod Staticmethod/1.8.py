
class Data:
    def __init__(self, s: str, ip: int):
        self.data = s
        self.ip = ip

class Server:
    IP = 1

    def __init__(self):
        self.ip = self.IP
        self._ip_count()
        self.buffer = []
        self.router: Router = None

    @classmethod
    def _ip_count(cls):
        cls.IP += 1

    def send_data(self, data: Data):
        self.router.buffer.append(data)

    def get_data(self):
        return self.buffer

    def get_ip(self):
        return self.ip



class Router:

    def __init__(self):
        self.buffer: list[Data] = []
        self.servers: dict = {}



    def link(self, server: Server):
        if server.ip not in self.servers:
            self.servers[server.ip] = server
            server.router = self

    def unlink(self, server: Server):
        if server.ip in self.servers:
            s = self.servers.pop(server.ip)
            s.router = None

    def send_data(self):
        for pack in self.buffer:
            self.servers[pack.ip].buffer.append(pack)
        self.buffer.clear()



router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
