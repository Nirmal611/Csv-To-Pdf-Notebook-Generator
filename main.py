from fpdf import FPDF
import pandas as pd

class FPDFs (FPDF):
    def __init__(self,orientation,unit,format,footer_text=''):
        super().__init__()
        self.footer_text=footer_text

    def footer(self):
        self.set_font(family='Times',style='I',size=10)
        self.set_y(-15)
        self.cell(txt=self.footer_text,w=0,h=8,ln=1,align='R',border=0)

    def add_lines(self):
        for i in range(21,290,10):
            self.line(x1=10,y1=i,x2=200,y2=i)


pdf = FPDFs(orientation='P' , unit = 'mm' , format='a4')

df = pd.read_csv('topics.csv')

for index , row in df.iterrows():
    pdf.add_page()
    pages = int(row['Pages'])
    pdf.footer_text=row['Topic']
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(txt=str(row['Order'])+')'+'\t'+row['Topic'] , w=0 , h=12 , align='L' , ln=1 , border=0)
    pdf.add_lines()

    for i in range(1,pages) :
        pdf.add_page()
        pdf.add_lines()

pdf.output('output.pdf')
