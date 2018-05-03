import xml.etree.ElementTree as ET

nodes = 0
edges = []


def build_graph(src_relations):
    global nodes

    tree = ET.parse(src_relations)
    root = tree.getroot()

    for child in root:
        if 'hypernym' not in child.get('name'):
            continue
        v = int(child.get('parent_id')[1:])
        u = int(child.get('child_id')[1:])
        edges.append((v, u))
        nodes = max(nodes, v, u)


def main():
    global nodes

    build_graph('ruwordnet/synset_relations.A.xml')
    build_graph('ruwordnet/synset_relations.N.xml')
    build_graph('ruwordnet/synset_relations.V.xml')

    with open('tools/graph.txt', 'w') as f:
        f.write(str(nodes) + ' ' + str(len(edges)) + '\n')
        for v, u in edges:
            f.write(str(v) + ' ' + str(u) + '\n')


if __name__ == '__main__':
    main()
