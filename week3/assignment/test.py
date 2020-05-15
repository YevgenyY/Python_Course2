class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def _gen_map(self, grid):
        # no checking if grid is correct

        # initialize grids
        height = len(grid)
        width = len(grid[0])

        self.adaptee.set_dim( (height, weight) )
        self.newgrid = [[0 for i in range(width)] for _ in range(height)]

        # calculate lights/obstacles indexes
        lights = []
        obstacles = []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    self.adaptee.grid[j][i] = 1
                    lights.append( (j, i) ) # use reverse coordinates
                if grid[i][j] == -1:
                    self.adaptee.grid[j][i] = -1
                    obstacles.append( (j, i) ) # use reverse coordinates
        
        self.adaptee.set_lights( lights )
        self.adaptee.set_obstacles( obstacles )

        # call lightening
        tmp = self.adaptee.generate_lights()

        # recalculate grid
        for i in range(height):
            for j in range(width):
                #print("{} {}".format(i, j))
                self.newgrid[i][j] = tmp[j][i]

        return self.newgrid.copy()

    def lighten(self, grid):
        # calculate light
        return self._gen_map(grid)
        
