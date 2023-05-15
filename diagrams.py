class Photon:
    def __init__(self, conjugate, index, momentum):
        self.photon = True
        self.conjugate = conjugate
        self.index = index
        self.momentum = momentum
        self.polarized = False
        
    def generate_string(self):
        if self.conjugate:
            return "\epsilon^{ \ast }_{ " + self.index[0] + " } \left( " + self.momentum + " \right)"
        return "\epsilon_{ " + self.index[0] + " } \left( " + self.momentum + " \right)"
    
    
class Fermion:
    def __init__(self, bar, matter, mass, momentum):
        self.photon = False
        self.bar = bar
        self.matter = matter
        self.mass = mass
        self.momentum = momentum
        
    def generate_string(self):
        if self.matter:
            if self.bar:
                return "\bar{u} \left( " + self.momentum + " \right)"
            return "u \left( " + self.momentum + " \right)"
        elif self.bar:
            return "\bar{v} \left( " + self.momentum + " \right)"
        return "v \left( " + self.momentum + " \right)"
        

class FermionPropagator:
    def __init__(self, bar, matter, virtual, mass, momentum):
        self.photon = False
        self.mass = mass
        self.momentum = momentum
        
    def generate_string(self):
        return "S \left( " + self.momentum + " \right)"
                  
                  
class PhotonPropagator:
    def __init__(self, momentum, index):
        self.photon = True
        self.momentum = momentum
        self.index = index
        
    def generate_string(self):
        return "D_{ " + self.index[0] + " " + self.index[1] + " } \left( " + self.momentum + " \right)"}

                  
class Diagram:
    def __init__(self):
        pass

      
class  Perturbate:
    def __init__(self, particles):  # by deffinition these must be non-virtual states and thus on shell
        self.particles = particles
        
    def check_charge_conservation(self):
        result = 0
        for i in self.particles:
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
        if self.particles[a].bar != self.particles[b].bar:
            return True
        return False
      
    def find_tree_level(self):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
