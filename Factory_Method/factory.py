import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    """Class to extract JSON Data"""

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property 
    def parsed_data(self):
        """Returns all data as a dictionary"""
        return self.data


class XMLDataExtractor:
    """Class to extract XML Data"""

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        """Returns all data as a list of xml.etree.Element"""
        return self.tree


def data_extraction_factory(filepath):
    """Factory method returns instance of class depending on file extension"""
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f'Cannot extract data from {filepath}')
    return extractor(filepath)


def extract_data_from(filepath):
    """Wrapper of data_extraction_factory. Function adds exception handling"""
    factory_object = None
    try:
        factory_object = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_object


def main():
    sqlite_factory = extract_data_from('data/person.sq3')
    print()

    json_factory = extract_data_from('Factory_Method/data/movies.json')
    json_data = json_factory.parsed_data
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title: {movie['title']}")
        rank = movie['rank']
        if rank:
            print(f"rank: {rank}")
        id = movie['id']
        if id:
            print(f"id: {id}")

    xml_factory = extract_data_from('Factory_Method/data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f'found: {len(liars)} persons')
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f'first name: {firstname}')
        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')
        [print(f"phone number ({p.attrib['type']}):", p.text) 
              for p in liar.find('phoneNumbers')]


if __name__ == '__main__':
    main()