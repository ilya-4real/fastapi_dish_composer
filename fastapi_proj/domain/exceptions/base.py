from dataclasses import dataclass


@dataclass
class ApplicationException(Exception):
    status_code: int

    @property
    def message(self):
        return ""
