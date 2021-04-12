import abc
import urllib.parse
import urllib.request


class ResourceContent:
    """Define the abstraction's interface, and maintain a reference to an 
    object which represents the Implementer."""

    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)


class ResourceContentFetcher(metaclass=abc.ABCMeta):
    """Define the interface for implementation class that help fetch content"""

    @abc.abstractmethod
    def fetch(path):
        pass


class URLFetcher(ResourceContentFetcher):
    """
    Implement the Implementor interface and define its concrete implementation,
    and fetch URLs.
    """

    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)


class LocalFileFetcher(ResourceContentFetcher):
    """Implement the Implementor interface and define its concrete implementation,
    and fetch local files.
    """

    def fetch(self, path):
        with open(path) as f:
            print(f.read())


def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')

    print('---------')

    local_file_fetcher = LocalFileFetcher()
    iface = ResourceContent(local_file_fetcher)
    iface.show_content('Bridge_Pattern/text.txt')


if __name__ == '__main__':
    main()