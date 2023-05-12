class FermiConnector:
    def __init__(self, bar, matter, virtual, photon, mass, momentum):
        self.photon = False
        self.bar = bar
        self.matter = matter
        self.virtual = virtual
        self.mass = mass
        self.momentum = momentum
        
    def generate_string(self):
        if self.vitual:
            return "S \left( " + self.momentum + " \right)"
        else:
            if self.matter:
                if self.bar:
                    return "\bar{u} \left( " + self.momentum + " \right)"
                else:
                    return "u \left( " + self.momentum + " \right)"
            else:
                if self.bar:
                    return "\bar{v} \left( " + self.momentum + " \right)"
                else:
                    return "v \left( " + self.momentum + " \right)"
                  
                  
class PhotoConnector:
    def __init__(self, star, virtual, momentum, index):
        self.photon = True
        self.star = star
        self.virtual = virtual
        self.momentum = momentum
        self.index = index
        
    def generate_string(self):
        if self.virtual:
            return "D_{ " + self.index[0] + " " + self.index[1] + " } \left( " + self.momentum + " \right)"}
        else:
            if self.star:
                return "\epsilon^{ \ast }_{ " + self.index[0] + " } \left( " + self.momentum + " \right)"
            else:
                return "\epsilon_{ " + self.index[0] + " } \left( " + self.momentum + " \right)"

                  
class Diagram:
    def __init__(self):
        pass

      
class  Perturbate:
    def __init__(self, inbound, outbound):  # by deffinition these must be non-virtual states and thus on shell
        self.inbound = inbound  # by definition either in-photon, (in-anti or vbar) or (in-matter or u)
        self.outbound = outbound  # by deffinition either out-pho, (out-anti or v) or (out-matter or ubar)
        
    def check_charge_conservation(self):
        initial_result = 0
        for i in self.inboud:
            if i.photon:
                continue
            if i.matter:
                initial_result += 1
            initial_result -= 1
        final_result = 0
        for j in self.outbound:
            if i.photon:
                continue
            if i.matter:
                final_result += 1
            final_result -= 1
        if initial_result == final_result:
            return True
        return False
      
    def find_tree_level(self):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
