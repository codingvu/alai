from colorama import Fore, init

init(autoreset=True)


class City_Distance():
    class Graph:
        def __init__(self, graph_dict=None, directed=True):
            self.graph_dict = graph_dict or {}
            self.directed = directed
            if not directed:
                self.make_undirected()

        def make_undirected(self):
            for a in list(self.graph_dict.keys()):
                for (b, dist) in self.graph_dict[a].items():
                    self.graph_dict.setdefault(b, {})[a] = dist

        def connect(self, A, B, distance=1):
            self.graph_dict.setdefault(A, {})[B] = distance
            if not self.directed:
                self.graph_dict.setdefault(B, {})[A] = distance

        def get(self, a, b=None):
            links = self.graph_dict.setdefault(a, {})
            if b is None:
                return links
            else:
                return links.get(b)

        def nodes(self):
            s1 = set([k for k in self.graph_dict.keys()])
            s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in
                      v.items()])
            nodes = s1.union(s2)
            return list(nodes)

        def display_graph(self):
            print(Fore.YELLOW+"\n\t\t\tTHE GRAPH IS - \n")
            for key in self.graph_dict:
                print(Fore.CYAN+key, Fore.WHITE+' -> ', self.graph_dict[key])

    class Node:
        def __init__(self, name: str, parent: str):
            self.name = name
            self.parent = parent
            self.g = 0
            self.h = 0
            self.f = 0

        def __eq__(self, other):
            return self.name == other.name

        def __lt__(self, other):
            return self.f < other.f

    def a_star(self, graph, heuristics, start, end):
        open = []
        closed = []
        start_node = self.Node(start, "")
        goal_node = self.Node(end, "")
        open.append(start_node)
        while len(open) > 0:
            print(Fore.BLUE+"\n\nOpen List - ")
            for i in open:
                print(i.name, end=" | ")
            print()
            print(Fore.BLUE+"Closed List - ")
            for i in closed:
                print(i.name, end=" | ")
            open.sort()
            current_node = open.pop(0)
            closed.append(current_node)
            if current_node == goal_node:
                path = []
                while current_node != start_node:
                    path.append(current_node.name)
                    current_node = current_node.parent
                path.append(start_node.name)
                return path[::-1]
            neighbors = graph.get(current_node.name)
            for key, unused_value in neighbors.items():
                neighbor = self.Node(key, current_node)
                if (neighbor in closed):
                    continue
                neighbor.g = current_node.g + \
                    graph.get(current_node.name, neighbor.name)
                neighbor.h = heuristics.get(neighbor.name)
                neighbor.f = neighbor.g + neighbor.h
                if (self.add_to_open(open, neighbor) == True):
                    open.append(neighbor)
        return None

    def add_to_open(self, open, neighbor):
        for node in open:
            if (neighbor == node and neighbor.f >= node.f):
                return False
        return True

    def start(self):
        graph = self.Graph()
        graph.connect('Delhi', 'Indore', 800)
        graph.connect('Delhi', 'Kolkata', 1300)
        graph.connect('Indore', 'Mumbai', 600)
        graph.connect('Indore', 'Nagpur', 500)
        graph.connect('Indore', 'Delhi', 800)
        graph.connect('Kolkata', 'Nagpur', 1200)
        graph.connect('Kolkata', 'Hyderabad', 1500)
        graph.connect('Kolkata', 'Delhi', 1300)
        graph.connect('Mumbai', 'Hyderabad', 800)
        graph.connect('Mumbai', 'Bangalore', 1000)
        graph.connect('Mumbai', 'Indore', 600)
        graph.connect('Nagpur', 'Indore', 500)
        graph.connect('Nagpur', 'Kolkata', 1200)
        graph.connect('Nagpur', 'Hyderabad', 500)
        graph.connect('Hyderabad', 'Mumbai', 800)
        graph.connect('Hyderabad', 'Nagpur', 500)
        graph.connect('Hyderabad', 'Kolkata', 1500)
        graph.connect('Hyderabad', 'Bangalore', 500)
        graph.connect('Bangalore', 'Hyderabad', 500)
        graph.connect('Bangalore', 'Mumbai', 1000)
        graph.make_undirected()
        graph.display_graph()
        heuristics = {}
        heuristics['Hyderabad'] = 1500
        heuristics['Delhi'] = 0
        heuristics['Indore'] = 800
        heuristics['Mumbai'] = 1300
        heuristics['Bangalore'] = 1800
        heuristics['Nagpur'] = 1000
        heuristics['Kolkata'] = 1300
        path = self.a_star(graph, heuristics, 'Hyderabad', 'Delhi')
        print(Fore.GREEN+"\n\nThe Path Is - ")
        if path is not None:
            for i in range(len(path)):
                print(path[i])
                print(Fore.BLUE+"\t\t\t\t\t\tA* Search\n")


temp = City_Distance()
temp.start()
