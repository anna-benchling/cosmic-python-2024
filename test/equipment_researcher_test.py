#!/usr/bin/python3
from dataclasses import dataclass

@dataclass(frozen=True)
class Slot:
    length_minutes: int

@dataclass(frozen=True)
class AvailabilityPeriod:
    day_of_week_start: str
    time_of_day_start: str
    day_of_week_end: str
    time_of_day_end: str
    # Validation that the timing is correct?

@dataclass(frozen=True)
class Availability:
    periods: list[AvailabilityPeriod]

@dataclass(frozen=True)
class MaintenanceSchedule:
    crontab: str

class Equipment:
    def __init__(self,model:str,  availability: Availability, slot_length: Slot, maintenance_schedule: MaintenanceSchedule) -> None:
        self.model = model
        self.availability = availability
        self.slot_length = slot_length
        self.maintenance_schedule = maintenance_schedule

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