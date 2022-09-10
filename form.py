from typing import List
from typing import Optional

from fastapi import Request

class ContactForm:
    def __init__(self, request:Request):
        self.request: Request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.email: Optional[str] = None
        self.message: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("Name")
        self.email  = form.get("Email")
        self.message = form.get("Message")

    def is_valid(self):
        if not self.name:
            self.errors.append("Name required.")
        
        # this is not the best implementation to check for a valid email. Regex would be better.
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Valid Email required.")

        if not self.message or len(self.message) < 5:
            self.errors.append("Message too short.")
