# connection to MongoDB

from pymongo import MongoClient


# https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/
client = MongoClient('mongodb+srv://stefan:R&1o#I7dKQ2M@cluster0-isnkw.mongodb.net/<dbname>?retryWrites=true&w=majority')

db = client.gettingStarted
people = db.people

import datetime
personDocument = {
  "name": { "first": "Alan", "last": "Turing" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}
people.insert_one(personDocument)
people.find_one({ "name.last": "Turing" })
