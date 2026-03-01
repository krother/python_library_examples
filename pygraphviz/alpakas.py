from graphviz import Digraph

tree = Digraph(
    edge_attr={'dir': 'back', 'color': 'red'},
    node_attr={'fontname': 'arial', 'color': 'lightblue', 'style': 'filled'}
)

#Knoten
with tree.subgraph() as level1:
    level1.attr(rank='same')
    level1.node('lamaglama', r'Lama\n(Lama glama)\nLast-, Woll- und Fleischkamel')
    level1.node('guanaco', r'Guanako\n(Lama guanicoe)\nwilde Lamaart')
    level1.node('vicunja', r'Vikunja\n(Vicugna vicugna)\nWollkamel')
    level1.node('alpaka', r'Alpaka\n(Vicugna pacos)\nWoll- und Therapiekamel')
    level1.node('baktrianus', 'Baktrisches Kamel\n(Camelus bactrianus)\nTrampeltier, 2 Höcker')
    level1.node('dromedarius', 'Dromedar\n(Camelus dromedarius)\n1 Höcker')
    level1.node('hesternus', 'nordamerik. Riesenkamel\n(Camelops hesternus)\num 10000 v. Chr. ausgestorben')

with tree.subgraph() as level2:
    level2.attr(rank='same')
    level2.node('lama', 'Gattung Lama\n(Lama)')
    level2.node('vicugna', 'Gattung Vikunja\n(Vicugna)')
    level2.node('camelops', 'Gattung Camelops')

with tree.subgraph() as level3:
    level3.attr(rank='same')
    level3.node('camelus', 'Altweltkamele\n(Camelus)')
    level3.node('lamini', 'Neuweltkamele\n(Lamini)')

with tree.subgraph() as level4:
    level4.attr(rank='same')
    level4.node('camelidae', 'Kamele\n(camelidae)')

tree.node('laminops', '', shape='point', color='black')

tree.edge('camelidae', 'camelus', dir='none', color='black')
tree.edge('camelidae', 'laminops', dir='none', color='black')
tree.edge('laminops', 'lamini', dir='none', color='black')
tree.edge('laminops', 'camelops', dir='none')

tree.edge('camelus', 'baktrianus', dir='none', color='black')
tree.edge('camelus', 'dromedarius', dir='none', color='black')
tree.edge('lamini', 'lama', dir='none', color='black')
tree.edge('lamini', 'vicugna', dir='none', color='black')

tree.edge('lama', 'lamaglama', dir='none', color='black')
tree.edge('lama', 'guanaco', dir='none', color='black')
tree.edge('vicugna', 'vicunja', dir='none', color='black')
tree.edge('vicugna', 'alpaka', dir='none', color='black')
tree.edge('camelops', 'hesternus', dir='none', color='red')

tree.render('alpakas.gv', view=True)
