def handler_info():

    destination = input("Insert the destination email: ").strip()
    subject = input("Insert the subject email: ").strip()
    message = input ("Insert the message: ").strip()

    info = {
        'destination': destination,
        'subject': subject,
        'message': message
    }
    
    return info   

def create_email(info):

    email = {
        'to': info['destination'],
        'subject': info['subject'],
        'message': info['message']
    }

    return email