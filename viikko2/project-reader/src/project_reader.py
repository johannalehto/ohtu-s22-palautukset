from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url
        
        #debug
        self._testurl = "/Users/johannalehto/johanna-dev/ohtu-s22-palautukset/viikko2/project-reader/pyproject.toml"

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        with open(self._testurl, "rb") as f:
            toml_dict = tomli.load(f)

        toml_content = toml_dict['tool']['poetry']

        # print(toml_dict['tool']['poetry']['name'])
        # print("Dependencies", toml_dict['tool']['poetry']['dependencies'])

        return Project(
            toml_content['name'], 
            toml_content['description'], 
            toml_content['dependencies'], 
            []
            )

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        # return Project("Test name", "Test description", [], [])
