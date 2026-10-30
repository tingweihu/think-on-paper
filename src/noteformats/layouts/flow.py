from __future__ import annotations

from math import hypot

from ..geometry import Scene


def arrow(s: Scene, x1, y1, x2, y2, layer="normal"):
    s.line(x1, y1, x2, y2, layer)
    dx, dy = x2 - x1, y2 - y1
    length = hypot(dx, dy)
    if length < 2:
        return
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    s.line(x2, y2, x2 - 3.5*ux + 1.7*px, y2 - 3.5*uy + 1.7*py, layer)
    s.line(x2, y2, x2 - 3.5*ux - 1.7*px, y2 - 3.5*uy - 1.7*py, layer)


def flow_four_horizontal(s: Scene, p: dict):
    # A5 portrait needs more than a single row of tiny action boxes. Each
    # stage now has a short action area and three lines for evidence/notes.
    w, h = 24, 96
    gap = (s.width - 4*w) / 3
    y = (s.top + s.bottom - h) / 2
    for i in range(4):
        x = s.left + i*(w+gap)
        s.rect(x, y, w, h, "normal")
        for yy in (y + 33, y + 54, y + 75):
            s.line(x + 2, yy, x + w - 2, yy, "light")
        s.slot(x+2, y+17, w-4)
        if i < 3:
            arrow(s, x+w+1, y+h/2, x+w+gap-1, y+h/2, "light")


def flow_six_snake(s: Scene, p: dict):
    gap_x, w, h = 6, (s.width - 12)/3, 34
    top_y, bottom_y = s.top + 33, s.bottom - 33 - h
    for row in range(2):
        y = top_y if row == 0 else bottom_y
        for col in range(3):
            x = s.left + col*(w+gap_x)
            s.rect(x, y, w, h, "normal")
            s.slot(x+3, y+17, w-6)
    for col in range(2):
        x = s.left + col*(w+gap_x)
        arrow(s, x+w+1, top_y+h/2, x+w+gap_x-1, top_y+h/2, "light")
        arrow(s, x+w+gap_x-1, bottom_y+h/2, x+w+1, bottom_y+h/2, "light")
    right_cx = s.right - w/2
    arrow(s, right_cx, top_y+h+1, right_cx, bottom_y-1, "light")


def cycle_four(s: Scene, p: dict):
    cx, cy = (s.left+s.right)/2, (s.top+s.bottom)/2
    centers = [(cx,cy-43),(cx+43,cy),(cx,cy+43),(cx-43,cy)]
    r = 14
    for x,y in centers:
        s.circle(x,y,r,"normal")
        s.slot(x-9,y+2,18)
    for a,b in zip(centers,centers[1:]+centers[:1]):
        dx,dy=b[0]-a[0],b[1]-a[1]
        length=hypot(dx,dy)
        ux,uy=dx/length,dy/length
        arrow(s,a[0]+(r+2)*ux,a[1]+(r+2)*uy,b[0]-(r+2)*ux,b[1]-(r+2)*uy,"light")


def decision_tree(s: Scene, p: dict):
    cx = (s.left+s.right)/2
    root=(cx-20,s.top+10,40,26)
    s.rect(*root,"normal")
    s.slot(root[0]+3,root[1]+16,root[2]-6)
    middle_y=s.top+71
    for x in (s.left+12,s.right-43):
        s.rect(x,middle_y,31,27,"normal")
        s.slot(x+3,middle_y+16,25)
        arrow(s,cx,root[1]+root[3]+2,x+15.5,middle_y-2,"light")
    leaf_y=s.bottom-39
    leaf_w=(s.width-3*5)/4
    for i in range(4):
        x=s.left+i*(leaf_w+5)
        s.rect(x,leaf_y,leaf_w,30,"normal")
        s.slot(x+2,leaf_y+17,leaf_w-4)
        parent_x=(s.left+27.5) if i<2 else (s.right-27.5)
        arrow(s,parent_x,middle_y+29,x+leaf_w/2,leaf_y-2,"light")


def swimlane_flow(s: Scene, p: dict):
    lane_h=s.height/3
    for n in (1,2):
        y=s.top+n*lane_h
        s.line(s.left,y,s.right,y,"normal")
    boxes=[(s.left+5,s.top+15),(s.left+42,s.top+lane_h+15),(s.left+80,s.top+lane_h*2+15)]
    w,h=34,28
    for x,y in boxes:
        s.rect(x,y,w,h,"normal")
        s.slot(x+3,y+16,w-6)
    for (x1,y1),(x2,y2) in zip(boxes,boxes[1:]):
        arrow(s,x1+w+1,y1+h/2,x2-2,y2+h/2,"light")


def converging_flow(s: Scene, p: dict):
    left_x=s.left+2
    input_w,input_h=34,29
    ys=(s.top+13,(s.top+s.bottom)/2-input_h/2,s.bottom-13-input_h)
    out_x=s.right-44
    out_y=(s.top+s.bottom)/2-23
    for y in ys:
        s.rect(left_x,y,input_w,input_h,"normal")
        s.slot(left_x+3,y+17,input_w-6)
        arrow(s,left_x+input_w+2,y+input_h/2,out_x-2,out_y+23,"light")
    s.rect(out_x,out_y,42,46,"normal")
    s.slot(out_x+4,out_y+25,34)


BUILDERS={
    "flow-four-horizontal":flow_four_horizontal,
    "flow-six-snake":flow_six_snake,
    "cycle-four":cycle_four,
    "decision-tree":decision_tree,
    "swimlane-flow":swimlane_flow,
    "converging-flow":converging_flow,
}
