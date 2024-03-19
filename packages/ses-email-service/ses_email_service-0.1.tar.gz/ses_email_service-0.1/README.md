# SES Email service

A Python library for sending emails with the help of amazon service SES (simple email service).

## Installation steps

You can install SES Mailer using pip:

command- pip install ses-email-x20238813

# How to use ? 

1. Create a IAM user - add policy AmazonSESFullAccess
2. Create access key and input the key and secret access key 
    aws_access_key_id = ''
    aws_secret_access_key = ''

3. Instantiate SESEmailService object
mailService = SESMailer(aws_access_key_id, aws_secret_access_key)

4. Define the following variables-
sender_email = 'abc@gmail.com'
recipient_email = 'abcd@gmail.com'
subject = 'Email Subject'
body = 'Add the message here that you want to send'


# Note before sending the email user must be identified in you AWS, so to do so pass the email address that needs to be verified, a email will be sent to user from amazon, once user approves it then only they can send or recieve email.

5. mailService.Identify_user_email(verifiy_email)

6. Once user is verified then you can send them email using the following code-
mailService.send_email(sender_email, recipient_email, subject, body)
