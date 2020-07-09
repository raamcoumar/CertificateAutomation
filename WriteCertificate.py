def WriteCertificate(template, name, CertificateFileName, score = None):
    from PIL import Image, ImageDraw, ImageFont

    """
    Creates a certificate for the given template and exports
    in PDF. 
    Parameters:
        template (string)   : file name of the certificate's template
        name (string)       : Name to be written on the Certificate
    """

    # The Template is imported as RGBA and then it is converted to
    # RGB as Pillow can only convert RGB to PDF.
    rgba = Image.open(template) 
    certificate = Image.new('RGB', rgba.size, (255, 255, 255))
    certificate.paste(rgba, mask=rgba.split()[3]) 

    font = ImageFont.truetype(font = 'name.ttf',size = 60) # Importing Font
    draw = ImageDraw.Draw(certificate) # Draw object (like a turtle)
    draw.text((1672, 985),
               name.center(50, ' '),
               font = font, fill ="black",
               align ="left") # drawing text size 
    draw.text((1190, 1240),
               str(score),
               font = font, fill ="black",
               align ="left") # drawing text size 
    certificate.save(f'{name}{CertificateFileName}') # Exporting as PDF.   

    return f'{name}{CertificateFileName}'