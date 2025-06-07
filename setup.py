"""
Setup script for Travel Concierge Chatbot
Helps with installation and dependency management
"""

import subprocess
import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    try:
        # Try different pip commands
        commands = [
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            ["pip", "install", "-r", "requirements.txt"],
            ["py", "-m", "pip", "install", "-r", "requirements.txt"]
        ]
        
        for cmd in commands:
            try:
                result = subprocess.run(cmd, check=True, capture_output=True, text=True)
                print("✅ Dependencies installed successfully!")
                return True
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        
        print("❌ Failed to install dependencies")
        print("Please try manually:")
        print("pip install -r requirements.txt")
        return False
        
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_files():
    """Check if all required files are present"""
    required_files = [
        "app.py",
        "travel_data.py", 
        "mock_mcp.py",
        "requirements.txt",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def test_imports():
    """Test if all imports work correctly"""
    print("🧪 Testing imports...")
    
    try:
        import streamlit
        print("✅ Streamlit imported successfully")
    except ImportError:
        print("❌ Streamlit import failed")
        return False
    
    try:
        import anthropic
        print("✅ Anthropic imported successfully")
    except ImportError:
        print("❌ Anthropic import failed")
        return False
    
    try:
        from travel_data import DESTINATIONS
        print("✅ Travel data imported successfully")
    except ImportError:
        print("❌ Travel data import failed")
        return False
    
    try:
        from mock_mcp import demonstrate_mcp_integration
        print("✅ Mock MCP imported successfully")
    except ImportError:
        print("❌ Mock MCP import failed")
        return False
    
    return True

def run_application():
    """Launch the Streamlit application"""
    print("🚀 Launching Travel Concierge Chatbot...")
    
    commands = [
        [sys.executable, "-m", "streamlit", "run", "app.py"],
        ["streamlit", "run", "app.py"],
        ["py", "-m", "streamlit", "run", "app.py"]
    ]
    
    for cmd in commands:
        try:
            subprocess.run(cmd, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    
    print("❌ Failed to launch application")
    print("Please try manually:")
    print("streamlit run app.py")
    return False

def main():
    """Main setup function"""
    print("🎯 Travel Concierge Chatbot Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check required files
    if not check_files():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Test imports
    if not test_imports():
        print("\n💡 Try installing dependencies manually:")
        print("pip install -r requirements.txt")
        return
    
    print("\n✅ Setup completed successfully!")
    print("\n🚀 Ready to launch the application!")
    
    # Ask user if they want to launch
    try:
        launch = input("\nWould you like to launch the application now? (y/n): ").lower().strip()
        if launch in ['y', 'yes']:
            run_application()
        else:
            print("\nTo launch later, run:")
            print("streamlit run app.py")
    except KeyboardInterrupt:
        print("\n\nSetup completed. To launch later, run:")
        print("streamlit run app.py")

if __name__ == "__main__":
    main()
