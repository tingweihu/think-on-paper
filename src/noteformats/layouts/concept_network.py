from __future__ import annotations

from math import cos, hypot, pi, sin

from ..geometry import Scene


def _edge(s: Scene, a, b, ra=0, rb=0, layer="light"):
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = hypot(dx, dy)
    ux, uy = dx / length, dy / length
    s.line(a[0] + ux * ra, a[1] + uy * ra,
           b[0] - ux * rb, b[1] - uy * rb, layer)


def _node(s: Scene, x, y, r=12, layer="normal"):
    s.circle(x, y, r, layer)
    s.slot(x - r + 2, y + 2, 2*r - 4)


def mindmap_six(s: Scene, p: dict):
    cx, cy = (s.left+s.right)/2, (s.top+s.bottom)/2
    satellites = [(cx + 45*cos(-pi/2+i*pi/3), cy + 64*sin(-pi/2+i*pi/3)) for i in range(6)]
    for pt in satellites:
        _edge(s, (cx,cy), pt, 19, 13)
    _node(s,cx,cy,18,"strong")
    for x,y in satellites:
        _node(s,x,y,12)


def asymmetric_branches(s: Scene, p: dict):
    cx=s.left+20; cy=(s.top+s.bottom)/2
    s.rect(cx-13,cy-19,26,38,"strong")
    s.slot(cx-10,cy+2,20)
    branches=[(s.left+68,s.top+33),(s.left+75,cy),(s.left+69,s.bottom-31)]
    leaves=[(s.right-14,s.top+20),(s.right-12,s.top+51),(s.right-13,cy-16),(s.right-14,cy+18),(s.right-14,s.bottom-29)]
    for b in branches:
        _edge(s,(cx+13,cy),b,1,11)
        _node(s,*b,10)
    for parent,leaf in [(0,0),(0,1),(1,2),(1,3),(2,4)]:
        _edge(s,branches[parent],leaves[leaf],11,8)
    for x,y in leaves:
        _node(s,x,y,7,"light")


def double_center_mindmap(s: Scene, p: dict):
    cx=(s.left+s.right)/2
    cores=[(cx,s.top+54),(cx,s.bottom-54)]
    leaves=[(s.left+20,s.top+25),(s.right-20,s.top+25),(s.left+20,s.top+82),(s.right-20,s.top+82),
            (s.left+20,s.bottom-82),(s.right-20,s.bottom-82),(s.left+20,s.bottom-25),(s.right-20,s.bottom-25)]
    _edge(s,cores[0],cores[1],17,17,"normal")
    for i,leaf in enumerate(leaves):
        _edge(s,cores[0 if i<4 else 1],leaf,17,10)
    for x,y in cores:
        _node(s,x,y,16,"strong")
    for x,y in leaves:
        _node(s,x,y,9)


def triple_core_network(s: Scene, p: dict):
    cx=(s.left+s.right)/2; cy=(s.top+s.bottom)/2
    cores=[(cx,cy-35),(cx-34,cy+25),(cx+34,cy+25)]
    leaves=[(cx,cy-76),(s.left+13,cy-33),(s.right-13,cy-33),(s.left+14,cy+70),(s.right-14,cy+70)]
    for a,b in ((0,1),(0,2),(1,2)):
        _edge(s,cores[a],cores[b],15,15,"normal")
    for core,leaf in ((0,0),(1,1),(2,2),(1,3),(2,4)):
        _edge(s,cores[core],leaves[leaf],15,9)
    for x,y in cores:
        _node(s,x,y,14,"strong")
    for x,y in leaves:
        _node(s,x,y,8)


def cluster_ring(s: Scene, p: dict):
    cx=(s.left+s.right)/2; cy=(s.top+s.bottom)/2
    groups=[(cx-31,cy-47),(cx+31,cy-47),(cx-31,cy+47),(cx+31,cy+47)]
    s.circle(cx,cy,18,"light")
    s.slot(cx-14,cy+2,28)
    for x,y in groups:
        s.circle(x,y,24,"normal")
        s.circle(x-7,y-4,5,"light")
        s.circle(x+7,y+5,5,"light")
        s.slot(x-13,y+17,26)


def constellation_network(s: Scene, p: dict):
    cx=(s.left+s.right)/2; cy=(s.top+s.bottom)/2
    pts=[(cx-31,cy-69),(cx+19,cy-71),(cx+45,cy-31),(cx+26,cy+9),
         (cx+43,cy+66),(cx-5,cy+55),(cx-43,cy+32),(cx-46,cy-22)]
    for a,b in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,0),(1,7),(2,5),(3,6)):
        _edge(s,pts[a],pts[b],8,8)
    for x,y in pts:
        _node(s,x,y,7)


def bipartite_network(s: Scene, p: dict):
    ys=[s.top+27+i*42 for i in range(4)]
    left=[(s.left+16,y) for y in ys]
    right=[(s.right-16,y) for y in ys]
    for a,b in ((0,0),(0,1),(1,1),(1,3),(2,0),(2,2),(3,2),(3,3)):
        _edge(s,left[a],right[b],13,13)
    for x,y in left+right:
        _node(s,x,y,11)


BUILDERS={
    "mindmap-six":mindmap_six,
    "asymmetric-branches":asymmetric_branches,
    "double-center-mindmap":double_center_mindmap,
    "triple-core-network":triple_core_network,
    "cluster-ring":cluster_ring,
    "constellation-network":constellation_network,
    "bipartite-network":bipartite_network,
}
