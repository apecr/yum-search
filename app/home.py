from framework.request_handler import YumSearchRequestHandler


class Home(YumSearchRequestHandler):
    def get(self):
        self.response.write(self.render('home/home.html'))