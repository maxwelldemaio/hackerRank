class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        # Make start/destination dict
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        """Get all paths from start to end"""
        path = path + [start]
        if start == end:
            # Flight start and end are the same
            # Base condition 
            return [path]
        if start not in self.graph_dict:
            # Where no flights originate from location
            return []

        paths = []

        # Ex) Mumbai to New York
        # Go through all routes from Mumbai
        # Take all those endpoints and go through their routes
        # If we end up at New York
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start,end))

    start = "Mumbai"
    end = "New York"
    print(f"Shortest path from {start} to {end}:", route_graph.get_shortest_path(start, end))
