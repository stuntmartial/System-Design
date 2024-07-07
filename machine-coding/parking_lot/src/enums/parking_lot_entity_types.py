from enum import Enum


class ParkingLotEntityType(Enum):

    ENTRY_GATE = 'ENTRY_GATE'
    EXIT_GATE = 'EXIT_GATE'
    PARKING_SPOT = 'PARKING_SPOT'
    INVALID_PARKING_LOT_ENTITY = 'INVALID_PARKING_LOT_ENTITY'
