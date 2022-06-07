const express = require('express');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http);
s = []
last = "u"
app.get('/', function (req, res) {
    res.render('index.ejs');
});

let players = {};
let timerVal = 40;
io.sockets.on('connection', (socket) => {
    socket.on('username', ({ username, count }) => {
        socket.username = username;
        timerVal = 40;
        if(Object.keys(players).length == 2)
            players = {};
        players[username] = {
            Red: Number(count),
            Green: Number(count)
        }
        io.emit('player_connected', '🔵 <i> Player: ' + ((Object.keys(players).length - 1).toString()) + ' joined as :' + socket.username + '..</i>');
        if(Object.keys(players).length == 2)
        {
            setInterval(()=>{
                timerVal--;
                if (timerVal == 0){
                    io.emit('game_end', 'Time up');
                    clearInterval();
                }
                io.emit('timer_val', timerVal);
            }, 1000);
        }
    });

    socket.on('operation', ({ val, username }) => {
        // console.log(socket.username);
        if (socket.username == last) {
            io.emit('alert', "Other users turn, please wait");
        }
        else {
            last = socket.username
            console.log(socket.username);
            console.log(val);
            data=socket.username+"_"+val
            for (const key in players) {
                if (key != socket.username) {
                    console.log("in if");
                    if (s.includes(data)) {
                        console.log(data);
                        console.log("Already used...");
                        m = data+" this value already used"
                        io.emit('alert', m);
                    }
                    else {
                        console.log("adding");
                        console.log(data);
                        s.push(data)    
                    }
                    
                    io.emit('game_end',s.toString());
                    players[key] = (players[key] - val <= 0) ? 0 : players[key] - val;
                }
            }
            io.emit('game_continues', s.toString());    
        }
        
    });
});
const server = http.listen(8080, function () {
    console.log('listening on *:8080');
});