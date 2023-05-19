import particles as pp

                  
class Diagram:
    def __init__(self):
        pass

      
class Perturbate:
    def __init__(self, particles):  # by definition these must be non-virtual states and thus on shell
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
        if (self.particles[a].photon or self.particles[b].photon) \
                and not (self.particles[a].photon and self.particles[b].photon):
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
                result.append(((0, 1), (2, 3)))
        if self.check_vertex_current_compatibility(0, 2):
            if self.check_vertex_current_compatibility(1, 3):
                result.append(((0, 2), (1, 3)))
        if self.check_vertex_current_compatibility(0, 3):
            if self.check_vertex_current_compatibility(1, 2):
                result.append(((0, 3), (1, 2)))
        return result

    def find_tree_level_vertices(self):
        leaf = []
        for l in range(0, len(self.particles)):
            leaf.append(l)
        p = []

        def reduce(s, q):
            if not s:
                p.append(q)
            else:
                for i in range(1, len(s)):
                    if self.check_vertex_current_compatibility(s[0], s[1]):
                        new_q = []
                        for j in q:
                            new_q.append(j)
                        new_q.append((s[0], s[i]))
                        new_s = []
                        for k in range(1, len(s)):
                            if k != i:
                                new_s.append(s[k])
                        reduce(new_s, new_q)

        reduce(leaf, [])
        return p


lemon = Perturbate(pp.bhabha)
print(lemon.find_tree_level_vertices())

        
        
        
        
        
        
        
        
        
        
        
        
        
        
