print('Start #################################################################');

db = db.getSiblingDB('starwars-api');
db.createUser(
  {
    user: 'starwars-api',
    pwd: 'P4S5w0Rd',
    roles: [{ role: 'readWrite', db: 'starwars-api' }],
  },
);
db.createCollection('movie');
db.createCollection('planet');

print('END #################################################################');