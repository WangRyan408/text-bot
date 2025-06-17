# SMS Email Gateway

A Python tool to send SMS messages through email-to-SMS gateways using SMTP authentication.

## Features

- ✅ Send SMS via email gateways for major carriers
- ✅ Secure SMTP authentication with TLS encryption
- ✅ Support for 12+ mobile carriers
- ✅ Bulk SMS sending capabilities
- ✅ Environment variable support for automation
- ✅ Multiple email provider support (Gmail, Outlook, Yahoo)
- ✅ Comprehensive error handling

## Supported Carriers

| Carrier | Gateway |
|---------|---------|
| Verizon | @vtext.com |
| AT&T | @txt.att.net |
| T-Mobile | @tmomail.net |
| Sprint | @messaging.sprintpcs.com |
| Boost Mobile | @sms.myboostmobile.com |
| Cricket | @sms.cricketwireless.net |
| US Cellular | @email.uscc.net |
| Virgin Mobile | @vmobl.com |
| MetroPCS | @mymetropcs.com |
| TracFone | @mmst5.tracfone.com |
| Straight Talk | @vtext.com |
| Google Fi | @msg.fi.google.com |

## Quick Start

### 1. One-time Development Setup

```bash
# Run the setup script (installs dependencies and creates .env file)
python setup_dev.py
```

Then edit the `.env` file with your actual email credentials:
```env
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

### 2. Start Sending SMS!

```bash
python main.py  # Interactive demo
```

Or use in your code:
```python
from main import SMSEmailGateway

gateway = SMSEmailGateway()
# Credentials automatically loaded from .env file

success = gateway.send_sms("1234567890", "verizon", "Hello from Python!")
if success:
    print("SMS sent successfully!")
```

## Email Provider Setup

### Gmail Setup (Recommended)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Select "Mail" and generate password
   - Use this App Password instead of your regular Gmail password

3. **Use the App Password** when prompted for your email password

### Other Email Providers

The system supports other SMTP providers:

```python
# Outlook/Hotmail
gateway = SMSEmailGateway("smtp-mail.outlook.com", 587)

# Yahoo Mail
gateway = SMSEmailGateway("smtp.mail.yahoo.com", 587)
```

## Development Setup with .env File (Recommended)

For development, create a `.env` file in your project directory:

```bash
# Copy the template and edit with your credentials
cp env_template .env
```

Edit `.env` file:
```env
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

The system will automatically load these credentials when you run the script:

```bash
python main.py  # Automatically uses .env file
```

Or in your code:
```python
gateway = SMSEmailGateway()
# Credentials are automatically loaded from .env file
gateway.send_sms("1234567890", "tmobile", "Automated message!")
```

## Environment Variables (Alternative)

You can also use traditional environment variables:

```bash
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
```

## Bulk SMS Example

```python
recipients = [
    {'phone': '1234567890', 'carrier': 'verizon'},
    {'phone': '0987654321', 'carrier': 'att'},
    {'phone': '5555551234', 'carrier': 'tmobile'},
]

results = gateway.send_bulk_sms(
    recipients=recipients,
    message="System maintenance tonight at 10 PM",
    subject="Maintenance Alert"
)

print(f"Sent: {results['total_sent']}, Failed: {results['total_failed']}")
```

## Security Best Practices

1. **Use App Passwords**: Never use your main email password
2. **Environment Variables**: Store credentials in environment variables, not in code
3. **TLS Encryption**: The system automatically uses TLS encryption
4. **Limited Permissions**: Use dedicated email accounts for automation

## Troubleshooting

### Authentication Errors

If you get SMTP authentication errors:

1. **For Gmail**: Make sure you're using an App Password, not your regular password
2. **Check 2FA**: Ensure 2-factor authentication is enabled
3. **Less Secure Apps**: Some providers may require enabling "less secure app access"

### SMS Not Received

1. **Check Carrier**: Verify the recipient's carrier is correct
2. **Message Length**: Keep messages under 160 characters
3. **Rate Limiting**: Some carriers may have rate limits
4. **Network Issues**: Check if the carrier's SMS gateway is operational

### Common Issues

```python
# Issue: "Credentials not set"
# Solution: Call setup_credentials() or load_credentials_from_env() first

gateway = SMSEmailGateway()
gateway.setup_credentials()  # Add this line

# Issue: "Unsupported carrier"
# Solution: Check supported carriers list
gateway.list_supported_carriers()
```

## API Reference

### SMSEmailGateway Class

#### Methods

- `setup_credentials(email, password)` - Set SMTP credentials
- `load_credentials_from_env()` - Load credentials from environment variables
- `connect_smtp()` - Establish SMTP connection
- `send_sms(phone, carrier, message, subject)` - Send single SMS
- `send_bulk_sms(recipients, message, subject)` - Send bulk SMS
- `list_supported_carriers()` - Display supported carriers
- `disconnect_smtp()` - Close SMTP connection

#### Parameters

- `phone_number`: 10-digit phone number (e.g., "1234567890")
- `carrier`: Carrier name (e.g., "verizon", "att", "tmobile")
- `message`: SMS text (keep under 160 characters)
- `subject`: Optional email subject line

## Examples

See `config_example.py` for more detailed usage examples.

## Requirements

- Python 3.6+
- python-dotenv (for .env file support)

Install dependencies:
```bash
pip install -r requirements.txt
```

## License

This project is open source. Use responsibly and respect carrier terms of service. 