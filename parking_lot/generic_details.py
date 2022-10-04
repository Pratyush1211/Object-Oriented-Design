from abc import ABCMeta, abstractmethod


class VehicleSize:
    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2

# blueprint for vehicles
class Vehicle(metaclass = ABCMeta):

    def __init__(self, vehicle_size, licence_plate_no, spot_size) -> None:
        self.vehicle_size = vehicle_size
        self.licence_plate_no = licence_plate_no
        self.spot_size = spot_size
        self.spots_taken = []

    def clear_spots(self):
        for spots in self.spots_taken:
            spots.remove_vehicle(self)
        self.spots_taken = []
    
    def take_spot(self, spot):
        self.spots_taken.append(spot)
    
    @abstractmethod
    def can_fit_in_spot(self,spot):
        pass

        