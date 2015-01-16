import requests
from bs4 import BeautifulSoup
import re


class MyEavesDrop(object):

    def __init__(self, type, project, year=None):
        self.__url = "http://eavesdrop.openstack.org/"
        self.__type = type
        self.__project = project
        self.__year = year

    def validate(self):
        url = self.__url
        url += str(self.__type) + "/" + str(self.__project) + "/" + ("" if self.__year is None else self.__year)
        self.start(url)

    def start(self, url):
        source = requests.get(url).text
        soup = BeautifulSoup(source)
        for project in soup.findAll('a', text=re.compile(self.__project)):
            print(project.text)


x = MyEavesDrop('meetings', '3rd_party_ci', '2014')
x.validate()


