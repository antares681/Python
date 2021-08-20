from Ex02_Movie_World.customer import Customer
from Ex02_Movie_World.dvd import DVD

class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer:Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        disk = [disk for disk in self.dvds if disk.id == dvd_id][0]
        # disk = list(filter(lambda d: d.id == dvd_id, self.dvds))[0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if disk in customer.rented_dvds:
            return f"{customer.name} has already rented {disk.name}"
        if disk.is_rented == True:
            return "DVD is already rented"
        if customer.age < disk.age_restriction:
            return f"{customer.name} should be at least {disk.age_restriction} to rent this movie"
        disk.is_rented = True
        customer.rented_dvds.append(disk)
        return f'{customer.name} has successfully rented {disk.name}'

    def return_dvd(self, customer_id, dvd_id):
        disk = [disk for disk in self.dvds if disk.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if disk in customer.rented_dvds:
            disk.is_rented = False
            customer.rented_dvds.remove(disk)
            return f"{customer.name} has successfully returned {disk.name}"
        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        disks = "\n".join([disks.__repr__() for disks in self.dvds])
        c = "\n".join([c.__repr__() for c in self.customers])
        result = f'{c}\n{disks}'
        return result
