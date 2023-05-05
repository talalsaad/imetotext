class data:
    def __init__(self, device_id, device_name, processor, installed_ram, system_type):
        self.id = device_id
        self.device_name = device_name
        self.processor = processor
        self.installed_ram = installed_ram
        self.system_type = system_type
    def __str__(self) :
        return f"Device ID : {self.id} \nDevice Name : {self.device_name} \nProcessor : {self.processor} \nInstalled RAM : {self.installed_ram} \nSystem Type : {self.system_type} \n"