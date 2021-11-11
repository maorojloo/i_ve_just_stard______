class pc :

    def __init__(self,cpu,gpu,ram):
        self.cpu=cpu
        self.gpu=gpu
        self.ram=ram

    def get_cpu (self):
        print('hte cpu is',self.cpu)
    def get_gpu (self):
        print('hte gpu is',self.gpu)    
    def get_ram (self):
        print('hte ram is',self.ram)

mypc =pc("is", 2, "8gb ddr4")
mypc.get_cpu()
mypc.get_gpu()
mypc.get_ram()

"""
class car :
    def __init__(self,model,sokht,color,ring):
        self.model=model
        self.sokht=sokht
        self.color=color
        self.ring=ring

    def model_get(self):
        return self.model
    def color_get(self):
        return self.color    




sina = car(1400,'gass','red','iron')   
p405 = car(1379,'gass','black','iron') 
car_name = input('which car?:')
print('moedel {} and color is {}'.format(car_name.model_get(),car_name.color_get()) )

"""