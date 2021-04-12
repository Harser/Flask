import os
from peewee import Model, SqliteDatabase, CharField, IntegerField, FloatField, DateTimeField, ForeignKeyField, \
    ManyToManyField
from playhouse.shortcuts import model_to_dict

db = SqliteDatabase(os.path.dirname(os.path.abspath(__file__)) + '/movies.db')
db.connect()


class BaseModel(Model):
    # TODO посмотреть, как нужно правильно делать сериализацию (перевод объекта в словарь) в Peewee
    def to_dict(self):
        raise NotImplemented

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

    def to_dict(self):
        return model_to_dict(self, manytomany=True)

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