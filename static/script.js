const grid = document.getElementById("grid");
const ctx = grid.getContext("2d");
const graph = document.getElementById("graph");
const gctx = graph.getContext("2d");

let gridSize = 6;
let cell = grid.width / gridSize;
let rewards = [];

function draw(agent, foods, walls) {
    ctx.clearRect(0,0,grid.width,grid.height);

    for(let i=0;i<gridSize;i++){
        for(let j=0;j<gridSize;j++){
            ctx.strokeRect(j*cell,i*cell,cell,cell);
        }
    }

    // Walls
    ctx.fillStyle = "black";
    walls.forEach(w => ctx.fillRect(w[1]*cell,w[0]*cell,cell,cell));

    // Foods
    ctx.fillStyle = "red";
    foods.forEach(f => ctx.fillRect(f[1]*cell,f[0]*cell,cell,cell));

    // Agent
    ctx.fillStyle = "blue";
    ctx.fillRect(agent[1]*cell,agent[0]*cell,cell,cell);
}

function drawGraph() {
    gctx.clearRect(0,0,graph.width,graph.height);
    gctx.beginPath();
    gctx.moveTo(0, graph.height);

    rewards.forEach((r,i)=>{
        gctx.lineTo(i*8, graph.height - (r+10)*5);
    });

    gctx.stroke();
}

function start() {
    setInterval(()=>{
        fetch("/step")
        .then(res=>res.json())
        .then(data=>{
            document.getElementById("score").innerText = data.score;
            rewards = data.rewards;
            draw(data.agent, data.foods, data.walls);
            drawGraph();
        });
    },500);
}
