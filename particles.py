me = 1  # electron_mass


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
        
  
bhabha = [Fermion(False, True, me, 'P_{1}'), Fermion(True, False, me, 'P_{2}'), Fermion(True, True, me, 'P_{3}'), Fermion(False, False, me, 'P_{4}')]
        
