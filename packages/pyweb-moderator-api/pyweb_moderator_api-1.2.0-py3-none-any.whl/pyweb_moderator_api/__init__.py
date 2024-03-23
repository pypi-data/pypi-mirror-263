import aiohttp
import requests
from typing import Literal
import time, asyncio
import urllib.parse as urlparse
from dataclasses import dataclass

@dataclass
class Response:
    error: dict | None
    text_class: str
    time_taken: float
    confidence: float
    unique_id: str
    balance: float
    label: str

@dataclass
class PredictionInfo:
    error: dict | None
    text_class: str
    confidence: float
    text: str

def syncPost(url, json):
    attempts = 0

    while True:
        try:
            response = requests.post(url, json=json)
            return response
        except Exception as e:
            if attempts == 3:
                return {"error": e}
            attempts += 1
            time.sleep(1)

def syncGet(url, json):
    attempts = 0

    while True:
        try:
            response = requests.get(url, json=json)
            return response
        except Exception as e:
            if attempts == 3:
                return {"error": e}
            attempts += 1
            time.sleep(1)

async def asyncPost(url, json):
    attempts = 0

    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json) as response:
                    return await response.json()
        except Exception as e:
            if attempts == 3:
                return {"error": e}
            attempts += 1
            await asyncio.sleep(1)

async def asyncGet(url, json):
    attempts = 0

    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, json=json) as response:
                    return await response.json()
        except Exception as e:
            if attempts == 3:
                return {"error": e}
            attempts += 1
            await asyncio.sleep(1)

class SyncAPI:
    def __init__(self, token: str = None, base_url: str = "http://pywebsolutions.ru:30"):
        self.token = token
        self.base_url = base_url

        with syncPost(urlparse.urljoin(self.base_url, "get_key"), json={"api_token": self.token}) as r:
            self.api_info = r.json()
            if "error" in self.api_info:
                raise Exception(str(self.api_info))
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def getClass(self, text: str, model: Literal["bert", "tinybert"] = "bert") -> Response:
        with syncPost(urlparse.urljoin(self.base_url, "predict"), json={"text": text, "api_token": self.token, "model": model}) as r:
            result = r.json()

            if "error" in result:
                return Response(result["error"], None, None, None, None, None, None)
            
            return Response(None, result["class"], result["time_taken"], result["confidence"], result["unique_id"], result["balance"], result["class_names"][str(result["class"])])
    
    def getAPIInfo(self):
        with syncPost(urlparse.urljoin(self.base_url, "get_key"), json={"api_token": self.token}) as r:
            self.api_info = r.json()
            if "error" in self.api_info:
                raise Exception(str(self.api_info))
        
        return self.api_info
    
    def getPrediction(self, unique_id: str):
        with syncPost(urlparse.urljoin(self.base_url, "get_prediction"), json={"api_token": self.token, "unique_id": unique_id}) as r:
            result = r.json()
            if "error" in self.api_info:
                raise Exception(str(self.api_info))

            if "error" in result:
                return PredictionInfo(result["error"], None, None, None)
            
            return PredictionInfo(result["error"] if "error" in result else None, result["class"], result["confidence"], result["text"])
    
    def getPrice(self):
        with syncGet(urlparse.urljoin(self.base_url, "price")) as r:
            result = r.json()
            if "error" in self.api_info:
                raise Exception(str(self.api_info))
            return result

class AsyncAPI:
    def __init__(self, token: str = None, base_url: str = "http://pywebsolutions.ru:30"):
        self.token = token
        self.base_url = base_url

    async def __aenter__(self):
        r = await asyncPost(urlparse.urljoin(self.base_url, "get_key"), json={"api_token": self.token})

        self.api_info = r

        if "error" in self.api_info:
            raise Exception(str(self.api_info))
        
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        pass
    
    async def getClass(self, text: str, model: Literal["bert", "tinybert"] = "bert") -> Response:
        r = await asyncPost(urlparse.urljoin(self.base_url, "predict"), json={"text": text, "api_token": self.token, "model": model})

        result = r
        
        if "error" in result:
            return Response(result["error"], None, None, None, None, None, None)
        
        return Response(None, result["class"], result["time_taken"], result["confidence"], result["unique_id"], result["balance"], result["class_names"][str(result["class"])])
    
    async def getAPIInfo(self):
        r = await asyncPost(urlparse.urljoin(self.base_url, "get_key"), json={"api_token": self.token})

        self.api_info = r
        if "error" in self.api_info:
            raise Exception(str(self.api_info))

        return self.api_info
    
    async def getPrediction(self, unique_id: str):
        r = await asyncPost(urlparse.urljoin(self.base_url, "get_prediction"), json={"api_token": self.token, "unique_id": unique_id})
        
        result = r
        if "error" in self.api_info:
            raise Exception(str(self.api_info))
        
        if "error" in result:
            return PredictionInfo(result["error"], None, None, None)
        
        return PredictionInfo(result["error"] if "error" in result else None, result["class"], result["confidence"], result["text"])
    
    async def getPrice(self):
        r = await asyncGet(urlparse.urljoin(self.base_url, "price"))

        result = r
        if "error" in self.api_info:
            raise Exception(str(self.api_info))
        return result