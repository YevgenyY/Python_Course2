class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []
        
    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
    
    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()
    
    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()
        
    def generate_lights(self):
        return self.grid.copy()

class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1 # Источники света
        self.map[5][2] = -1 # Стены
    
    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)
        return self.lightmap

class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def _gen_map(self, grid):
        # no checking if grid is correct

        # initialize grids
        height = len(grid)
        width = len(grid[0])

        self.adaptee.set_dim( (height, width) )
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
        
obj = System()
light_obj = Light((0,0))
adapter = MappingAdapter(light_obj)

res = obj.get_lightening(adapter)
print(res)
