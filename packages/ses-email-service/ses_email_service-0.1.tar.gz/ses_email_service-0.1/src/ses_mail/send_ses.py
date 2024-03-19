import boto3

class SESEmailService:

    # default region set to 'eu-north-1 (Stockholm)'
    def __init__(self, access_key, secret_key, region='eu-north-1'):
        self.client = boto3.client('ses', 
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key,
                                   region_name=region)
    
    # send email to the recipient using aws SES.
    def send_email_ses(self, sender_mail, recipient_mail, subject, body):
        try:
            response = self.client.send_email(
                Source=sender_mail,
                Destination={'ToAddresses': [recipient_mail]},
                Message={
                    'Subject': {'Data': subject},
                    'Body': {'Text': {'Data': body}}
                }
            )
            print("Email sent! Message ID:", response['MessageId'])
            return True
        except Exception as e:
            print("Sending Email failed")
            return False
        

    # user needs to verify the email address before sending/ recieving email so this will verify the user.
    def Identify_user_email(self, identify_email_address):
        try:
            self.client.verify_email_identity(
                EmailAddress = identify_email_address
            )
            print(f"Verification email sent to {identify_email_address}.")
            return True
        except Exception as e:
            print(f"Failed to verify email address")
            return False




