"""A very small terminal-based civilization world simulation."""

from dataclasses import dataclass
import random


MAP_WIDTH = 15
MAP_HEIGHT = 15

TERRAIN_SYMBOLS = {
    "grassland": ".",
    "forest": "F",
    "fertile_land": "+",
    "mountain": "M",
    "water": "~",
}

TERRAIN_RESOURCES = {
    "grassland": {"food": (1, 3), "wood": (0, 1), "stone": (0, 1)},
    "forest": {"food": (0, 2), "wood": (4, 8), "stone": (0, 1)},
    "fertile_land": {"food": (5, 9), "wood": (0, 2), "stone": (0, 1)},
    "mountain": {"food": (0, 1), "wood": (0, 1), "stone": (5, 9)},
    "water": {"food": (2, 5), "wood": (0, 0), "stone": (0, 0)},
}


@dataclass
class Tile:
    """One location in the world and the resources found there."""

    x: int
    y: int
    terrain: str
    resources: dict[str, int]

    @property
    def symbol(self) -> str:
        return TERRAIN_SYMBOLS[self.terrain]


class World:
    """A rectangular world made entirely from Tile objects."""

    def __init__(
        self,
        width: int = MAP_WIDTH,
        height: int = MAP_HEIGHT,
        seed: int | None = None,
    ) -> None:
        self.width = width
        self.height = height
        self._random = random.Random(seed)
        self.grid = self._generate_grid()

    def _generate_grid(self) -> list[list[Tile]]:
        return [
            [self._create_tile(x, y) for x in range(self.width)]
            for y in range(self.height)
        ]

    def _create_tile(self, x: int, y: int) -> Tile:
        terrain = self._random.choice(list(TERRAIN_SYMBOLS))
        resources = {
            resource: self._random.randint(minimum, maximum)
            for resource, (minimum, maximum) in TERRAIN_RESOURCES[terrain].items()
        }
        return Tile(x=x, y=y, terrain=terrain, resources=resources)

    def get_tile(self, x: int, y: int) -> Tile:
        """Return a tile by coordinate, raising IndexError when out of bounds."""
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError(f"Tile coordinate ({x}, {y}) is outside the world")
        return self.grid[y][x]

    def render(self) -> str:
        """Build the terminal representation of the world."""
        border = "+" + "+".join("---" for _ in range(self.width)) + "+"
        rows = [border]
        for row in self.grid:
            rows.append("|" + "|".join(f" {tile.symbol} " for tile in row) + "|")
            rows.append(border)
        legend = "  ".join(
            f"{symbol} {terrain.replace('_', ' ').title()}"
            for terrain, symbol in TERRAIN_SYMBOLS.items()
        )
        return "\n".join(rows + ["", legend])


def main() -> None:
    world = World()
    print("Ancient Civilization World (15 x 15)\n")
    print(world.render())


if __name__ == "__main__":
    main()
