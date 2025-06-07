"""
Travel Concierge Chatbot
A Streamlit-based travel recommendation chatbot using Claude API and MCP integration
"""

# Import handling with error messages
try:
    import streamlit as st
except ImportError:
    print("❌ Streamlit not found. Please install dependencies:")
    print("pip install -r requirements.txt")
    exit(1)

try:
    import anthropic
except ImportError:
    st.error("❌ Anthropic library not found. Please install dependencies: pip install -r requirements.txt")
    st.stop()

from datetime import datetime
import json

# Import our custom modules
try:
    from travel_data import DESTINATIONS, search_destinations, get_destinations_by_category
    from mock_mcp import demonstrate_mcp_integration, format_mcp_results
except ImportError as e:
    st.error(f"❌ Error importing custom modules: {e}")
    st.error("Please ensure all project files are in the same directory.")
    st.stop()

# Configure Streamlit page
st.set_page_config(
    page_title="Travel Concierge Chatbot",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Claude API client
ANTHROPIC_API_KEY = "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"

@st.cache_resource
def get_claude_client():
    """Initialize and cache Claude API client"""
    return anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "user_preferences" not in st.session_state:
        st.session_state.user_preferences = {}
    if "booking_state" not in st.session_state:
        st.session_state.booking_state = None
    if "conversation_context" not in st.session_state:
        st.session_state.conversation_context = ""

def create_travel_prompt(user_message, conversation_history, user_preferences):
    """Create a structured prompt for Claude API"""
    
    # Build context from available destinations
    destinations_context = ""
    for category, destinations in DESTINATIONS.items():
        destinations_context += f"\n{category.upper()} DESTINATIONS:\n"
        for dest_name, dest_info in destinations.items():
            destinations_context += f"- {dest_name}: {dest_info['description']}\n"
            destinations_context += f"  Budget: {dest_info['budget_range']}, Best time: {dest_info['best_time']}\n"
    
    prompt = f"""You are a friendly and knowledgeable travel concierge chatbot. Your role is to help users discover amazing travel destinations and activities based on their preferences.

AVAILABLE DESTINATIONS AND ACTIVITIES:
{destinations_context}

USER PREFERENCES: {json.dumps(user_preferences) if user_preferences else "Not yet collected"}

CONVERSATION HISTORY:
{conversation_history}

GUIDELINES:
1. Be conversational, friendly, and enthusiastic about travel
2. Ask clarifying questions about preferences (budget, travel style, dates, group size)
3. Recommend specific destinations from the available list based on user interests
4. Provide detailed information about activities, costs, and timing
5. If user asks for "more details" about a destination, suggest using external search
6. When user shows interest in booking, guide them through a simple confirmation process
7. Keep responses concise but informative

USER MESSAGE: {user_message}

Respond as the travel concierge chatbot:"""
    
    return prompt

def get_claude_response(prompt):
    """Get response from Claude API"""
    try:
        client = get_claude_client()
        
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.7,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.content[0].text
    
    except Exception as e:
        st.error(f"Error communicating with Claude API: {str(e)}")
        return "I apologize, but I'm having trouble connecting to my travel database right now. Please try again in a moment."

def check_for_mcp_trigger(user_message):
    """Check if user message should trigger MCP search"""
    mcp_triggers = [
        "more details", "tell me more", "current weather", "what's happening",
        "events", "safety", "travel advisory", "more information"
    ]
    
    return any(trigger in user_message.lower() for trigger in mcp_triggers)

def extract_destination_from_context(messages):
    """Extract the most recently mentioned destination from conversation"""
    recent_messages = messages[-5:]  # Look at last 5 messages
    
    all_destinations = []
    for category in DESTINATIONS.values():
        all_destinations.extend(category.keys())
    
    for message in reversed(recent_messages):
        content = message["content"].lower()
        for destination in all_destinations:
            if destination.lower() in content:
                return destination
    
    return None

def format_destination_recommendation(destination_name, destination_info, category):
    """Format destination information for display"""
    
    formatted = f"""
## 🌟 {destination_name} ({category.title()})

**{destination_info['description']}**

**📅 Best Time to Visit:** {destination_info['best_time']}
**💰 Budget Range:** {destination_info['budget_range']}
**🌤️ Climate:** {destination_info['climate']}

### 🎯 Recommended Activities:
"""
    
    for activity in destination_info['activities']:
        formatted += f"""
- **{activity['name']}** - ${activity['price']} ({activity['duration']})
  ⭐ Rating: {activity['rating']}/5.0
"""
    
    return formatted

def handle_booking_request(destination, activity=None):
    """Handle booking confirmation process"""
    
    booking_details = {
        "destination": destination,
        "activity": activity,
        "booking_id": f"TC{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "timestamp": datetime.now().isoformat(),
        "status": "confirmed"
    }
    
    st.session_state.booking_state = booking_details
    
    confirmation_message = f"""
## ✅ Booking Confirmed!

**Booking ID:** {booking_details['booking_id']}
**Destination:** {destination}
"""
    
    if activity:
        confirmation_message += f"**Activity:** {activity}\n"
    
    confirmation_message += f"""
**Booking Date:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}

🎉 **Congratulations!** Your travel experience has been confirmed. 

📧 A confirmation email has been sent to your registered email address.
📱 You'll receive SMS updates about your booking.

**Next Steps:**
- Check your email for detailed itinerary
- Download our mobile app for real-time updates
- Contact our 24/7 support if you need assistance

Have an amazing trip! ✈️🌍
"""
    
    return confirmation_message

def main():
    """Main Streamlit application"""
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.title("✈️ Travel Concierge Chatbot")
    st.markdown("*Your AI-powered travel companion for discovering amazing destinations*")
    
    # Sidebar with user preferences
    with st.sidebar:
        st.header("🎯 Travel Preferences")
        
        # Collect user preferences
        budget = st.selectbox(
            "Budget Range",
            ["Any", "$ (Budget-friendly)", "$$ (Moderate)", "$$$ (Expensive)", "$$$$ (Ultra-luxury)"]
        )
        
        travel_style = st.multiselect(
            "Travel Style",
            ["Adventure", "Culture", "Beach", "City", "Nature", "Food", "History"]
        )
        
        group_size = st.selectbox(
            "Group Size",
            ["Solo", "Couple", "Family", "Friends Group", "Large Group"]
        )
        
        travel_dates = st.date_input("Preferred Travel Dates")
        
        # Update session state with preferences
        st.session_state.user_preferences = {
            "budget": budget,
            "travel_style": travel_style,
            "group_size": group_size,
            "travel_dates": str(travel_dates)
        }
        
        # Display MCP integration status
        st.header("🔧 MCP Integration")
        st.info("Mock MCP server active\n\nReal integration would connect to Perplexity MCP for live data")
        
        # Show booking status
        if st.session_state.booking_state:
            st.header("📋 Current Booking")
            st.success(f"Booking ID: {st.session_state.booking_state['booking_id']}")
    
    # Main chat interface
    st.header("💬 Chat with Your Travel Concierge")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me about travel destinations, activities, or anything travel-related!"):
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Check if this should trigger MCP search
        if check_for_mcp_trigger(prompt):
            destination = extract_destination_from_context(st.session_state.messages)
            
            if destination:
                # Demonstrate MCP integration
                with st.chat_message("assistant"):
                    with st.spinner("🔍 Searching for current information..."):
                        
                        # This is where real MCP integration would occur
                        mcp_query = f"current information about {destination}"
                        mcp_response = demonstrate_mcp_integration(mcp_query)
                        
                        mcp_formatted = format_mcp_results(mcp_response)
                        
                        response_with_mcp = f"""Let me get you the latest information about {destination}:

{mcp_formatted}

*This information was retrieved using our MCP integration for real-time data.*

Would you like me to help you plan activities or book something for {destination}?"""
                        
                        st.markdown(response_with_mcp)
                        st.session_state.messages.append({"role": "assistant", "content": response_with_mcp})
            else:
                # General MCP search
                with st.chat_message("assistant"):
                    with st.spinner("🔍 Searching for information..."):
                        mcp_response = demonstrate_mcp_integration(prompt)
                        mcp_formatted = format_mcp_results(mcp_response)
                        
                        response = f"Here's what I found:\n\n{mcp_formatted}"
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Check for booking requests
        elif any(word in prompt.lower() for word in ["book", "reserve", "confirm", "i want to go"]):
            destination = extract_destination_from_context(st.session_state.messages)
            
            if destination:
                with st.chat_message("assistant"):
                    booking_confirmation = handle_booking_request(destination)
                    st.markdown(booking_confirmation)
                    st.session_state.messages.append({"role": "assistant", "content": booking_confirmation})
            else:
                with st.chat_message("assistant"):
                    response = "I'd be happy to help you book a trip! Could you let me know which destination you're interested in?"
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
        
        else:
            # Regular conversation with Claude
            with st.chat_message("assistant"):
                with st.spinner("🤔 Thinking about your travel needs..."):
                    
                    # Build conversation history
                    conversation_history = ""
                    for msg in st.session_state.messages[-10:]:  # Last 10 messages for context
                        conversation_history += f"{msg['role']}: {msg['content']}\n"
                    
                    # Create prompt and get Claude response
                    travel_prompt = create_travel_prompt(prompt, conversation_history, st.session_state.user_preferences)
                    response = get_claude_response(travel_prompt)
                    
                    # Check if response mentions specific destinations and format them
                    for category, destinations in DESTINATIONS.items():
                        for dest_name, dest_info in destinations.items():
                            if dest_name.lower() in response.lower() and dest_name.lower() in prompt.lower():
                                # Add formatted destination info
                                formatted_dest = format_destination_recommendation(dest_name, dest_info, category)
                                response += f"\n\n{formatted_dest}"
                                break
                    
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Welcome message for new users
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            welcome_message = """
👋 **Welcome to your Travel Concierge!**

I'm here to help you discover amazing travel destinations and plan unforgettable experiences. 

🌍 **I can help you with:**
- Finding destinations based on your preferences
- Recommending activities and experiences
- Providing current information about destinations
- Simulating booking confirmations

**To get started, try asking:**
- "I want an adventure trip"
- "Suggest a relaxing beach destination"
- "Tell me about cultural destinations"
- "What's the weather like in Dubai?"

What kind of travel experience are you looking for? ✈️
"""
            st.markdown(welcome_message)
            st.session_state.messages.append({"role": "assistant", "content": welcome_message})

if __name__ == "__main__":
    main()
