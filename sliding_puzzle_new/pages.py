from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants

class Introduction(Page):
    pass

class instructions1(Page):
    pass

class instructions2(Page):
    pass

class instructions3(Page):
    pass

class instructions4(Page):
    pass

class instructions5(Page):
    pass





class Game1(Page):
    form_model = 'player'
    form_fields = ['puzzle_solved', 'move_history', 'payoff_display', 'num_of_moves', 'board_history']


    def get_timeout_seconds(self):
        return 300


    def js_vars(self):
            return {
                'game_id': 1,
                'player_id': self.player.id,
                'board': [ #self.session
                            [1, 3, 6],
                            [4, 2, 8],
                            [7, 5, None],       # The starting board will be randomized.
                        ]                     # Preferably around 5 to 8 moves away from the final state.

            }



class Game2(Page):
    form_model = 'player'
    form_fields = ['puzzle_solved'] #, 'move_history']

    def get_timeout_seconds(self):
        return 300

    def js_vars(self):

        return {
            'game_id': 2,
            'player_id': self.player.id,
            'board': [ #self.session
                            [1, 8, 2],
                            [None, 4, 3],
                            [7, 6, 5],
                            ]

            }

class Game3(Page):
    form_model = 'player'
    form_fields = ['puzzle_solved'] #, 'move_history']

    def get_timeout_seconds(self):
        return 300

    def js_vars(self):
        return {
            'game_id': 3,
            'player_id': self.player.id,
            'board': [  # self.session
                        [4, 1, 2],
                        [8, None, 3],
                        [5, 7, 6],
                        ]

            }

class Game4(Page):
    form_model = 'player'
    form_fields = ['puzzle_solved'] #, 'move_history']

    def get_timeout_seconds(self):
        return 300

    def js_vars(self):
        return {
            'game_id': 4,
            'player_id': self.player.id,
            'board': [ #self.session
                            [4, 2, None],
                            [7, 1, 3],
                            [8, 5, 6],
                        ]

        }

class Game5(Page):
    form_model = 'player'
    form_fields = ['puzzle_solved'] #, 'move_history']

    def get_timeout_seconds(self):
        return 300

    def js_vars(self):
        return {
            'game_id': 5,
            'player_id': self.player.id,
            'board': [ #self.session
                            [2, 4, 3],
                            [7, 1, 6],
                            [None, 5, 8],
                        ]

                }




class Results(Page):
    pass         # need to include how long participants take to finish and how much they earn


page_sequence = [Introduction,
                 instructions1, Game1, Results,
                 instructions2, Game2, Results,
                 instructions3, Game3, Results,
                 instructions4, Game4, Results,
                 instructions5, Game5, Results]
