from collections.abc import Generator
from bs4 import BeautifulSoup
from Tile import Tile, make_tile

# const isHap = (x,y,z) =>
#   (x.s+y.s+z.s)%3===0 && (x.b+y.b+z.b)%3===0 && (x.f+y.f+z.f)%3===0;

def _is_hap(t1: Tile, t2: Tile, t3: Tile) -> bool:
    return (
        (t1.shape + t2.shape + t3.shape) % 3 == 0
        and (t1.bgcolor + t2.bgcolor + t3.bgcolor) % 3 == 0
        and (t1.color + t2.color + t3.color) % 3 == 0
    )

# function allHapsIn(tiles){
#   const out=[];
#   for(let i=0;i<7;i++)for(let j=i+1;j<8;j++)for(let k=j+1;k<9;k++)
#     if(isHap(tiles[i],tiles[j],tiles[k])) out.push([i,j,k]);
#   return out;
# }

def get_haps(src: str) -> Generator[tuple[int, int, int]]:
    soup = BeautifulSoup(src, "html.parser")
    tiles = soup.find("div", {"id": "grid"})
    if not tiles: return

    parsed = [
        make_tile(t) for t in tiles.select(".tile")
    ]

    for i in range(7):
            for j in range(i + 1, 8):
                for k in range(j + 1, 9):
                    if _is_hap(parsed[i], parsed[j], parsed[k]):
                        yield (i + 1, j + 1, k + 1)