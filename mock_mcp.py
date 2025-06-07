"""
Mock MCP (Model Context Protocol) Integration
Simulates Perplexity MCP search tool with realistic travel data responses
"""

import json
import random
from datetime import datetime

class MockPerplexityMCP:
    """
    Mock implementation of Perplexity MCP server
    In production, this would connect to actual MCP server endpoints
    """
    
    def __init__(self):
        self.server_name = "perplexity-mcp"
        self.available_tools = ["search"]
        
        # Mock data for realistic search responses
        self.mock_data = {
            "weather": {
                "Dubai": "Dubai: 35°C, sunny, low humidity. Perfect weather for outdoor activities and desert adventures.",
                "AlUla": "AlUla: 28°C, clear skies, perfect for outdoor activities. Ideal conditions for rock climbing and stargazing.",
                "Kyoto": "Kyoto: 15°C, partly cloudy, cherry blossom season approaching. Beautiful weather for temple visits.",
                "Rome": "Rome: 22°C, mild and pleasant. Excellent weather for walking tours and outdoor dining.",
                "Istanbul": "Istanbul: 18°C, partly cloudy with mild winds. Great weather for exploring historic sites.",
                "Maldives": "Maldives: 30°C, tropical paradise with gentle ocean breeze. Perfect for water activities.",
                "Bali": "Bali: 29°C, tropical warmth with occasional refreshing showers. Ideal for beach and cultural activities.",
                "Santorini": "Santorini: 24°C, clear Mediterranean skies. Perfect sunset viewing conditions.",
                "Singapore": "Singapore: 32°C, hot and humid with afternoon thunderstorms. Indoor attractions recommended during midday.",
                "Barcelona": "Barcelona: 26°C, pleasant Mediterranean climate. Perfect for outdoor exploration and beach visits.",
                "Tokyo": "Tokyo: 20°C, mild spring weather with cherry blossoms in bloom. Excellent for city exploration.",
                "New Zealand": "New Zealand: 25°C, crisp and clear with stunning visibility. Perfect conditions for adventure activities."
            },
            "travel_advisories": {
                "Dubai": "Dubai: No restrictions, safe for tourists. Excellent infrastructure and tourist-friendly policies.",
                "AlUla": "AlUla: Recommended destination with new tourist infrastructure. Saudi Vision 2030 has made it very accessible.",
                "Kyoto": "Kyoto: No restrictions, very safe for international visitors. Well-developed tourist infrastructure.",
                "Rome": "Rome: Safe for tourists, standard European travel precautions recommended. Excellent public transportation.",
                "Istanbul": "Istanbul: Generally safe for tourists, vibrant and welcoming to international visitors.",
                "Maldives": "Maldives: No restrictions, luxury resort destination with excellent safety standards.",
                "Bali": "Bali: Popular tourist destination, check seasonal weather patterns. Generally very safe and welcoming.",
                "Santorini": "Santorini: No restrictions, popular European destination with excellent tourist facilities.",
                "Singapore": "Singapore: Extremely safe, well-regulated destination with world-class infrastructure.",
                "Barcelona": "Barcelona: Safe European destination, standard precautions for pickpocketing in tourist areas.",
                "Tokyo": "Tokyo: Extremely safe, excellent public transportation and tourist-friendly infrastructure.",
                "New Zealand": "New Zealand: Very safe destination with excellent adventure tourism infrastructure and safety standards."
            },
            "local_events": {
                "Dubai": "Dubai: Shopping Festival (Jan-Feb), Food Festival (Mar), Dubai Summer Surprises (Jul-Aug)",
                "AlUla": "AlUla: Winter at Tantora Festival (Dec-Mar), featuring music, arts, and cultural experiences",
                "Kyoto": "Kyoto: Cherry Blossom Festival (Apr), Gion Matsuri Festival (Jul), Autumn Colors Festival (Nov)",
                "Rome": "Rome: Rome Marathon (Mar), Estate Romana Summer Festival (Jun-Sep), White Night cultural events",
                "Istanbul": "Istanbul: Istanbul Music Festival (Jun), Biennale art exhibitions, Ramadan cultural events",
                "Maldives": "Maldives: Surfing season (Mar-Oct), Whale shark season (May-Nov), Cultural festivals year-round",
                "Bali": "Bali: Nyepi Silent Day (Mar), Galungan Festival (varies), Arts Festival (Jun-Jul)",
                "Santorini": "Santorini: Wine harvest festival (Aug), Jazz Festival (Jul), Cultural summer events",
                "Singapore": "Singapore: Chinese New Year (Jan-Feb), Food Festival (Jul), Formula 1 Grand Prix (Sep)",
                "Barcelona": "Barcelona: La Mercè Festival (Sep), Primavera Sound (May), Sant Joan Festival (Jun)",
                "Tokyo": "Tokyo: Cherry Blossom Festival (Mar-Apr), Summer Festivals (Jul-Aug), Autumn Illuminations (Nov-Dec)",
                "New Zealand": "New Zealand: Summer festivals (Dec-Feb), Adventure racing events, Wine harvest festivals (Mar-Apr)"
            }
        }
    
    def search(self, query: str) -> dict:
        """
        Mock implementation of Perplexity search tool
        
        In production, this would make actual API calls to:
        - use_mcp_tool(server_name="perplexity-mcp", tool_name="search", arguments={"query": query})
        """
        
        # Simulate API call delay and processing
        search_type = self._determine_search_type(query)
        destination = self._extract_destination(query)
        
        response = {
            "tool": "search",
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "results": []
        }
        
        if destination:
            if search_type == "weather":
                response["results"].append({
                    "type": "weather",
                    "content": self.mock_data["weather"].get(destination, f"{destination}: Weather information not available"),
                    "source": "Weather API"
                })
            
            elif search_type == "travel_advisory":
                response["results"].append({
                    "type": "travel_advisory",
                    "content": self.mock_data["travel_advisories"].get(destination, f"{destination}: No travel advisories found"),
                    "source": "Travel Advisory Database"
                })
            
            elif search_type == "events":
                response["results"].append({
                    "type": "local_events",
                    "content": self.mock_data["local_events"].get(destination, f"{destination}: No current events found"),
                    "source": "Local Events Database"
                })
            
            else:
                # General search - return multiple types of information
                response["results"] = [
                    {
                        "type": "weather",
                        "content": self.mock_data["weather"].get(destination, f"{destination}: Weather information not available"),
                        "source": "Weather API"
                    },
                    {
                        "type": "travel_advisory",
                        "content": self.mock_data["travel_advisories"].get(destination, f"{destination}: No travel advisories found"),
                        "source": "Travel Advisory Database"
                    },
                    {
                        "type": "local_events",
                        "content": self.mock_data["local_events"].get(destination, f"{destination}: No current events found"),
                        "source": "Local Events Database"
                    }
                ]
        else:
            response["results"].append({
                "type": "general",
                "content": f"Search results for '{query}': This is where real MCP search results would appear with current information from external sources.",
                "source": "General Search"
            })
        
        return response
    
    def _determine_search_type(self, query: str) -> str:
        """Determine what type of search based on query keywords"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ["weather", "temperature", "climate", "forecast"]):
            return "weather"
        elif any(word in query_lower for word in ["safety", "advisory", "travel warning", "restrictions"]):
            return "travel_advisory"
        elif any(word in query_lower for word in ["events", "festival", "happening", "activities", "what's on"]):
            return "events"
        else:
            return "general"
    
    def _extract_destination(self, query: str) -> str:
        """Extract destination name from query"""
        destinations = list(self.mock_data["weather"].keys())
        query_lower = query.lower()
        
        for destination in destinations:
            if destination.lower() in query_lower:
                return destination
        
        return None
    
    def get_available_tools(self) -> list:
        """Return list of available MCP tools"""
        return self.available_tools
    
    def get_tool_schema(self, tool_name: str) -> dict:
        """Return schema for a specific tool"""
        if tool_name == "search":
            return {
                "name": "search",
                "description": "Search for current information about travel destinations",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query for travel-related information"
                        }
                    },
                    "required": ["query"]
                }
            }
        return {}

# Global instance for use in the main application
# In production, this would be replaced with actual MCP client initialization
mock_mcp_client = MockPerplexityMCP()

def demonstrate_mcp_integration(query: str) -> dict:
    """
    Demonstrate MCP integration with mock data
    
    This function shows exactly where real MCP integration would occur.
    In production, replace this with:
    
    from mcp_client import MCPClient
    client = MCPClient("perplexity-mcp")
    result = client.use_tool("search", {"query": query})
    """
    
    print(f"🔍 MCP Search Query: {query}")
    result = mock_mcp_client.search(query)
    print(f"📊 MCP Response: {len(result['results'])} results found")
    
    return result

def format_mcp_results(mcp_response: dict) -> str:
    """Format MCP search results for display in chat"""
    if not mcp_response.get("results"):
        return "No additional information found."
    
    formatted_results = []
    for result in mcp_response["results"]:
        formatted_results.append(f"**{result['type'].title()}**: {result['content']}")
    
    return "\n\n".join(formatted_results)
