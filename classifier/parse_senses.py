import xml.etree.ElementTree as ET
import json


senses = {}


def parse(src_senses, src_synsets):
    tree = ET.parse(src_synsets)
    root = tree.getroot()

    synsets = {}
    for child in root:
        id = child.get('id')
        name = child.get('ruthes_name').lower()
        synsets[id] = name

    tree = ET.parse(src_senses)
    root = tree.getroot()

    for child in root:
        name = child.get('name')
        if len(name.split()) != 1:
            name = child.get('main_word')
        if len(name) == 0:
            continue

        name = name.lower()

        if name not in senses:
            senses[name] = {}
        id = child.get('synset_id')
        if synsets[id] not in senses[name]:
            senses[name][synsets[id]] = id


def main():
    parse('ruwordnet/senses.A.xml', 'ruwordnet/synsets.A.xml')
    parse('ruwordnet/senses.N.xml', 'ruwordnet/synsets.N.xml')
    parse('ruwordnet/senses.V.xml', 'ruwordnet/synsets.V.xml')
    json.dump(senses, open('tools/senses.txt', 'w'))


main()
