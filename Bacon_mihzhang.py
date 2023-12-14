import pandas as pd

'''
author: Minghua Zhang
'''
def read_file(name_file):
    """Reads the file and returns a list of lists with the data"""
    data = []
    for line in name_file:
        line = line.replace("...", '')
        line = line.strip()
        parts = line.split('/')
        cleaned_parts = [part for part in parts if part]
        # line = [x.replace(',','') for x in line]
        data.append(cleaned_parts)
    return data

# def read_file_list(filefloder):
#     '''
#     read all files in the filefloder and return a list of lists with the data
#     '''
#     import os
#     filelist = os.listdir(filefloder)
#     file_paths = [os.path.join(filefloder, file_name) for file_name in filelist]
#     datalist = []
#     for file_path in file_paths:
#         with open(file_path, 'r', encoding='ISO-8859-1') as file:
#             datalist.extend(read_file(file))
#             file.close()
#     return datalist


def parse_data(data):
    '''
    transform the data into a list of tuples, each tuple contains a movie and 
    a list of actors in the movie
    
    input:
    data: a list of lists with the data
    
    return:
    movies_actors: a list of tuples, each tuple contains a movie and a list of
    '''
    movies_actors = []
    for entry in data:
        movie = entry[0]
        actors = entry[1:]
        movies_actors.append((movie, actors))
    return movies_actors

class SimpleGraph:
    def __init__(self):
        '''
        initialize a graph
        '''
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)  # Assuming it's an undirected graph

    
    def shortest_path_length(self, source):
        '''
        find the shortest path between source and all other nodes in the graph
        
        input:
        source: the graph of movies and actors
        
        return:
        visited: a dictionary with node name as key and distance as value
        '''
        if source not in self.graph:
            return {}

        visited = {source: 0}
        queue = [source]

        while queue:
            current_node = queue.pop(0)
            current_distance = visited[current_node]

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited[neighbor] = current_distance + 1
                    queue.append(neighbor)

        return visited

       
        
    def find_shortest_path(self, source, target):
        '''
        find the shortest path between source and target
        
        input:
        source: the graph of movies and actors
        target: the target actor
        
        return:
        distance: the distance between source and target
        path: the shortest path between source and target
        '''
        if source not in self.graph or target not in self.graph:
            return None, None

        queue = [source]
        paths = {source: [source]}  # to keep track of the path to each node

        while queue:
            current_node = queue.pop(0)
            current_path = paths[current_node]

            if current_node == target:
                return len(current_path) - 1, current_path  # return distance and path

            for neighbor in self.graph[current_node]:
                if neighbor not in paths:
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    paths[neighbor] = new_path
                    queue.append(neighbor)

        return None, None

# Find shortest path between two nodes in a graph
def calculate_distance_to_actor(G, source, target):
    '''
    calculate the distance and shortest path between certain actors in the network
    
    input:
    G: a graph of actors and movies
    source: the name of the source actor
    target: the name of the target actor
    
    return:
    distance: the distance between source and target
    path: the shortest path between source and target
    '''
    distance, path = G.find_shortest_path(source, target)
    return distance, path


def build_actor_network(movies_actors):
    '''
    build a graph of actors and movies
    
    input: 
    movies_actors: a list of tuples, each tuple contains a movie and a list of 
    actors in the movie
    
    output:
    G: a graph of actors and movies  
    '''
    G = SimpleGraph()
    for movie, actors in movies_actors:
        for actor in actors:
            G.add_node(actor)
            for other_actor in actors:
                if actor != other_actor:
                    G.add_edge(actor, other_actor)
    return G


def calculate_kevin_bacon_numbers(G, kevin_bacon_name="Bacon Kevin"):
    '''
    calculate the distance between Kevin Bacon and all other actors in the network
    
    input:
    G: a graph of actors and movies
    kevin_bacon_name: the name of Kevin Bacon
    
    return:
    bacon_numbers: a dictionary with actor name as key and distance as value
    '''
    if kevin_bacon_name not in G.graph:
        print(f"Warning: '{kevin_bacon_name}' not found in network.")
        return {}

    bacon_numbers = G.shortest_path_length(kevin_bacon_name)
    return bacon_numbers


def print_menu():
    '''
    print menu
    '''
    print("1. Calculate Kevin Bacon numbers between Richard Nisbett(1 st umich search result in google scholar) and another Umich authors")
    print("2. Calculate Kevin Bacon numbers between author A and author B")
    print("3. Print mean KB distance between Richard Nisbett and all other authors in the network")
    print("4. Print mean KB distance between author A and all other authors in the network")
    
def valid_input():
    '''
    keep asking user to input 1 or 2 or 3 or 4
    until user input is 1 or 2 or 3 or 4
    
    return:
    choice: int 1 or 2 or 3 or 4
    '''
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1,2,3,4]:
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid choice. Try again.")

def YorN():
    '''
    keep asking user to input Y or N until user input is Y or N
    
    return:
    True if user input is Y
    False if user input is N
    
    '''
    while True:
        try:
            choice = input("Do you want to continue? (Y/N): ")
            if choice in ['Y','N']:
                if choice == 'Y':
                    return True
                else:
                    return False
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid choice. Try again.")
            
def main():
    
    with open('scholar_publications.txt', 'r', encoding='utf-8') as file:
        raw_data = read_file(file)
        file.close()
    print("Data loaded.")
    # print(raw_data)
    # pd.DataFrame(raw_data).to_csv('raw_data.csv')
    parsed_data = parse_data(raw_data)
    pd.DataFrame(parsed_data).to_csv('parsed_data.csv')
    actor_network = build_actor_network(parsed_data)
    
    status = True
    while status:
        print_menu()
        choice = valid_input()
        if choice == 1:
            author_name = input("Please Enter the name of the UMICH author only use space to separate the name:(e.g. 'Initials of first&middle name +   + Lastname')") 
            distance_to_actor,path_to_actor = calculate_distance_to_actor(actor_network, 'RE Nisbett', author_name)
            print(f"The distance from 'RE Nisbett(Richard Nisbett)' to '{author_name}' is: {distance_to_actor}")
            print(f"The path from 'RE Nisbett(Richard Nisbett)' to '{author_name}' is: {path_to_actor}")
            
        elif choice == 2:
            author_name_a = input("Please Enter the name of the A author only use space to separate the name:(e.g. 'Initials of first&middle name + ' ' + Lastname')") 
            author_name_b = input("Please Enter the name of the B author only use space to separate the name:(e.g. 'Initials of first&middle name + ' ' + Lastname')")
            distance_to_actor,path_to_actor = calculate_distance_to_actor(actor_network, author_name_a, author_name_b)
            print(f"The distance from '{author_name_a}' to '{author_name_b}' is: {distance_to_actor}")
            print(f"The path from '{author_name_a}' to '{author_name_b}' is: {path_to_actor}")
        
        elif choice == 3:
            bacon_numbers = calculate_kevin_bacon_numbers(actor_network, 'RE Nisbett')
            distance_elements = [element[1] for element in list(bacon_numbers.items())]
            print(f"Mean KB distance: {sum(distance_elements) / len(distance_elements)}")
                
        elif choice == 4:
            author_name = input("Please Enter the name of the UMICH author only use space to separate the name:(e.g. 'Initials of first&middle name + ' ' + Lastname')")
            bacon_numbers = calculate_kevin_bacon_numbers(actor_network, author_name)
            distance_elements = [element[1] for element in list(bacon_numbers.items())]
            print(f"Mean KB distance: {sum(distance_elements) / len(distance_elements)}")
        
        if (YorN()):
            continue
        else:
            status = False
    print("Goodbye!")
    
if __name__ == "__main__":
    main()
        