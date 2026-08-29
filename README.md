# Civilization Simulation

A small terminal-based project for exploring how an ancient civilization might
grow and prosper.

The first version creates a random 15 x 15 world. Every position in the grid is
a `Tile` object containing:

- its `x` and `y` coordinates;
- a terrain type;
- food, wood, and stone resource amounts.

## Run it

```powershell
python Civilization.py
```

Map symbols: `.` grassland, `F` forest, `+` fertile land, `M` mountain, and `~`
water.
