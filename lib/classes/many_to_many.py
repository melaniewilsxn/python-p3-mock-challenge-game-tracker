class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise ValueError("Title cannot be changed once set.")
        
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Invalid title. Title must be a non-empty string.")

    def results(self):
        return[result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in Result.all if result.game == self})

    def average_score(self, player):
        player_scores = []
        for result in Result.all:
            if result.game == self and result.player == player:
                player_scores.append(result.score)
        return sum(player_scores)/len(player_scores)

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16:
            self._username = username
        else:
            raise ValueError("Invalid username. Username must be a string between 2 and 16 characters.")

    def results(self):
        return[result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in Result.all if result.player == self})
    
        # unique_games = []
        # for result in Result.all:
        #     if result.player == self and result.game not in unique_games:
        #         unique_games.append(result.game)

        # return unique_games

    def played_game(self, game):
        for result in Result.all:
            if result.player == self and result.game == game:
                return True
        return False

    def num_times_played(self, game):
        i=0
        for result in Result.all:
            if result.player == self and result.game == game:
                i+=1
        return i

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, '_score'):
            raise ValueError("Score cannot be changed once set.")

        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise ValueError("Invalid score. Score must be an integer between 1 and 5000.")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise TypeError("Player must be an instance of Player class.")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise TypeError("Game must be an instance of Game class.")