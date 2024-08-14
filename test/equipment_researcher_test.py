#!/usr/bin/python3

class Equipment:
    def __init__(self, num_available_slots):
        self.num_available_slots = num_available_slots

    def get_available_slots(self):
        pass

    def reserve_first_available_slot(self):
        pass

class EquipmentReservation():
    pass

def test_reserve_first_available_slot():
    equipment = Equipment(num_available_slots=10)
    available_slots = equipment.get_available_slots()
    reservation = equipment.reserve_first_available_slot()

    assert reservation is not None
    assert len(equipment.get_available_slots()) == len(available_slots) - 1

def test_reserve_booked_up():
    equipment = Equipment(num_available_slots=0)
    reservation = equipment.reserve_first_available_slot()

    assert reservation is None
    assert len(equipment.get_available_slots()) == 0