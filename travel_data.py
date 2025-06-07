"""
Synthetic Travel Data for Travel Concierge Chatbot
Contains destinations, activities, and pricing information
"""

DESTINATIONS = {
    "adventure": {
        "Dubai": {
            "description": "A modern desert metropolis offering thrilling adventures",
            "activities": [
                {"name": "Desert Safari", "price": 150, "duration": "6 hours", "rating": 4.8},
                {"name": "Dune Bashing", "price": 120, "duration": "4 hours", "rating": 4.7},
                {"name": "Skydiving", "price": 600, "duration": "3 hours", "rating": 4.9},
                {"name": "Hot Air Balloon", "price": 300, "duration": "4 hours", "rating": 4.6}
            ],
            "best_time": "November to March",
            "budget_range": "$$$ (Luxury)",
            "climate": "Desert, hot and dry"
        },
        "AlUla": {
            "description": "Saudi Arabia's ancient wonder with stunning rock formations",
            "activities": [
                {"name": "Rock Climbing", "price": 200, "duration": "5 hours", "rating": 4.7},
                {"name": "Hiking Trails", "price": 80, "duration": "3 hours", "rating": 4.8},
                {"name": "Stargazing Tours", "price": 150, "duration": "4 hours", "rating": 4.9},
                {"name": "Archaeological Tours", "price": 120, "duration": "6 hours", "rating": 4.6}
            ],
            "best_time": "October to April",
            "budget_range": "$$ (Moderate)",
            "climate": "Desert, mild winters"
        },
        "New Zealand": {
            "description": "Adventure capital with breathtaking landscapes",
            "activities": [
                {"name": "Bungee Jumping", "price": 250, "duration": "2 hours", "rating": 4.9},
                {"name": "Glacier Hiking", "price": 180, "duration": "8 hours", "rating": 4.8},
                {"name": "Skydiving", "price": 400, "duration": "3 hours", "rating": 4.9},
                {"name": "White Water Rafting", "price": 160, "duration": "5 hours", "rating": 4.7}
            ],
            "best_time": "December to February",
            "budget_range": "$$$ (Expensive)",
            "climate": "Temperate, varied"
        }
    },
    "culture": {
        "Kyoto": {
            "description": "Ancient capital with temples, gardens, and traditional culture",
            "activities": [
                {"name": "Temple Visits", "price": 50, "duration": "4 hours", "rating": 4.8},
                {"name": "Tea Ceremony", "price": 80, "duration": "2 hours", "rating": 4.7},
                {"name": "Traditional Crafts Workshop", "price": 120, "duration": "3 hours", "rating": 4.6},
                {"name": "Bamboo Forest Walk", "price": 30, "duration": "2 hours", "rating": 4.9}
            ],
            "best_time": "April and November",
            "budget_range": "$$ (Moderate)",
            "climate": "Temperate, four seasons"
        },
        "Rome": {
            "description": "Eternal city with ancient history and incredible architecture",
            "activities": [
                {"name": "Colosseum Tour", "price": 60, "duration": "3 hours", "rating": 4.8},
                {"name": "Vatican Museums", "price": 70, "duration": "4 hours", "rating": 4.9},
                {"name": "Cooking Classes", "price": 150, "duration": "4 hours", "rating": 4.7},
                {"name": "Roman Forum Walk", "price": 40, "duration": "2 hours", "rating": 4.6}
            ],
            "best_time": "April to June, September to October",
            "budget_range": "$$ (Moderate)",
            "climate": "Mediterranean"
        },
        "Istanbul": {
            "description": "Where East meets West with rich Ottoman heritage",
            "activities": [
                {"name": "Historic Sites Tour", "price": 90, "duration": "6 hours", "rating": 4.8},
                {"name": "Grand Bazaar Shopping", "price": 20, "duration": "3 hours", "rating": 4.5},
                {"name": "Turkish Bath Experience", "price": 100, "duration": "2 hours", "rating": 4.7},
                {"name": "Bosphorus Cruise", "price": 80, "duration": "3 hours", "rating": 4.8}
            ],
            "best_time": "April to May, September to November",
            "budget_range": "$ (Budget-friendly)",
            "climate": "Mediterranean/Continental"
        }
    },
    "beach": {
        "Maldives": {
            "description": "Tropical paradise with crystal clear waters and luxury resorts",
            "activities": [
                {"name": "Overwater Bungalow Stay", "price": 800, "duration": "24 hours", "rating": 4.9},
                {"name": "Snorkeling", "price": 100, "duration": "3 hours", "rating": 4.8},
                {"name": "Spa Treatments", "price": 200, "duration": "2 hours", "rating": 4.7},
                {"name": "Sunset Dolphin Cruise", "price": 150, "duration": "3 hours", "rating": 4.8}
            ],
            "best_time": "November to April",
            "budget_range": "$$$$ (Ultra-luxury)",
            "climate": "Tropical, warm year-round"
        },
        "Bali": {
            "description": "Indonesian island paradise with culture and beaches",
            "activities": [
                {"name": "Beach Club Experience", "price": 80, "duration": "6 hours", "rating": 4.6},
                {"name": "Temple Visits", "price": 40, "duration": "4 hours", "rating": 4.7},
                {"name": "Rice Terrace Tours", "price": 60, "duration": "5 hours", "rating": 4.8},
                {"name": "Surfing Lessons", "price": 70, "duration": "3 hours", "rating": 4.5}
            ],
            "best_time": "April to October",
            "budget_range": "$ (Budget-friendly)",
            "climate": "Tropical, wet and dry seasons"
        },
        "Santorini": {
            "description": "Greek island famous for sunsets and white-washed buildings",
            "activities": [
                {"name": "Sunset Viewing", "price": 30, "duration": "2 hours", "rating": 4.9},
                {"name": "Wine Tasting", "price": 120, "duration": "4 hours", "rating": 4.7},
                {"name": "Volcanic Tours", "price": 100, "duration": "6 hours", "rating": 4.6},
                {"name": "Beach Relaxation", "price": 50, "duration": "4 hours", "rating": 4.5}
            ],
            "best_time": "April to October",
            "budget_range": "$$$ (Expensive)",
            "climate": "Mediterranean"
        }
    },
    "city": {
        "Singapore": {
            "description": "Modern city-state with incredible food and attractions",
            "activities": [
                {"name": "Gardens by the Bay", "price": 40, "duration": "3 hours", "rating": 4.8},
                {"name": "Food Tours", "price": 80, "duration": "4 hours", "rating": 4.9},
                {"name": "Shopping Districts", "price": 60, "duration": "5 hours", "rating": 4.6},
                {"name": "Marina Bay Sands", "price": 100, "duration": "3 hours", "rating": 4.7}
            ],
            "best_time": "February to April",
            "budget_range": "$$$ (Expensive)",
            "climate": "Tropical, hot and humid"
        },
        "Barcelona": {
            "description": "Vibrant Spanish city with unique architecture and culture",
            "activities": [
                {"name": "Gaudí Architecture Tour", "price": 90, "duration": "5 hours", "rating": 4.8},
                {"name": "Tapas Tours", "price": 70, "duration": "3 hours", "rating": 4.7},
                {"name": "Beach Access", "price": 20, "duration": "4 hours", "rating": 4.5},
                {"name": "Park Güell Visit", "price": 50, "duration": "2 hours", "rating": 4.6}
            ],
            "best_time": "May to June, September to October",
            "budget_range": "$$ (Moderate)",
            "climate": "Mediterranean"
        },
        "Tokyo": {
            "description": "Ultra-modern metropolis blending tradition and innovation",
            "activities": [
                {"name": "Modern Culture Tour", "price": 100, "duration": "6 hours", "rating": 4.7},
                {"name": "Sushi Experiences", "price": 150, "duration": "2 hours", "rating": 4.9},
                {"name": "Technology Districts", "price": 60, "duration": "4 hours", "rating": 4.6},
                {"name": "Traditional Markets", "price": 40, "duration": "3 hours", "rating": 4.8}
            ],
            "best_time": "March to May, September to November",
            "budget_range": "$$$ (Expensive)",
            "climate": "Temperate, four seasons"
        }
    }
}

def get_destinations_by_category(category):
    """Get all destinations for a specific category"""
    return DESTINATIONS.get(category, {})

def get_all_destinations():
    """Get all destinations across all categories"""
    all_destinations = {}
    for category, destinations in DESTINATIONS.items():
        all_destinations.update(destinations)
    return all_destinations

def search_destinations(query):
    """Search destinations by name or description"""
    results = {}
    query_lower = query.lower()
    
    for category, destinations in DESTINATIONS.items():
        for dest_name, dest_info in destinations.items():
            if (query_lower in dest_name.lower() or 
                query_lower in dest_info['description'].lower() or
                query_lower in category.lower()):
                results[dest_name] = {**dest_info, 'category': category}
    
    return results
