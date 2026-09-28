"""Generate the original terminal UI animations; requires Pillow only.
No photo processing occurs here. Set PROFILE_MONO_FONT on non-Windows systems.
"""
from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BG, PANEL, LINE = '#080d14', '#101a25', '#213748'
TEXT, MUTED, CYAN, GREEN = '#eaf5ff', '#91a7b9', '#48dcff', '#6cf5b0'
FONT = os.getenv('PROFILE_MONO_FONT', 'C:/Windows/Fonts/consola.ttf')
if not Path(FONT).exists():
    FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

def font(n):
    return ImageFont.truetype(FONT, n)

def base(h, title):
    im = Image.new('RGB', (900, h), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, 899, h-1), radius=14, outline=LINE)
    d.line((26, 50, 874, 50), fill=LINE)
    d.text((27, 18), title, font=font(15), fill=MUTED)
    for i, c in enumerate([GREEN, CYAN, '#ab9cff']):
        d.ellipse((825+i*16, 24, 831+i*16, 30), fill=c)
    return im, d

def write(frames, name, hold=2500):
    p = ROOT / 'assets/ui' / (name+'.gif')
    p.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(p, save_all=True, append_images=frames[1:], duration=[80]*(len(frames)-1)+[hold], loop=0, optimize=True, disposal=1)
    static = ROOT / 'assets/static/ui' / (name+'.png')
    static.parent.mkdir(parents=True, exist_ok=True)
    frames[-1].save(static, optimize=True)
    print(name, p.stat().st_size, 'bytes', len(frames), 'frames')

frames=[]
modules=['NEURAL MODULES','COMPUTER VISION','GENERATIVE AI','AGENT SYSTEMS','CLOUD + LINUX','PROJECT DIRECTORY']
for f in range(64):
    im,d=base(324,'BOOT SEQUENCE / HARSHIT.KUMAR')
    cmd='$ ./initialize_profile --load-engineering-modules'
    d.text((28,69),cmd[:min(len(cmd),f*3+5)],font=font(22),fill=TEXT)
    if f<20 and f%6<3:
        x=28+d.textlength(cmd[:min(len(cmd),f*3+5)],font=font(22))
        d.rectangle((x+4,70,x+15,92),fill=GREEN)
    progress=min(1,max(0,(f-3)/44))
    d.rounded_rectangle((28,112,871,128),radius=4,fill=PANEL)
    if progress>0:d.rounded_rectangle((28,112,28+max(8,int(843*progress)),128),radius=4,fill=CYAN)
    for i,name in enumerate(modules):
        x=28+(i%2)*439;y=155+(i//2)*37
        active=f>=9+i*6
        d.text((x,y),('[OK] ' if active else '[..] ')+name,font=font(20),fill=GREEN if active else MUTED)
    d.line((28,277,872,277),fill=LINE)
    d.text((28,292),'SYSTEM ONLINE' if f>=47 else 'INITIALIZING PROFILE ENVIRONMENT',font=font(17),fill=GREEN if f>=47 else MUTED)
    d.text((778,292),f'{int(progress*100):3} %',font=font(17),fill=CYAN)
    frames.append(im)
write(frames,'boot',3500)

rows=[('IDENTITY','HARSHIT KUMAR'),('SPECIALIZATION','AI / ML'),('ENVIRONMENT','LINUX'),('PRIMARY LANGUAGE','PYTHON'),('FOCUS','AI SYSTEMS'),('PROJECTS','BUILDING'),('HACKATHONS','PARTICIPANT + WINNER'),('STATUS','ONLINE')]
frames=[]
for f in range(60):
    im,d=base(432,'PROFILE DIAGNOSTICS / IDENTITY RECORD')
    d.text((28,67),'$ sudo ./harshit_profile --deep-scan',font=font(23),fill=TEXT)
    for i,(k,v) in enumerate(rows):
        y=113+i*34
        d.text((28,y),k.ljust(19,'.'),font=font(20),fill=MUTED)
        if f>=i*5:
            shown=v[:min(len(v),(f-i*5)*2+1)]
            d.text((342,y),shown,font=font(21),fill=GREEN if i==7 else CYAN)
    d.text((28,404),'ENGINEERING RECORD / BUILD. TEST. ITERATE.',font=font(13),fill=MUTED)
    frames.append(im)
write(frames,'deep-scan',4500)
