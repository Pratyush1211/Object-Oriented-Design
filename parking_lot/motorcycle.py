import generic_details

class Motorcycle(generic_details.Vehicle):
    def __init__(self, licence_plate_no):
        super(Motorcycle, self).__init__(generic_details.VehicleSize.MOTORCYCLE, licence_plate_no, spot_size = 1)
    
    def can_fit_in_spot(self, spot):
        return True

motor = Motorcycle('FNTPM2933k')