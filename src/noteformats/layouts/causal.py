from __future__ import annotations

from ..geometry import Scene
from .flow import arrow


def causal_network(s: Scene, p: dict):
    cx, cy = (s.left+s.right)/2, (s.top+s.bottom)/2
    nodes=[(cx,cy-48),(cx-39,cy-13),(cx+39,cy-13),(cx-30,cy+43),(cx+30,cy+43)]
    r=14
    edges=[(0,1),(0,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
    for a,b in edges:
        x1,y1=nodes[a]; x2,y2=nodes[b]
        dx,dy=x2-x1,y2-y1
        length=(dx*dx+dy*dy)**0.5
        ux,uy=dx/length,dy/length
        arrow(s,x1+(r+2)*ux,y1+(r+2)*uy,x2-(r+2)*ux,y2-(r+2)*uy,"light")
    for x,y in nodes:
        s.circle(x,y,r,"normal")
        s.slot(x-9,y+2,18)


def hypothesis_evidence(s: Scene, p: dict):
    cx=(s.left+s.right)/2
    top_y=s.top+9
    s.rect(cx-32,top_y,64,32,"normal")
    s.slot(cx-28,top_y+17,56)
    y=s.top+75
    gap=5
    w=(s.width-2*gap)/3
    for n in range(3):
        x=s.left+n*(w+gap)
        s.rect(x,y,w,44,"normal")
        s.slot(x+3,y+17,w-6)
        arrow(s,cx,top_y+34,x+w/2,y-2,"light")
    bottom_y=s.bottom-39
    s.rect(s.left+15,bottom_y,s.width-30,34,"normal")
    s.slot(s.left+19,bottom_y+18,s.width-38)
    for n in range(3):
        x=s.left+n*(w+gap)+w/2
        arrow(s,x,y+46,cx,bottom_y-2,"light")


BUILDERS={
    "causal-network":causal_network,
    "hypothesis-evidence":hypothesis_evidence,
}
