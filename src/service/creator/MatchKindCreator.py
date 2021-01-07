from src.abstract.DBAbstract import DBAbstract
from src.models import EventModel, MatchKindModel
from src.repository.MatchKindRepository import MatchKindRepository


class MatchKindCreator(DBAbstract):
    repository: MatchKindRepository

    def __init__(self):
        super().__init__()
        self.repository = MatchKindRepository()

    def create(self, title: str, commit: bool = False) -> MatchKindModel:
        assert title != '', 'Match kind name doesnt be empty'

        match_kind_model = self.repository.get_by_title(title=title)
        if match_kind_model:
            return match_kind_model

        match_kind_model = MatchKindModel()
        match_kind_model.title = title

        self.db.add_model(match_kind_model, need_flush=True)

        if commit:
            self.db.commit()

        return match_kind_model
