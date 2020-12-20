"""Board Games."""
from functools import reduce


class Game:
    """Game class."""

    def __init__(self, name, score_kind):
        """Constructor."""
        self._name = name
        self._score_kind = score_kind
        self._players = {}
        self._played = 0
        self._numbers_of_people = []

    @property
    def name(self):
        """Return favorite game."""
        return self._name

    @property
    def players(self):
        """Return players."""
        return self._players

    @property
    def score_kind(self):
        """Return score kind."""
        return self._score_kind

    @property
    def played(self):
        """Return number of played games."""
        return self._played

    def add_participants(self, number):
        """How many people participated."""
        self._numbers_of_people.append(number)

    def add_player(self, player):
        """Add player to the game."""
        self._players[player.name] = player

    def add_game(self):
        """One more game played."""
        self._played += 1

    # ?? SHOULD BE DELETED ??
    def __eq__(self, other):
        """Define whether two game are of the same kind."""
        return self._name == other.kind

    def amount(self):
        """How many times {game} has been played."""
        return self._played

    def player_amount(self):
        """How many people usually play the game."""
        return max(set(self._numbers_of_people), key=self._numbers_of_people.count)

    def most_wins(self):
        """Who has the most wins in the game."""
        return reduce(lambda a1, a2: a1 if self._players[a1].won > self._players[a2].won else a2, self._players)

    def most_frequent_winner(self):
        """Who usually wins in the game."""
        return reduce(lambda a1, a2: a1 if self._players[a1].won / self._players[
            a1].games_played > self._players[a2].won / self._players[a2].games_played else a2, self._players)

    def most_losses(self):
        """Who has the most losses in the game."""
        return reduce(lambda a1, a2: a1 if self._players[a1].losses > self._players[a2].losses else a2, self._players)

    def most_frequent_loser(self):
        """Who usually loses the game."""
        return reduce(lambda a1, a2: a1 if (self._players[a1].losses / self._players[
            a1].games_played) > (self._players[a2].losses / self._players[a2].games_played) else a2, self._players)

    def record_holder(self):
        """Who has got the most points. WITH POINTS GAMES ONLY. viigi korral tagastame esimese tulemuse."""
        return reduce(lambda a1, a2: a1 if self._players[a1].points > self._players[a2].points else a2, self._players)


class Player:
    """Player class."""

    def __init__(self, name):
        """Constructor."""
        self._name = name
        self._wins = 0
        self._games_played = 0
        self._points = 0
        self._losses = 0
        self._game_counter = {}

    @property
    def name(self):
        """Return favorite game."""
        return self._name

    @property
    def points(self):
        """Return favorite game."""
        return self._points

    @property
    def amount(self):
        """Return number of played games."""
        return self._games_played

    @property
    def won(self):
        """Return how many games have been won."""
        return self._wins

    @property
    def losses(self):
        """Return how many game have been won."""
        return self._losses

    @property
    def games_played(self):
        """Return how many game have been won."""
        return self._games_played

    @property
    def favourite(self):
        """Return the favourite game of a person."""
        return max(self._game_counter)

    def add_result(self, result: str):
        """Add needed result to the winner."""
        if result == 'win':
            self._wins += 1
        elif result == 'lose':
            self._losses += 1

    def add_game(self, game_name):
        """Add one game to the number of played games."""
        self._games_played += 1
        if game_name in self._game_counter:
            self._game_counter[game_name] += 1
        else:
            self._game_counter[game_name] = 1

    def add_points(self, points):
        """Add points."""
        self._points += int(points)


class Statistics:
    """Statistics class."""

    def __init__(self, filename):
        """Statistic constructor."""
        self._filename = filename
        self._games = {}
        self._players = {}
        self._total = 0

    def read_data(self):
        """Process the data given in the file."""
        with open(self._filename, 'r') as f:
            data = f.readlines()
            data = list(map(lambda x: x.replace('\n', ''), data))

        for line in data:
            split_line = line.split(';')
            game = Game(split_line[0], split_line[-2])
            if game.name not in self._games:  # add game if needed
                self._games[game.name] = game
            self._games[game.name].add_game()
            participants = split_line[1].split(',')
            self._games[game.name].add_participants(len(participants))  # how many people participated
            for p in participants:  # p == player.name
                game_player, stat_player = Player(p), Player(p)  # storing one player in Stats and inside of Game
                self.add_players(game_player, stat_player, game)
                if game.score_kind != 'winner':  # use special method to process points and places type data
                    results = split_line[-1].split(',')
                    self.data_places_points(p, game, results, participants)
                else:
                    winner = split_line[-1]
                    self.data_winner(p, game, winner)  # use special method to process winner type data
                self._players[p].add_game(game.name)
                self._games[game.name].players[p].add_game(game.name)
            self._total += 1

    def add_players(self, game_player, stat_player, game):
        """Add players to Statistics.players and Game.players in needed."""
        if game_player.name not in self._games[game.name].players:
            self._games[game.name].add_player(game_player)
        if stat_player.name not in self._players:
            self._players[stat_player.name] = stat_player

    def data_places_points(self, p, game, results, participants):
        """
        Use an appropriate method to process data of a points or places kind.

        param: p - player's name
        param: game - game's name
        param: results - list with game results
        param: participants - list of people participated
        """
        if game.score_kind == 'points':
            self.points_data(p, game, results, participants)

        if game.score_kind == 'places':
            self.places_data(p, game, results)

    def points_data(self, p, game, results, participants):
        """Process points game type data."""
        self._players[p].add_points(results[participants.index(p)])
        self._games[game.name].players[p].add_points(results[participants.index(p)])

        if results[participants.index(p)] == max(results, key=lambda x: int(
                x) if x.isdigit() else x):
            self._players[p].add_result('win')
            self._games[game.name].players[p].add_result('win')
        if results[participants.index(p)] == min(results, key=lambda x: int(
                x) if x.isdigit() else x):
            self._players[p].add_result('lose')
            self._games[game.name].players[p].add_result('lose')

    def places_data(self, p, game, results):
        """Process places game type data."""
        if results[0] == p:
            self._players[p].add_result('win')
            self._games[game.name].players[p].add_result('win')

        if results[-1] == p:
            self._players[p].add_result('lose')
            self._games[game.name].players[p].add_result('lose')

    def data_winner(self, p, game, winner):
        """
        Analyze data for games of winner type.

        param: p - player's name
        param: game - game's name
        param: winner - winner of the game
        """
        if winner == p:
            self._games[game.name].players[p].add_result('win')

            self._players[p].add_result('win')

    def get(self, path: str):
        """Get the path of the file with the info what is asked.

        "/players" - tagastab listi mängijate nimedest (nimede järjekord pole oluline)
        "/games" - tagastab listi mängude nimedest (nimede järjekord pole oluline)
        "/total" - tagastab int-i, mis kirjeldab, mitu mängu on mängitud
        "/total/{result_type}" - kus {result_type} on string võimalike väärtustega points, places või winner,
        funktsioon peab tagastama, mitu seda tüüpi mängu on mängitud
        """
        if self._games == {}:  # read data if it's not yet done
            self.read_data()

        if path[:7] == '/player':
            return self.players_operation(path)

        elif path[:5] == '/game':
            return self.games_operation(path)

        elif path == '/total':
            return self._total

        elif path[:7] == "/total/":
            return self.total_operation(path)

    def players_operation(self, path):
        """Perform operations asked with command for a specified player."""
        if path == '/players':
            return [x for x in self._players]
        title, func = path.split('/')[2], path.split('/')[3]
        func = func.replace('-', '_')
        operation = eval(f'self._players["{title}"].{func}')
        return operation

    def games_operation(self, path):
        """Perform operations asked with command for a specified game."""
        if path == '/games':
            return [x for x in self._games]
        title, func = path.split('/')[2], path.split('/')[3]
        func = func.replace('-', '_')
        operation = eval(f'self._games["{title}"].{func}()')
        return operation

    def total_operation(self, path):
        """Perform operation asked with a command '/total'."""
        ret = 0
        for x in self._games:
            if self._games[x].score_kind == path[7:]:
                ret += self._games[x].played
        return ret


if __name__ == '__main__':
    s = Statistics('example.txt')
    print(s.get('/game/chess/most-losses'))
