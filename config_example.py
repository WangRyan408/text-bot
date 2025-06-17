#!/usr/bin/env python3
"""
Example configuration and usage of the SMS Email Gateway

This file demonstrates different ways to use the SMS gateway system.
"""

from main import SMSEmailGateway

# Example 1: Basic usage with interactive credentials
def basic_example():
    """Basic example with interactive credential input"""
    gateway = SMSEmailGateway()
    
    # Interactive setup (will prompt for email and password)
    gateway.setup_credentials()
    
    # Send a single SMS
    success = gateway.send_sms(
        phone_number="1234567890",
        carrier="verizon",
        message="Hello from Python!",
        subject="Test Message"
    )
    
    if success:
        print("Message sent successfully!")
    else:
        print("Failed to send message")
    
    gateway.disconnect_smtp()

# Example 2: Using .env file (recommended for development)
def env_example():
    """Example using .env file for credentials"""
    
    # Create .env file with:
    # EMAIL_ADDRESS=your-email@gmail.com
    # EMAIL_PASSWORD=your-app-password
    
    gateway = SMSEmailGateway()
    
    try:
        # Credentials are automatically loaded from .env file
        gateway.load_credentials_from_env()
        
        # Send SMS
        gateway.send_sms("1234567890", "tmobile", "Automated message!")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Make sure .env file exists with EMAIL_ADDRESS and EMAIL_PASSWORD")
    finally:
        gateway.disconnect_smtp()

# Example 3: Bulk SMS sending
def bulk_example():
    """Example of sending bulk SMS messages"""
    gateway = SMSEmailGateway()
    gateway.setup_credentials()
    
    # List of recipients
    recipients = [
        {'phone': '1234567890', 'carrier': 'verizon'},
        {'phone': '0987654321', 'carrier': 'att'},
        {'phone': '5555551234', 'carrier': 'tmobile'},
    ]
    
    # Send to all recipients
    results = gateway.send_bulk_sms(
        recipients=recipients,
        message="Bulk notification: System maintenance tonight at 10 PM",
        subject="Maintenance Alert"
    )
    
    print(f"Bulk SMS Results:")
    print(f"  Successfully sent: {results['total_sent']}")
    print(f"  Failed: {results['total_failed']}")
    
    gateway.disconnect_smtp()

# Example 4: Using with different email providers
def custom_smtp_example():
    """Example using different SMTP providers"""
    
    # Gmail (default)
    gmail_gateway = SMSEmailGateway("smtp.gmail.com", 587)
    
    # Outlook/Hotmail
    outlook_gateway = SMSEmailGateway("smtp-mail.outlook.com", 587)
    
    # Yahoo
    yahoo_gateway = SMSEmailGateway("smtp.mail.yahoo.com", 587)
    
    # Use any of them the same way
    gateway = gmail_gateway  # Choose your provider
    gateway.setup_credentials()
    gateway.send_sms("1234567890", "verizon", "Test from custom SMTP")
    gateway.disconnect_smtp()

if __name__ == "__main__":
    print("SMS Email Gateway Examples")
    print("=" * 40)
    
    # Uncomment the example you want to run:
    
    # basic_example()
    # env_example()
    # bulk_example()
    # custom_smtp_example()
    
    # Show supported carriers
    gateway = SMSEmailGateway()
    gateway.list_supported_carriers() 