def WebinarText(name, event):
    body = f"""
        <!DOCTYPE html>
            <head>
                <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300&family=Kite+One&family=Philosopher:wght@700&display=swap" rel="stylesheet">
            </head>
            <body style="width: 100%;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border: 1px snow; height: 100%; margin: 0 auto; padding: 10px 10px 10px 10px; width: 600px;">
                <tbody align="center">
                    <tr>
                        <td colspan = "3">
                            <img
                                src='https://christcet.edu.in/view/client/images/logo.png'
                                alt='Christ College of Engineering and Technology'
                                style='display: block; max-width: 100%; height: auto; padding: 40px 0px 5px 0px;''>
                        </td>
                    </tr>
                    <tr>
                        <td
                        colspan = "3"
                        style="font-size: 18px;">
                        <b>(Approved by AICTE, New Delhi  and Affiliated to Pondicherry University)</b>
                        </td>
                    </tr>
                    <tr>
                        <td
                        colspan = "3">
                        <h1 style="padding: 20px 0px 20px 30px; color:#505264; font-family: Arial, sans-serif; line-height: 20px; text-align: left;">
                        <b>Hi {name}!</b></h1>
                        </td>
                    </tr>
                    <tr>
                        <td
                        colspan = "3"
                        style="padding: 0px 0px 20px 30px; color:#505264; font-family: Arial, sans-serif; line-height: 20px; text-align: left;">
                        Greetings from <b>Christ College of Engineering and Technology</b>.
                        We would like to extend our heartfelt thanks for attending the Webinar on "{event}".
                        Kindly find your E-Certificate in the attachment.<br/><br/>

                        With regards,<br/>
                        The Principal,<br/>
                        Christ College of Engineering and Technology.<br/>
                        </td>
                    </tr>
                    <tr style="background-color: #505061; color: #ffffff; font-family: 'Heebo', sans-serif; font-size: 14px; text-align: left;">
                        <td style="padding: 30px;"
                            width="75%">
                            &reg; Christ College of Engineering and Technology,<br/>
                            Pitchaveeranpet, Moolakulam, Pondicherry, India - 605010  
                        </td>
                        <td>
                            <a href="https://instagram.com/ccetinsta">
                                <img
                                style="display: block;"    
                                width="38"
                                height="38"
                                src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png"
                                alt="Insagram"/>
                            </a>
                        </td>
                        <td>
                            <a href="https://www.facebook.com/christcet.edu.in">
                            <img
                                style="display: block;"
                                width="38"
                                height="38"
                                src="https://facebookbrand.com/wp-content/uploads/2019/04/f_logo_RGB-Hex-Blue_512.png"
                                alt="Facebook"/>
                            </a>
                        </td>
                    </tr>
                </tbody>
                </table>
            </body>
        </html>
    """

    return body

def OnlineQuizText(name, event):
    body = f"""
            <!DOCTYPE html>
            <head>
                <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300&family=Kite+One&family=Philosopher:wght@700&display=swap" rel="stylesheet">
            </head>
            <body style="width: 100%;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border: 1px snow; height: 100%; margin: 0 auto; padding: 10px 10px 10px 10px; width: 600px;">
                <tbody align="center">
                    <tr>
                        <td colspan = "3">
                            <img
                                src='https://christcet.edu.in/view/client/images/logo.png'
                                alt='Christ College of Engineering and Technology'
                                style='display: block; max-width: 100%; height: auto; padding: 40px 0px 5px 0px;''>
                        </td>
                    </tr>
                    <tr>
                        <td
                        colspan = "3"
                        style="font-size: 18px;">
                        <b>(Approved by AICTE, New Delhi  and Affiliated to Pondicherry University)</b>
                        </td>
                    </tr>
                    <tr>
                        <td
                            colspan = "3"
                            style="font-size: 30px; padding-top: 10px; color: red;">
                            <b>Department of Management Studies</b>
                        </td>
                    </tr>
                    <tr>
                        <td colspan = "3" style="font-size: 20px; font-family: 'Heebo', sans-serif; padding: 0px 0px 5px 0px;">
                            presents
                        </td>
                    </tr>
                    <tr>
                        <td
                            colspan = "3"
                            style="border-radius: 15px; background-color: red; color: yellow; padding: 10px; height: auto; font-size: 25px; font-family: 'Philosopher', sans-serif;">
                            Online Quiz on {event}
                        </td>
                    </tr>
                    <tr>
                        <td
                        colspan = "3">
                        <h1 style="padding: 20px 0px 20px 30px; color:#505264; font-family: Arial, sans-serif; line-height: 20px; text-align: left;">
                        <b>Hi {name}!</b></h1>
                        </td>
                    </tr>
                    <tr>
                        <td
                            colspan = "3"
                            style="padding: 0px 0px 20px 30px; color:#505264; font-family: Arial, sans-serif; line-height: 20px; text-align: left;">
                            Greetings from <b>Christ College of Engineering and Technology</b>.
                            We would like to extend our heartfelt thanks for participating in the Online Quiz on "{event}".
                            Kindly find your E-Certificate in the attachment.<br/><br/>

                            With regards,<br/>
                            The Principal,<br/>
                            Christ College of Engineering and Technology.<br/>
                        </td>
                    </tr>
                    <tr style="background-color: #505061; color: #ffffff; font-family: 'Heebo', sans-serif; font-size: 14px; text-align: left;">
                        <td style="padding: 30px;"
                            width="75%">
                            &reg; Christ College of Engineering and Technology,<br/>
                            Pitchaveeranpet, Moolakulam, Pondicherry, India - 605010  
                        </td>
                        <td>
                            <a href="https://instagram.com/ccetinsta">
                                <img
                                style="display: block;"    
                                width="38"
                                height="38"
                                src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png"
                                alt="Insagram"/>
                            </a>
                        </td>
                        <td>
                            <a href="https://www.facebook.com/christcet.edu.in">
                            <img
                                style="display: block;"
                                width="38"
                                height="38"
                                src="https://facebookbrand.com/wp-content/uploads/2019/04/f_logo_RGB-Hex-Blue_512.png"
                                alt="Facebook"/>
                            </a>
                        </td>
                </tr>
            </tbody>
            </table>
        </body>
        </html>
        """

    return body




def Email(sender_email, receiver_email, Subject, Body, Attachment):
    from email import encoders
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart

    # Setting Headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = Subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Setting Body of the Mail
    # message.attach(MIMEText(Body, 'text')) # -> For plain text emails
    message.attach(MIMEText(Body, 'html')) # -> For HTML Content

    # Attaching a file
    with open(Attachment, 'rb') as File:
        payload = MIMEBase('application', 'octet-stream')
        payload.set_payload(File.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(payload)

    # Add header as key/value pair to attachment part
    payload.add_header(
        'Content-Disposition',
        f'attachment; filename = {Attachment}',
    )

    # Add attachment to message and convert message to string
    message.attach(payload)

    return message.as_string()