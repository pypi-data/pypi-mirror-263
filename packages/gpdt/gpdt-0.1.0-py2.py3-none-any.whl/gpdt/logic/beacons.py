"""
Implement some logic

"""

# ---------------------------------------------------------
# Import models
# ---------------------------------------------------------
from typing import List
from ..models.beacons import Person, MessageBox


# ---------------------------------------------------------
# Define logic
# ---------------------------------------------------------
class MailBox:
    def __init__(self) -> None:
        pass

    def send(self, message: MessageBox) -> bool:
        return True

    def list(self, person: Person) -> List[str]:
        pass

    def get(self) -> MessageBox:
        pass
