from graphviz import Digraph

baum = Digraph(
    edge_attr={'dir': 'back', 'color': 'red'},
    node_attr={'fontname': 'arial', 'color': 'lightblue', 'style': 'filled'}
)

#Knoten
with baum.subgraph() as level1:
    level1.attr(rank='same')
    level1.node('lamaglama', r'Lama\n(Lama glama)\nLast-, Woll- und Fleischkamel')
    level1.node('guanaco', r'Guanako\n(Lama guanicoe)\nwilde Lamaart')
    level1.node('vicunja', r'Vikunja\n(Vicugna vicugna)\nWollkamel')
    level1.node('alpaka', r'Alpaka\n(Vicugna pacos)\nWoll- und Therapiekamel')
    level1.node('baktrianus', 'Baktrisches Kamel\n(Camelus bactrianus)\nTrampeltier, 2 Höcker')
    level1.node('dromedarius', 'Dromedar\n(Camelus dromedarius)\n1 Höcker')
    level1.node('hesternus', 'nordamerik. Riesenkamel\n(Camelops hesternus)\num 10000 v. Chr. ausgestorben')

with baum.subgraph() as level2:
    level2.attr(rank='same')
    level2.node('lama', 'Gattung Lama\n(Lama)')
    level2.node('vicugna', 'Gattung Vikunja\n(Vicugna)')
    level2.node('camelops', 'Gattung Camelops')

with baum.subgraph() as level3:
    level3.attr(rank='same')
    level3.node('camelus', 'Altweltkamele\n(Camelus)')
    level3.node('lamini', 'Neuweltkamele\n(Lamini)')

with baum.subgraph() as level4:
    level4.attr(rank='same')
    level4.node('camelidae', 'Kamele\n(camelidae)')

baum.node('laminops', '', shape='point', color='black')

baum.edge('camelidae', 'camelus', dir='none', color='black')
baum.edge('camelidae', 'laminops', dir='none', color='black')
baum.edge('laminops', 'lamini', dir='none', color='black')
baum.edge('laminops', 'camelops', dir='none')

baum.edge('camelus', 'baktrianus', dir='none', color='black')
baum.edge('camelus', 'dromedarius', dir='none', color='black')
baum.edge('lamini', 'lama', dir='none', color='black')
baum.edge('lamini', 'vicugna', dir='none', color='black')

baum.edge('lama', 'lamaglama', dir='none', color='black')
baum.edge('lama', 'guanaco', dir='none', color='black')
baum.edge('vicugna', 'vicunja', dir='none', color='black')
baum.edge('vicugna', 'alpaka', dir='none', color='black')
baum.edge('camelops', 'hesternus', dir='none', color='red')

"""
 # Verbindungen
baum.edge('ehe-rm', 'ramona', dir='none')
baum.edge('lilja', 'ehe-rm')

baum.edge('ehe-km', 'kristian', dir='none')
baum.edge('ehe-km', 'magdalena', dir='none')
baum.edge('ewa', 'ehe-km')
baum.edge('wojtek', 'ehe-km')
baum.edge('nils', 'kristian')

baum.edge('ehe-bb', 'boguslaw', dir='none')
baum.edge('magdalena', 'ehe-bb')
baum.edge('ania', 'ehe-bb')
baum.edge('ehe-bb', 'bozena',dir='none')

baum.edge('ehe-iw', 'wolfgang', dir='none')
baum.edge('ehe-iw', 'irmeli',dir='none')
baum.edge('brigitte', 'wolfgang', dir='both')
baum.edge('kristian', 'ehe-iw')
baum.edge('markus', 'ehe-iw')
"""
baum.render('alpakas.gv', view=True)
