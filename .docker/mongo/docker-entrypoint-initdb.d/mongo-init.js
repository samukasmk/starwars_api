print('Start #################################################################');

db = db.getSiblingDB('starwars');
db.createUser(
  {
    user: 'starwars',
    pwd: 'starwars',
    roles: [{ role: 'readWrite', db: 'starwars' }],
  },
);
db.createCollection('movie');
db.createCollection('planet');

print('END #################################################################');