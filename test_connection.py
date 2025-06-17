#!/usr/bin/env python3
"""
SMTP Connection Test Script
This script helps diagnose SMTP connection issues step by step.
"""

import os
from main import SMSEmailGateway

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️  python-dotenv not available, using environment variables only")

def test_env_variables():
    """Test if environment variables are set correctly"""
    print("🔍 Testing Environment Variables:")
    
    email = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')
    
    print(f"   EMAIL_ADDRESS: {'✅ Set' if email else '❌ Not set'}")
    if email:
        print(f"   Value: {email}")
    
    print(f"   EMAIL_PASSWORD: {'✅ Set' if password else '❌ Not set'}")
    if password:
        print(f"   Length: {len(password)} characters")
        print(f"   Starts with: {password[:4]}...")
    
    print()
    return bool(email and password)

def test_smtp_connection():
    """Test SMTP connection step by step"""
    print("🧪 Testing SMTP Connection:")
    
    # Create gateway
    gateway = SMSEmailGateway()
    
    # Try to load credentials
    try:
        gateway.load_credentials_from_env()
        print("✅ Credentials loaded successfully")
    except ValueError as e:
        print(f"❌ Failed to load credentials: {e}")
        return False
    
    # Show debug info
    gateway.debug_credentials()
    
    # Test connection
    print("🔄 Testing SMTP connection...")
    success = gateway.connect_smtp()
    
    if success:
        print("🎉 Connection test PASSED!")
        gateway.disconnect_smtp()
        return True
    else:
        print("💥 Connection test FAILED!")
        return False

def diagnose_gmail_setup():
    """Provide Gmail-specific diagnostics"""
    print("🔧 Gmail Setup Checklist:")
    print("   □ 2-Factor Authentication enabled?")
    print("   □ App Password generated (not your regular password)?")
    print("   □ App Password is 16 characters long?")
    print("   □ No spaces in the App Password?")
    print("   □ Using correct Gmail address?")
    print()
    print("📋 To generate an App Password:")
    print("   1. Go to https://myaccount.google.com/security")
    print("   2. Enable 2-Factor Authentication if not already enabled")
    print("   3. Go to https://myaccount.google.com/apppasswords")
    print("   4. Select 'Mail' and 'Other (Custom name)'")
    print("   5. Name it 'Python SMS Gateway'")
    print("   6. Copy the 16-digit password")
    print("   7. Use this password in your .env file")
    print()

def main():
    print("🚀 SMTP Connection Diagnostic Tool")
    print("=" * 40)
    
    # Test 1: Environment variables
    env_ok = test_env_variables()
    
    if not env_ok:
        print("❌ Environment variables not set correctly.")
        print("📝 Create/edit .env file with:")
        print("   EMAIL_ADDRESS=your-email@gmail.com")
        print("   EMAIL_PASSWORD=your-app-password")
        return
    
    # Test 2: SMTP connection
    smtp_ok = test_smtp_connection()
    
    if not smtp_ok:
        print("\n" + "="*40)
        diagnose_gmail_setup()
    else:
        print("\n✅ All tests passed! Your SMTP setup is working correctly.")

if __name__ == "__main__":
    main() 