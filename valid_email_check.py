def get_emails():
    emails = []
    print("Enter 5 email addresses:")
    for i in range(5):
        email = input(f"Email {i+1}: ").strip()
        emails.append(email)
    return emails

def validate_emails(email_list):
    valid_emails = []
    invalid_emails = []

    for email in email_list:
        if "@" in email and not email.startswith("@") and not email.endswith("@"):
            if email.endswith(".com") or email.endswith(".cy") or email.endswith(".gr"):
                valid_emails.append(email)
            else:
                invalid_emails.append(email)
        else:
            invalid_emails.append(email)

    print("\nValid Emails:")
    for v in valid_emails:
        print("✔", v)

    print("\nInvalid Emails:")
    for i in invalid_emails:
        print("✖", i)

    with open("valid.emails.txt", "w") as file:
        for v in valid_emails:
            file.write(v + "\n")
    print("\nValid emails saved to 'valid.emails.txt'")

emails = get_emails()
validate_emails(emails)
