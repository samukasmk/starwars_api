from datetime import datetime

import mongoengine


class BaseDocument(mongoengine.Document):
    """Base model object"""

    # Force each child object to define its collection on models inheritance
    meta = {"abstract": True, "allow_inheritance": False}

    # Auditing fields
    created_at = mongoengine.DateTimeField(required=True)
    updated_at = mongoengine.DateTimeField(required=True, default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)
