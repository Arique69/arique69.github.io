# Builds the Arique logo kit (SVG masters). Run: python brand/build.py
import math, os
OUT=os.path.dirname(os.path.abspath(__file__))
BLUE, INK = "#2563eb", "#0f172a"
f=lambda v: f"{v:.2f}".rstrip('0').rstrip('.')
def poly(pts): return "M"+"L".join(f"{f(x)} {f(y)}" for x,y in pts)+"Z"
def rect(x,y,w,h): return poly([(x,y),(x+w,y),(x+w,y+h),(x,y+h)])
def P(cx,cy,r,t): a=math.radians(t); return f"{f(cx+r*math.cos(a))} {f(cy+r*math.sin(a))}"
def circ(cx,cy,r): return f"M{f(cx-r)} {f(cy)}A{r} {r} 0 1 0 {f(cx+r)} {f(cy)}A{r} {r} 0 1 0 {f(cx-r)} {f(cy)}Z"
def ring(cx,cy,R,r): return circ(cx,cy,R)+circ(cx,cy,r)

def tile(dx=-6):
    """Rounded tile with 'A_' cut out as real holes. dx centres the A_ group optically."""
    o="M56 16H200A40 40 0 0 1 240 56V200A40 40 0 0 1 200 240H56A40 40 0 0 1 16 200V56A40 40 0 0 1 56 16Z"
    k=52/132; ix=lambda y: 132-(190-y)*k
    A=[(108,58),(160,190),(132,190),(ix(176),176),(216-ix(176),176),(84,190),(56,190)]
    apex=190-(132-108)/k
    C=[(108,apex),(ix(154),154),(216-ix(154),154)]
    sh=lambda pts:[(x+dx,y) for x,y in pts]
    return o+poly(sh(A))+poly(sh(C))+rect(170+dx,172,42,18)

R,r,S=60,32,28
def wordmark(x=0):
    d=[]
    d+=[ring(x+R,120,R,r), rect(x+2*R-S,60,S,120)]; x+=2*R+22
    d+=[rect(x,60,S,120), f"M{x} 120A{R} {R} 0 0 1 {x+R} 60L{x+R+8} 60L{x+R+8} 88L{x+R} 88A{r} {r} 0 0 0 {x+S} 120Z"]; x+=R+8+18
    d+=[rect(x,60,S,120), circ(x+S/2,28,17)]; x+=S+22
    d+=[ring(x+R,120,R,r), rect(x+2*R-S,60,S,176)]; x+=2*R+22
    d+=[rect(x,60,S,61), f"M{x} 120A{R} {R} 0 0 0 {x+2*R} 120L{x+2*R-S} 120A{r} {r} 0 0 1 {x+S} 120Z", rect(x+2*R-S,60,S,120)]; x+=2*R+20
    cx=x+R
    d+=[f"M{P(cx,120,R,0)}A{R} {R} 0 1 0 {P(cx,120,R,38)}L{P(cx,120,r,38)}A{r} {r} 0 1 1 {P(cx,120,r,0)}Z", rect(cx-r-2,106,R+r+2,28)]
    return d, x+2*R

def paths(ds,fill): return "".join(f'<path fill="{fill}" fill-rule="evenodd" d="{d}"/>' for d in ds)
def svg(w,h,body,title="Arique"): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img"><title>{title}</title>{body}</svg>\n'
def save(name,s): open(os.path.join(OUT,name),"w",encoding="utf-8").write(s)

wm,ww=wordmark(0)
GAP=48; LW=int(256+GAP+ww+8)
for suffix,tf,wf in [("",BLUE,INK),("-white","#fff","#fff"),("-black","#000","#000")]:
    save(f"arique-symbol{suffix}.svg", svg(256,256,paths([tile()],tf)))
    save(f"arique-lockup{suffix}.svg", svg(LW,256,paths([tile()],tf)+f'<g transform="translate({256+GAP} 8)">'+paths(wm,wf)+'</g>'))

# Social preview 1200x630
lock=paths([tile()],BLUE)+f'<g transform="translate({256+GAP} 8)">'+paths(wm,INK)+'</g>'
s=0.62; lx=(1200-LW*s)/2
og=(f'<rect width="1200" height="630" fill="#f6f8fc"/>'
    f'<g transform="translate({f(lx)} 170) scale({s})">{lock}</g>'
    f'<text x="600" y="420" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="40" font-weight="600" fill="{INK}">Muhammad Rizq Athariq</text>'
    f'<text x="600" y="472" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="28" fill="#56607a">Web Developer · Laravel · Python · Astro</text>')
save("og-image.svg", svg(1200,630,og,"Arique, Muhammad Rizq Athariq"))
print("lockup width", LW)
