import particles.py as pp

                  
class Diagram:
    def __init__(self):
        pass

      
class  Perturbate:
    def __init__(self, particles):  # by deffinition these must be non-virtual states and thus on shell
        self.particles = particles
        
    def check_charge_conservation(self):
        result = 0
        for i in self.particles:
            if i.photon:
                continue
            if i.matter:
                if i.bar:
                    result -= 1
                    continue
                result += 1
                continue
            if i.bar:
                result -= 1
                continue
            result += 1
        if result == 0:
            return True
        return False
    
    def check_vertex_current_compatibility(self, a, b):
        if self.particles[a].photon xor self.particles[b].photon:
            return True
        elif self.particles[b].photon:
            return False
        if self.particles[a].mass == self.particles[b].mass:
            if self.particles[a].bar != self.particles[b].bar:
                return True
        return False
      
    def find_tree_level_vertices_2x2(self):
        result = []
        if self.check_vertex_current_compatibility(0, 1):
            if self.check_vertex_current_compatibility(2, 3):
                result.append(((0, 1),(2, 3)))
        if self.check_vertex_current_compatibility(0, 1):
            if self.check_vertex_current_compatibility(2, 3):
                result.append(((0, 2),(1, 3)))
        if self.check_vertex_current_compatibility(0, 1):
            if self.check_vertex_current_compatibility(2, 3):
                result.append(((0, 3),(1, 3)))
        return result
        
         
lemons = Perturbate(pp.bhabha)     
print(lemons.find_tree_level_vertices_2x2())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
