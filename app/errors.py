class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, visitor_name: str = ""):
        super().__init__(f"{visitor_name} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    def __init__(self, visitor_name: str = ""):
        super().__init__(f"{visitor_name}'s vaccine is outdated.")


class NotWearingMaskError(Exception):
    def __init__(self, visitor_name: str = ""):
        super().__init__(f"{visitor_name} is not wearing a mask.")