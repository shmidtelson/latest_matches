from strict_hint import strict

from src.abstract.DBAbstract import DBAbstract
from src.models import EventModel
from src.repository.EventRepository import EventRepository
from src.service.creator.image_storage_creator import ImageStorageCreator


class EventCreator(DBAbstract):
    repository: EventRepository
    image_storage_creator: ImageStorageCreator

    def __init__(self):
        super().__init__()
        self.repository = EventRepository()
        self.image_storage_creator = ImageStorageCreator()

    @strict
    def create(self, title: str) -> EventModel:
        assert title != '', 'Event name doesnt be empty'

        event_model = self.repository.get_by_title(title=title)
        if event_model:
            return event_model

        event_model = EventModel()
        event_model.title = title

        self.db.add_model(event_model, need_flush=True)

        return event_model
