# Coleta os dados do usuário via terminal
def get_user_input():
    destination = input("Insert the destination email: ").strip()
    subject = input("Insert the subject email: ").strip()
    message = input("Insert the message: ").strip()

    info = {
        'to': destination,
        'subject': subject,
        'message': message
    }
    
    return info   


# Valida os dados informados pelo usuário
def validate_info(info):
    
    email = info['to']

    # Verifica formato básico de email
    email_ok = (
        "@" in email and 
        "." in email and 
        email.index("@") < email.rindex(".")
    )

    # Verifica se subject e message não estão vazios
    subject_ok = bool(info['subject'])
    message_ok = bool(info['message'])

    return email_ok and subject_ok and message_ok


# Monta o objeto de email após validação
def build_email(info):
    
    # Se não passar na validação, retorna None
    if not validate_info(info):
        return None
            
    email = {
        'to': info['to'],
        'subject': info['subject'],
        'message': info['message']
    }

    return email
# Simula envio do email (apenas print no terminal)
def send_email(email):
    print("\n=== Sending Email ===")
    print(f"To: {email['to']}")
    print(f"Subject: {email['subject']}")
    print(f"Message: {email['message']}")
    print("Email sent successfully.")


# Loop principal até dados válidos
while True:

    info = get_user_input()
    email = build_email(info)

    if email:
        send_email(email)
        break
    else:
        print("Invalid data, try again.\n")