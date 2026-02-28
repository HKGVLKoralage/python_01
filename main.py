class Vehicle:
    company_name = "National Transport Services"

    def __init__(self, vehicle_id , plate_number, capacity):
            self.vehicle_id = vehicle_id
            self.plate_number = plate_number
            self.capacity = capacity
            self._status = "available"
    def start(self):
        self._status = "On Trip"
        return f"Vehicle {self.plate_number} started trip."
    def stop(self):
        self._status = "available"
        return f"Vehicle {self.plate_number}  trip completed."
    def get_status(self):
        return self._status


class Bus(Vehicle):
    def __init__(self, vehicle_id, plate_number, capacity, route_number):
        super().__init__(vehicle_id, plate_number, capacity)
        self.route_number = route_number

    def calculate_fare(self, distance):
        fare_per_km = 2.5
        total_fare = fare_per_km * distance
        return  f"Total fare: ${total_fare}"


class Driver:
    def __init__(self, driver_id, name, license_number):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.assigned_vehicle = None
    def assign_vehicle(self, vehicle):
        self.assigned_vehicle = vehicle
        return f"Driver {self.name} assigned to vehicle {vehicle.plate_number}."


class Route:
    def __init__(self, route_number, start_point, end_point,distance):
        self.route_number = route_number
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance
    def route_info(self):
        print(f"Route {self.route_number}: {self.start_point} to {self.end_point}, Distance: {self.distance} km")

class Maintenance:
    @staticmethod
    def perform_service(vehicle):
        vehicle._status = "under maintenance"
        return f"Vehicle {vehicle.plate_number} is under maintenance."



bus1 = Bus("B001", "ABC-123", 5000, 101)
driver1 = Driver("D001", "John Doe", "L123456")


print(driver1.assign_vehicle(bus1))
print(bus1.start())
print(bus1.calculate_fare(10))
print(bus1.stop())
print(Maintenance.perform_service(bus1))