#todo change everything from hackish to stylish
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import PyPDF2
import io
from datetime import datetime
def timestamp(my_canvas):
    my_canvas.setFont('Helvetica', 16)
    now = datetime.now()
    uhrzeit = now.strftime("%H:%M:%S")+" Uhr"
    datum = now.strftime("%d.%m.%Y")
    my_canvas.drawString(90+15+60, 10, " PDF Merge by Marco Kittel, ausgeführt am "+ datum+ " um "+ uhrzeit)
    #my_canvas.drawImage('youtube.png', 1300, 150, width=50, preserveAspectRatio=True, mask='auto')
def youtube(my_canvas,x=0,y=0):
    my_canvas.setFont('Helvetica-Bold', 32)
    my_canvas.drawImage('youtbe.png', 1300+x, 0+200+y, width=200, preserveAspectRatio=True, mask='auto')
    #my_canvas.drawString(1165+90+15+60+x, 200+60+y,'Video von mir zur PDF Erzeugung')
    my_canvas.setFont('Helvetica', 20)
    my_canvas.drawString(1345+90+15+40+x, 200+65+y,'https://youtu.be/18QtztXJ-mc')
    my_canvas.drawString(1345+90+15+40+x, 200+40+y,'https://youtu.be/_9EFi-L2HmI')
    my_canvas.drawString(1345+90+15+40+x, 200+15+y,'https://youtu.be/bnTPVeZwaC4')
def getHeader():
    packet = io.BytesIO()
    width = 2143
    my_canvas = canvas.Canvas(packet, pagesize=(width,200*mm))
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica-Bold', 76)
    my_canvas.drawString(90+15+60, 450+30, 'Achtung')
    my_canvas.setFont('Helvetica-Bold', 42)
    my_canvas.drawString(90+15+60, 200+150, 'Dieses PDF ist ein automatischer Merge.')
    my_canvas.drawString(90+15 +60, 150+150,'Aufgrund diverser neuer Udemy Kurse')
    my_canvas.drawString(90+15+60, 100+150,'wurde dieser Prozess automatisiert. ')
    my_canvas.setFont('Helvetica-Bold', 16)
    my_canvas.drawString(90+15+60, 50+150,'Das Seitenverhältnis der Udemy-Zertifikate wurde an das Verhältnis 1,414 DIN/A4 angepasst.')
    timestamp(my_canvas)
    youtube(my_canvas,300,-200)
    my_canvas.save()
    packet.seek(0)
    return packet
def sign():
    width = 2143
    packet = io.BytesIO()
    my_canvas = canvas.Canvas(packet, pagesize=(width,200*mm))
    timestamp(my_canvas)
    youtube(my_canvas,300,-200)
    my_canvas.save()
    packet.seek(0)
    obj = PyPDF2.PdfFileReader(packet)
    return obj.getPage(0)
