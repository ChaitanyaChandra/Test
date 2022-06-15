//server.js:
const express = require('express');
const redis = require('redis');

const app = express();
const client = redis.createClient({
    host: 'redis-server',
    port: 6379,
});

// Two get requests endpoints, have 2 counters
client.set('rootvisits', 0);
client.set('server1visits', 0);

app.get('/', (req, res) => {
    client.get('rootvisits', (err, visits) => {
        console.log("Root visit number: ", visits)
        res.send('Number of root visits ' + visits);
        client.set('rootvisits', parseInt(visits) + 1);
    });
});

app.get('/server1', (req, res) => {
    client.get('server1visits', (err, visits) => {
        console.log("Server1 visit number: ", visits)
        res.send('Number of server1 visits ' + visits);
        client.set('server1visits', parseInt(visits) + 1);
    });
});

app.listen(3000, () => {
    console.log('listening on port 3000');
});