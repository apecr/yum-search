from webapp2 import RequestHandler
import os
import jinja2


class YumSearchRequestHandler(RequestHandler):
    template_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'templates')
    jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

    def render(self, template, **kwargs):
        jinja_template = self.jinja_environment.get_template(template)
        return jinja_template.render(kwargs)