movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def highScore(movie):
    if movie["imdb"] > 5.5:
        return True 
    else:
        return False
def bestMovies(movies):
    listOfMovies = []
    for movie in movies:
        if highScore(movie):
            listOfMovies.append(movie["name"])
    print(listOfMovies)
def categorySort(movies, category):
    output = []
    for movie in movies:
        if movie["category"] == category:
            output.append(movie["name"])
    print(output)
def averageScore(movies):
    count = 0
    total = 0
    for movie in movies:
        total += movie["imdb"]
        count += 1
    print(f'Average IMDB score for all movies in the list is {total/count}')
def scoreByCategory(movies, category):
    total = 0
    count = 0
    for movie in movies:
        if movie["category"] == category:
            total += movie["imdb"]
            count += 1
    print(f'Average IMDB score in category {category} is {total / count}')

highScore(movies[1])#returns True
highScore(movies[2])#returns True
highScore(movies[8])#returns False

bestMovies(movies)#['Usual Suspects', 'Hitman', 'Dark Knight', 'The Help', 'The Choice', 'Colonia', 'Love', 'Joking muck', 'What is the name', 'Detective', 'We Two']

categorySort(movies, "Suspense")#['What is the name', 'Detective']
categorySort(movies, "Romance")#['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']

averageScore(movies)#Average IMDB score for all movies in the list is 6.486666666666667

scoreByCategory(movies, "Romance")#Average IMDB score in category Romance is 6.44
scoreByCategory(movies, "Thriller")#Average IMDB score in category Thriller is 5.6
scoreByCategory(movies, "Suspense")#Average IMDB score in category Suspense is 8.1
