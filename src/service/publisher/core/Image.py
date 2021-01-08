from urllib.parse import urlencode

from src.models import MatchModel
from src.service.ConfigService import ConfigService
from src.service.Screenshot import Screenshot


class Image:
    config: ConfigService
    screenshot: Screenshot

    def __init__(self):
        self.config = ConfigService()
        self.screenshot = Screenshot()

    """
    url: https://github.com/shmidtelson/csgo_bot_image_generator
    """

    def get(self, match: MatchModel):
        url = ConfigService.get_csgo_server_image_generator_url()
        params = {
            "team_won_name": match.team_won.title,
            "team_lose_name": match.team_lose.title,
            "championship_name": match.event.title,
            "team_won_score": match.score_won,
            "team_lose_score": match.score_lose,
            "match_type": match.match_kind.title,
        }
        full_url = f"{url}?{urlencode(params)}"
        image = self.screenshot.take_image(full_url)

        return image
