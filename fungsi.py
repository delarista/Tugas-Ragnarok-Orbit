class Person(object):
    def __init__(self, input_first_name, input_last_name, input_gender, input_alamat):
        self.first_name = input_first_name
        self.last_name = input_last_name
        self.gender = input_gender
        self.alamat = input_alamat
    
    def Info(self):
        print(f"Nama: {self.first_name} {self.last_name}, gender: {self.gender}, alamat: {self.alamat}")

class Manager(Person):
    def __init__(self, input_first_name, input_last_name, input_gender, input_alamat, input_email):
        super().__init__(input_first_name, input_last_name, input_gender, input_alamat)
        self.email = input_email
    
    def InfoManager(self):
        super().Info()
        print(f"Nama: {self.first_name} {self.last_name}, gender: {self.gender}, alamat: {self.alamat}, email: {self.email}")


class Employee(Person):
    insentif_lembur = 50000
    def __init__(self, input_first_name, input_last_name, input_gender, input_alamat, input_pendapatan):
        super().__init__(input_first_name, input_last_name, input_gender, input_alamat)
        self.pendapatan = input_pendapatan
        self.pendapatan_tambahan = 0
    
    def Lembur(self):
        return self.pendapatan_tambahan + Employee.insentif_lembur
    
    def TotalPendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
     
    def InfoEmployee(self):
        super().Info()
        print(f"Total Pendapatan: {self.pendapatan}")


class Customer(Person):
    def __init__(self, input_first_name, input_last_name, input_gender, input_alamat, input_id_customer):
        super().__init__(input_first_name, input_last_name, input_gender, input_alamat)
        self.id_customer = input_id_customer
        
    def Order(self, input_tanggal, input_status):
        self.tanggal = input_tanggal
        self.status = input_status
        print("Order Tanggal: ", input_tanggal)
        print("Status: ", input_status)
        
    def InfoCustomer(self):
        print(f"ID Customer: {self.id_customer}")
        super().Info()
        

