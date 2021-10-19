// importing files
const http = require('http');
const fs = require('fs');
const express = require('express');
const app = express();
const server = http.createServer(app);
const MongoClient = require('mongodb').MongoClient;
const { find } = require('async')
const path = require('path');
const bodyParser = require('body-parser');
const hostname = "127.0.0.1";
const port = process.env.PORT || 3000;

// setting config
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static("public"))
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

var objectId;
var info;
async function childprocess() {
    var spawn = require('child_process').spawn('python', ['./testing.py', objectId]);
    spawn.stdout.on('data', data => {
        console.log(data.toString());
    })

}

// for mongoclient
const url = 'mongodb://localhost:27017'
MongoClient.connect(url, function (err, db) {
    if (err) throw err;

    else {
        // create database
        var database = db.db("health_db")

        // store data recieved from html forms
        app.post('/health', (req, res) => {
            var object =
            {
                symptoms1: req.body.Symptom_1,
                symptoms2: req.body.Symptom_2,
                symptoms3: req.body.Symptom_3
            }
            database.collection("Symptoms").insertOne(object, function (err, result) {
                if (err) throw err;
                objectId = result.insertedId;
                console.log(objectId)
                childprocess();
                setTimeout(function () {
                    res.redirect('/showdata')
                }, 20000);
            })
            app.get('/showdata', (req, res) => {
                var query = { _id: objectId };
                database.collection("Symptoms").find(query).toArray(function (err, result) {
                    info = result;
                    console.log(info);
                    console.log(objectId);
                    res.send('outputdata', { data: info });
                })
            })
        })
    }
})

// routes
app.get('/', (req, res) => {
    res.render('home')
})


//listen
server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}`);
})