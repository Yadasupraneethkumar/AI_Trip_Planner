import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper


class GooglePlaceSearchTool:
    def __init__(self,api_key:str):
        self.place_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.place_wrapper = GooglePlacesTool(gplaces_api_key=api_key)

    def google_search_attractions(self, place:str)->dict:
        """
        Searches for attractions in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"top attractive places in and around{place}")
    
    def google_search_restaurants(self, place:str)->dict:
        """
        Searches for avialable restaurants in the specified place using GooglePlaces API
        """
        return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
    
    def google_search_activity(self, place:str)-> dict:
        """
        Searches for popular activities in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"Activities in and around {place}")
    
    def google_search_tranportation(self, place: str)-> dict:
        """
        Searches for available modes of transportation in the specifies place using GooglePlaces API
        """
        return self.places_tool.run(f"What are the different modes of transportation available in {place}?")
    
# ********************** Geoapify *******************************    
    
import requests

class GeoapifyPlaceSearchTool:
    """
    Replacement for GooglePlaceSearchTool using Geoapify.
    Accepts a place name (city, location) and provides:
    - Attractions
    - Restaurants
    - Activities
    - Transportation options
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.places_url = "https://api.geoapify.com/v2/places"
        self.geocode_url = "https://api.geoapify.com/v1/geocode/search"

    def _geocode_place(self, place: str) -> tuple:
        """
        Convert place name to latitude and longitude using Geoapify Geocoding API.
        Returns (lat, lon) tuple.
        """
        params = {
            "text": place,
            "format": "json",
            "apiKey": self.api_key
        }
        response = requests.get(self.geocode_url, params=params)
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            lat = data["results"][0]["lat"]
            lon = data["results"][0]["lon"]
            return lat, lon
        else:
            raise ValueError(f"Could not geocode place: {place}")

    def _search(self, place: str, categories: str, limit: int = 10) -> dict:
        """
        Internal helper: search for POIs around the place using Geoapify Places API.
        """
        lat, lon = self._geocode_place(place)
        params = {
            "categories": categories,
            "filter": f"circle:{lon},{lat},5000",  # 5km radius
            "limit": limit,
            "apiKey": self.api_key
        }
        response = requests.get(self.places_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text, "status_code": response.status_code}

    def google_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place.
        """
        return self._search(place, categories="tourism.sights")

    def google_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place.
        """
        return self._search(place, categories="catering.restaurant")

    def google_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place.
        """
        return self._search(place, categories="tourism,museum,entertainment.sport")

    def google_search_tranportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place.
        """
        return self._search(place, categories="transport,public_transport,parking")
    
        
# class TavilyPlaceSearchTool:
#     def __init__(self):
#         pass

#     def tavily_search_attraction(self, place:str) -> dict:
#         """
#         Searches for attractions in the specified place using TavilySearch.
#         """
#         tavily_tool = TavilySearch(topic="general", include_answer="advanced")
#         result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
#         if isinstance(result, dict) and result.get("answer"):
#             return result["answer"]
#         return result
    
#     def tavily_search_restaurants(self, place:str)-> dict:
#         """
#         Searches for restaurants in the specified place using TavilySearch.
#         """
#         tavily_tool = TavilySearch(topic="general", include_answer="advanced")
#         result = tavily_tool.invoke({"query": f"What are the top 10 retaurants and eateries in and around {place}"})
#         if isinstance(result, dict) and result.get("answer"):
#             return result["answer"]
#         return result
    
#     def tavily_search_activity(self, place:str)-> dict:
#         """
#         Searches for popular activites in the specified place using TavilySearch.
#         """
#         tavily_tool = TavilySearch(topic="general", include_answer="advanced")
#         result = tavily_tool.invoke({"query": f"activities in and around {place}"})
#         if isinstance(result, dict) and result.get("answer"):
#             return result["answer"]
#         return result
    
#     def tavily_search_transportation(self, place:str)-> dict:
#         """
#         Searches for available modes of transportation in the specified place using TavilySearch.
#         """
#         tavily_tool = TavilySearch(topic="general", include_answer="advanced")
#         result = tavily_tool.invoke({"query": f"what are the different modes of tranportation in and around {place}"})
#         if isinstance(result, dict) and result.get("answer"):
#             return result["answer"]
#         return result


