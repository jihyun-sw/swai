class Movie:
    count = 0

    def __init__(self, title, duration, age):
        self.title = title
        self.duration = duration
        self.age = age
        Movie.count += 1
    
    def dispaly_info(self):
        print(f"제목: {self.title}, 러닝 타임: {self.duration}, 제한 연령: {self.age}")

movie1 = Movie("죽은 시인의 사회", 120, 12)
movie1.dispaly_info()