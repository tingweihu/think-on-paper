from __future__ import annotations

from ..geometry import Scene


def top_excerpt_bottom_thoughts(s: Scene, p: dict):
    quote_h=s.height*0.43
    s.rect(s.left,s.top,s.width,quote_h,"normal")
    for n in range(1,7):
        y=s.top+n*quote_h/7
        s.line(s.left+6,y,s.right-6,y,"light")
    s.slot(s.left+6,s.top+18,s.width-12)
    thought_y=s.top+quote_h+12
    s.line(s.left,thought_y,s.right,thought_y,"strong")
    for n in range(1,8):
        y=thought_y+n*(s.bottom-thought_y)/9
        s.line(s.left+6,y,s.right-6,y,"light")
    s.slot(s.left+6,thought_y+16,s.width-12)


def claim_four_evidence(s: Scene, p: dict):
    cx=(s.left+s.right)/2
    s.rect(s.left+12,s.top+7,s.width-24,33,"strong")
    s.slot(s.left+17,s.top+26,s.width-34)
    card_w=(s.width-8)/2; card_h=54
    ys=[s.top+59,s.top+123]
    for row,y in enumerate(ys):
        for col in range(2):
            x=s.left+col*(card_w+8)
            s.rect(x,y,card_w,card_h,"normal")
            for n in range(1,4):
                yy=y+n*card_h/4
                s.line(x+4,yy,x+card_w-4,yy,"light")
            s.slot(x+4,y+18,card_w-8)
    s.line(cx,s.top+40,cx,s.top+50,"light")
    s.line(s.left+card_w/2,s.top+50,s.right-card_w/2,s.top+50,"light")


def source_network_notes(s: Scene, p: dict):
    cx=(s.left+s.right)/2
    sources=[(s.left+15,s.top+27),(cx,s.top+22),(s.right-15,s.top+27)]
    for x,y in sources:
        s.circle(x,y,11,"normal")
        s.slot(x-8,y+2,16)
    note_y=s.top+89
    cards=[]
    for i in range(3):
        x=s.left+i*(s.width/3)+2
        w=s.width/3-4
        s.rect(x,note_y,w,60,"normal")
        s.slot(x+3,note_y+19,w-6)
        cards.append((x+w/2,note_y))
    for i,(x,y) in enumerate(sources):
        s.line(x,y+12,cards[i][0],note_y-2,"light")
    s.line(sources[0][0]+9,sources[0][1]+7,cards[1][0]-3,note_y-2,"light")
    s.line(sources[2][0]-9,sources[2][1]+7,cards[1][0]+3,note_y-2,"light")
    s.line(s.left+4,s.bottom-19,s.right-4,s.bottom-19,"strong")
    s.slot(s.left+5,s.bottom-8,s.width-10)


BUILDERS={
    "top-excerpt-bottom-thoughts":top_excerpt_bottom_thoughts,
    "claim-four-evidence":claim_four_evidence,
    "source-network-notes":source_network_notes,
}
