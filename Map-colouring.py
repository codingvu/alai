#MAp Colouring
from colorama import Fore, Back, Style, init
init(strip=False)
init(autoreset=True)
class map_coloring():
    # Colors Used
    colors = [Fore.RED+'Red', Fore.GREEN+'Green',
              Fore.YELLOW+'Yellow', Fore.MAGENTA+'Violet']
    # Map
    states = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    neighbors = {}
    neighbors['A'] = ['B', 'C', 'D']
    neighbors['B'] = ['A', 'C']
    neighbors['C'] = ['A', 'B', 'D', 'E']
    neighbors['D'] = ['A', 'C', 'F', 'E']
    neighbors['E'] = ['F', 'C', 'D']
    neighbors['F'] = ['E', 'D', 'G']
    neighbors['G'] = ['F']
    # Output
    colors_of_states = {}
    def print_graph(self):
        for key in self.neighbors:
            print(Fore.CYAN + key + Fore.WHITE + ' -> ', self.neighbors[key])
    def promising(self, state, color):
        for neighbor in self.neighbors.get(state):
            color_of_neighbor = self.colors_of_states.get(neighbor)
            if color_of_neighbor == color:
                return False
        return True
    def get_color_for_state(self, state):
        for color in self.colors:
            if self.promising(state, color):
                return color
    def start(self):
        print(Fore.BLUE+"\n\n\t\tThe Graph Is ")
        self.print_graph()
        print("\n\n")
        for state in self.states:
            self.colors_of_states[state] = self.get_color_for_state(state)
            print(
                f"Color Used For State {state} is {self.colors_of_states[state]}")
        print(Fore.BLUE+"\n\n\t\tThe Solution Is - ")
        for key in self.colors_of_states:
            print(Fore.BLUE+key + Fore.WHITE +
                  ' -> ', self.colors_of_states[key])
temp = map_coloring()
temp.start()
