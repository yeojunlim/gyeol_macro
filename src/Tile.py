from dataclasses import dataclass

Shape = {"circle": 0, "polygon": 1, "rect": 2}
BgColor = {"#1A1A1A": 0,"#8C8C8C": 1,"#F2F2F2": 2}
Color = {"#E03A3A": 0,"#F2C230": 1,"#2E7BE0": 2}
@dataclass
class Tile:
    shape: int
    bgcolor: int
    color: int

def make_tile(t) -> Tile:
    return Tile(
        shape = Shape[t.find("g").find().name],
        bgcolor = BgColor[t.find("svg").find("rect")["fill"]],
        color = Color[t.find("g")["fill"]]
    )