import re
import time
from locust import HttpUser, task, between
from requests.models import Response

class QuickstartUser(HttpUser):
    wait_time = between(1,2.5)

    @task
    def home(self):
        self.client.get("/")
    
    @task(3)
    def vier_tour(self):
        for id in range(10):
            self.client.get(f"/tour/{id}/")
            time.sleep(1)
    
    def on_start(self):
        self.login()
    
    def login(self):
        response = self.client.get('/accounts/login/')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/accounts/login/',
            {'username':'servidor', 'password':'Secret.123'},
            headers={'X-CSRFToken':csrftoken})