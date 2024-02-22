class Node():
    '''Class for A* Pathfinding'''
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 # Cost from start to destination
        self.h = 0 # Heuristic (estimated cheapest cost to destination)
        self.f = 0 # Total path cost
        

    def __eq__(self, other):
        return self.position == other.position
    



def astar(maze, start, end):
    '''Returns a list of tuples as a path from the given start to the given end in a maze'''

    # Create start and end node
    start_node = Node(None, start) # Node with no parent at start-position
    start_node.g = start_node.h = start_node.f = 0 # Making the cost = 0
    end_node = Node(None, end) # End node has no parent before path is made
    end_node.g = end_node.h = end_node.f = 0


    # Initialize both open and closed list
    open_list = [] # queue for nodes that needs to be check for minimum cost
    closed_list = [] # already evaluated nodes

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                # If the cost of the node being checked is less than the current_node,
                # set the current node to the node being checked
                current_node = item
                current_index = index
        
        # Pop current off open list, add to closed list
        open_list.pop(current_index) # removes current_index
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent # Goes to the previous node
            return path[::-1] # return reversed path
        

        # Generate children
        children = []
        for new_position in [(0,-1), (0,1), (-1, 0), (1, 0), (-1,-1), (-1,1), (1,-1), (1,1)]: # Adjacent squares
            
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0 :
                continue
                # Stops if not within range
            
            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 1:
                continue
                # If value of node is 1 -> STOP
            
            # Create new node
            new_node = Node(current_node, node_position) # Creates a new node with the current node as parent

            # Appends to the child list
            children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                    # Create the f, g and h values:
                    child.g = current_node.g + 1 # This node is 1 unit away from the previous node
                    child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1])**2) # Using pythagoras as heuristic
                    child.f = child.g + child.h

                    # Child is already in the open list
                    for open_node in open_list:
                        if child == open_node and child.g > open_node.g:
                            continue 
                            # Stop iteration if child is in open list
                    
                    # Add the child to the open list
                    open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
    
