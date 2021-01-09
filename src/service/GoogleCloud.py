from google.cloud import storage

from src.abstract.LoggerAbstract import LoggerAbstract
from src.dto.ImageResponseDTO import ImageResponseDTO
from src.models import TeamModel, EventModel, CountryModel


class GoogleCloud(LoggerAbstract):
    def __init__(self):
        super(GoogleCloud, self).__init__()
        self.client = storage.Client()
        self.bucket = self.client.get_bucket('csgo_global_elite')

    def upload(self, folder: str, image_response_dto: ImageResponseDTO, img_name) -> bool:
        try:
            assert folder in self.folder_list(), f'{folder} doesnt have access'
            path = f'{folder}/{img_name}'

            exist = storage.Blob(bucket=self.bucket, name=path).exists(self.client)

            if not exist:
                blob = self.bucket.blob(path)
                blob.upload_from_string(
                    data=image_response_dto.blob,
                    content_type=image_response_dto.mime
                )

            return True
        except Exception as e:
            self.logger.error(e)
            return False

    @staticmethod
    def folder_list():
        return [
            TeamModel.google_storage_folder,
            EventModel.google_storage_folder,
            CountryModel.google_storage_folder,
        ]