from PIL import Image, ImageDraw, ImageFont
import textwrap
    
class Certificate:
    """
    Create a Certificate image/pdf
    """
    def __init__ (self, template):
        self.template = Image.open(template) 
        
    def size(self):
        width, height = self.template.size
        return (width, height)
        
    def add_text(self, Y, text, color, size, font):
        Font = ImageFont.truetype(font = font, size = size) # Importing Font
        write = ImageDraw.Draw(self.template) # Draw object (like a turtle)
        text_width, _ = write.textsize(text, font = Font)
        write.text(
            ((self.template.width - text_width)/2,Y),
            text,
            font = Font,
            fill = color,
            align = 'center')
        
    def add_para(self, Y, text, color, size, font):
        Font = ImageFont.truetype(font = font, size = size) # Importing Font
        write = ImageDraw.Draw(self.template) # Draw object (like a turtle)
        wrapped_text = textwrap.wrap(text, width = 90)
        
        for line in wrapped_text:
            line_width, _ = write.textsize(line, font = Font)
            write.text(
                ((self.template.width - line_width)/2, Y),
                line,
                font=Font,
                fill=color,
                align = 'center')
            Y += 105
        
    def show(self):
        self.template.show()
        
    def save(self, filename, fileformat):
        self.template.save(f'files/{filename}{fileformat}')