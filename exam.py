import requests

class Movie:
    def __init__(self):
        self.url = "https://api.themoviedb.org/3/"
        self.Apı_Key = ""

    def PopulerMovie(self):
        n_url = f"{self.url}movie/popular?language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNWNiY2Y0ODMwYzc0Yzc3MjhhNGRkNDhlNTFhODdlNyIsIm5iZiI6MTcyMjM0OTU0Ny45OTQ2NzksInN1YiI6IjY2YThmNWIyMjEzNjhmNDc4MTVjNGNlZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dNOFQP2aI8t2zoKsd-NzwHFoZ4yh4wGFtgR2ByZ69dE"
        }
        response = requests.get(n_url, headers=headers)
        data = response.json()
        dat = data["results"]
        num = 1
        for i in dat:
            print(f"{num}-" ,i["title"])
            num += 1

    def SearchMovie(self,name):
        n_url = f"{self.url}search/movie?query={name}&include_adult=false&language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNWNiY2Y0ODMwYzc0Yzc3MjhhNGRkNDhlNTFhODdlNyIsIm5iZiI6MTcyMjM0OTU0Ny45OTQ2NzksInN1YiI6IjY2YThmNWIyMjEzNjhmNDc4MTVjNGNlZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dNOFQP2aI8t2zoKsd-NzwHFoZ4yh4wGFtgR2ByZ69dE"
        }

        response = requests.get(n_url, headers=headers)
        data = response.json()
        data = data["results"]
        num = 1
        print("Arama Sonucunuz: ")
        for i in data:
            print(f"{num}-",i["title"])
            num += 1

n = Movie()

while True:
    print("*"*30)
    sec = input("1-Popüler Filmler\n2-Film Arama3\n3-Çıkış\nSeçim: ")
    print("*"*30)
    if sec == "3":
        break
    else:
        if sec == "1":
            n.PopulerMovie()
        elif sec == "2":
            name = input("Aradığınız filmin adını giriniz: ")
            n.SearchMovie(name)
        else:
            print("Yanlış Seçim...")