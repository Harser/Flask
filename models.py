from peewee import Model, SqliteDatabase, CharField, IntegerField, FloatField, DateTimeField, ForeignKeyField, \
    ManyToManyField

db = SqliteDatabase('Movies.db')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Genres(BaseModel):
    name = CharField()

    def __str__(self):
        return self.name


class Movies(BaseModel):
    title = CharField()
    genres = ManyToManyField(Genres, backref='movies')
    year = IntegerField()

    def __str__(self):
        return self.title


class Ratings(BaseModel):
    rating = FloatField()
    timestamp = DateTimeField()
    movie = ForeignKeyField(Movies, backref='ratings')


class Users(BaseModel):
    name = CharField()


class Tags(BaseModel):
    tag = CharField()
    timestamp = DateTimeField()
    user = ForeignKeyField(Users, backref='tags')
    movie = ForeignKeyField(Movies, backref='tags')


MovieGenres = Movies.genres.get_through_model()

db.create_tables([
    Movies,
    Genres,
    Ratings,
    Users,
    Tags,
    MovieGenres])