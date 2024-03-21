import logging
import random
from time import perf_counter


from space_collector.game.player import Player
from space_collector.game.planet import Planet
from space_collector.game.player_orientations import player_orientations
from space_collector.game.math import Vector
from space_collector.game.constants import MAX_NB_PLANETS


class Game:
    def __init__(self) -> None:
        self.start_time = perf_counter()
        self.last_update_time = self.start_time
        self.cumulated_time = 0
        self.players: list[Player] = []

        nb_planets = random.randint(2, MAX_NB_PLANETS)
        all_planets_positions = set()
        self.planets_positions = []
        while len(self.planets_positions) < nb_planets:
            planets_positions = set()
            planet = Planet(
                x=random.randrange(-7000, 7001, 1000),
                y=random.randrange(3000, 17001, 1000),
                size=random.randint(20, 40),
                id=random.randint(1, 65535),
            )
            planet_vector = Vector([planet.x, planet.y])
            for orientation in player_orientations:
                player_planet_position = orientation.rotate_around_base(planet_vector)
                planets_positions.add(tuple(player_planet_position))
            if len(planets_positions) < len(player_orientations):
                continue
            if planets_positions & all_planets_positions:
                # conflict with existing planets
                continue
            all_planets_positions.update(planets_positions)
            self.planets_positions.append(planet)

    def manage_command(self, player_id: int, command: str) -> str:
        if player_id >= len(self.players):
            logging.error("Unknown player ID: %d", player_id)
            return "BLOCKED"
        return self.players[player_id].manage_command(command)

    def add_player(self, player_name: str) -> None:
        if len(self.players) >= 4:
            return
        player = Player(player_name, self)
        player.reset_spaceships_and_planets(len(self.players), self.planets_positions)
        self.players.append(player)

    def update(self) -> None:
        delta_time = perf_counter() - self.last_update_time
        for player in self.players:
            player.update(delta_time)
        self.last_update_time += delta_time
        self.cumulated_time += delta_time
        logging.error(self.cumulated_time)

    def state(self) -> dict:
        return {
            "time": self.cumulated_time,
            "players": [player.state() for player in self.players],
        }
