#!/usr/bin/env python3
"""
Development setup script for SMS Email Gateway
This script helps you quickly set up your development environment.
"""

import os
import shutil
import subprocess
import sys

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def setup_env_file():
    """Set up .env file from template"""
    print("\n📝 Setting up .env file...")
    
    if os.path.exists('.env'):
        response = input("⚠️  .env file already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("📄 Keeping existing .env file")
            return True
    
    if os.path.exists('env_template'):
        shutil.copy('env_template', '.env')
        print("✅ .env file created from template")
        print("📝 Please edit .env file with your actual email credentials:")
        print("   - EMAIL_ADDRESS=your-email@gmail.com")
        print("   - EMAIL_PASSWORD=your-app-password")
        print()
        print("💡 For Gmail users:")
        print("   1. Enable 2-Factor Authentication")
        print("   2. Generate App Password at: https://support.google.com/accounts/answer/185833")
        print("   3. Use the App Password (not your regular Gmail password)")
        return True
    else:
        print("❌ env_template file not found")
        return False

def test_setup():
    """Test the setup"""
    print("\n🧪 Testing setup...")
    try:
        from main import SMSEmailGateway
        gateway = SMSEmailGateway()
        gateway.list_supported_carriers()
        print("✅ Setup test passed")
        return True
    except Exception as e:
        print(f"❌ Setup test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 SMS Email Gateway - Development Setup")
    print("=" * 50)
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Setup .env file
    if not setup_env_file():
        return
    
    # Test setup
    if not test_setup():
        return
    
    print("\n🎉 Development setup complete!")
    print("\nNext steps:")
    print("1. Edit .env file with your email credentials")
    print("2. Run: python main.py")
    print("3. Start building awesome SMS automation! 📱")

if __name__ == "__main__":
    main() 