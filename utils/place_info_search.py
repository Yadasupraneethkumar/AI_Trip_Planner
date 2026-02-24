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
        return self.places_tool.run(f"Activities in and aound {place}")
    
    def google_search_tranportation(self, place: str)-> dict:
        """
        Searches for available modes of transportation in the specifies place using GooglePlaces API
        """
        return self.places_tool.run(f"What are the different modes of transportation available in {place}?")
    
        
class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attraction(self, place:str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place:str)-> dict:
        """
        Searches for restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the top 10 retaurants and eateries in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place:str)-> dict:
        """
        Searches for popular activites in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_transportation(self, place:str)-> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the different modes of tranportation in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


