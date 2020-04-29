from .. import models
import otree.api


class Page(otree.api.Page):
    player: models.Player



class Bot(otree.api.Bot):
    player: models.Player
