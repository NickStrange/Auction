from fpdf import fpdf
from fpdf.enums import XPos, YPos
import math

def format_page(pdf):
    TABLEX = 45
    TABLEFONT=20
    IMAGEY = 60
    BASE=50
    GAP=35
    RECTX = 6
    RECTY=170
    RECTWIDTH=580
    RECTDEPTH=170
    CHARHT=30
    pdf.add_page()
    pdf.set_margin(0)
    pdf_style = 'B'
    pdf.set_font("Arial", style=pdf_style, size=30)
    #
    # pdf.set_xy(10, 10)
    # pdf.set_text_color(0, 255, 0)
    # pdf.cell(600, 30, text='CARY GARDEN CLUB 2023', border=0, align='C', new_x=XPos.RIGHT, new_y=YPos.NEXT)
    #
    # # IMAGES
    #
    # pdf.image('../data/rose.jpg', x=15, y=IMAGEY, w=80)
    # pdf.set_text_color(0, 0, 0)
    # pdf.set_xy(10, 70)
    # pdf.cell(600, 30, text='Annual Silent Auction', border=0, align='C', new_x=XPos.RIGHT, new_y=YPos.NEXT)
    pdf.set_xy(10, 25)
    pdf.cell(600, 30, text=f'Item # ', border=0, new_x=XPos.RIGHT, align='C', new_y=YPos.NEXT)
    # pdf.image('../data/rose.jpg', x=500, y=IMAGEY, w=80)
    # pdf.set_xy(10, 130)
    # pdf_style = ''
    # pdf.set_font("Arial", style=pdf_style, size=20)
    # pdf.cell(600, 30, text=f'Donated by: {name}', border=0, new_x=XPos.RIGHT, align='C', new_y=YPos.NEXT)
    #
    # pdf_style = 'B'
    # pdf.set_font("Arial", style=pdf_style, size=30)
    # pdf.set_line_width(3)
    # pdf.set_fill_color(0, 255, 0)
    # pdf.rect(RECTX, RECTY, RECTWIDTH, RECTDEPTH)
    #
    # pdf.set_xy(0,BASE)
    # pdf.set_text_color(0, 0, 0)
    # pdf_style = 'B'
    # pdf.set_font("Arial", style=pdf_style, size=20)
    # for t in title:
    #     pdf.set_x(0)
    #     pdf.cell(0, CHARHT, text=f'{t}', border=0, align='C', new_x=XPos.RIGHT, new_y=YPos.NEXT)
    #
    # pdf_style = 'B'
    # pdf.set_font("Arial", style=pdf_style, size=30)
    # pdf.set_xy(0,BASE+GAP*len(title))
    # pdf.cell(0, CHARHT, text=f'Retail Value: ${retail_value}', border=0, align='C', new_x=XPos.RIGHT, new_y=YPos.NEXT)
    # pdf_style = 'B'
    # pdf.set_font("Arial", style=pdf_style, size=30)
    #
    # pdf.set_text_color(0, 0, 0)
    # pdf.set_xy(0, BASE+5*GAP)
    # pdf.cell(600, CHARHT, text='Auction Bids', border=0, align='C', new_x=XPos.RIGHT, new_y=YPos.NEXT)
    # pdf.set_font(style='')
    # pdf.set_xy(0, BASE+6*GAP)
    # pdf.cell(600, CHARHT, text=f'Minimum bid: ${opening_bid}', border=0, align='C', new_x=XPos.RIGHT, new_y=YPos.NEXT)
    # pdf.set_xy(0, BASE+7*GAP)
    # pdf.cell(600, CHARHT, text='Minimum bid increment: $5', border=0, new_x=XPos.RIGHT, align='C', new_y=YPos.NEXT)

    data = [['', 'Name', 'Phone Number', 'Bid']]
    for i in range(20):
        data.append([f'{i+11}', '', '', ''])

    pdf.set_font(size=TABLEFONT)
    pdf.set_xy(TABLEX, BASE+ 25)
    row_height = pdf.font_size*1.5
    spacing = 1
    widths=[50, 170, 195, 80]
    for row in data:
        for item, width in zip(row, widths):
            pdf.cell(width, row_height * spacing,
                     text=item, border=1)
        pdf.ln(row_height * spacing)
        pdf.set_x(TABLEX)

pdf = fpdf.FPDF(format='A4', unit='pt')
format_page(pdf)
pdf.output('auction_overflow.pdf')

