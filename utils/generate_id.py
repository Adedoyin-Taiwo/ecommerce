import uuid


def generate_id(self):
    return uuid.uuid4().hex[:12].upper()
