const canvas = document.querySelector("canvas");
const c = canvas.getContext("2d");

canvas.width = 512;
canvas.height = 480;

c.fillStyle = "white";
c.fillRect(0, 0, canvas.width, canvas.height);

const image = new Image();
image.src = "./images/background.png";


//Creation of character and npc and text


class Sprite {
  constructor({position, velocity, image}) {
    this.position = position;
    this.velocity = velocity;
    this.image = image;
  }

  draw() {
    c.strokeStyle = "black";
    c.strokeRect(this.position.x - 1, this.position.y - 1, this.image.width + 2, this.image.height + 2);
    c.drawImage(this.image, this.position.x, this.position.y);
  }
  update(delta) {
    this.position.x += this.velocity.x * delta;
    this.position.y += this.velocity.y * delta;

    this.position.x = Math.max(0, Math.min(this.position.x, canvas.width - this.image.width));
    this.position.y = Math.max(0, Math.min(this.position.y, canvas.height - this.image.height));
  }
}


const background = new Sprite({
  position: { x: 0, y: 0 },
  image: image,
});

// Create the textbox element
const textbox = document.createElement("div");
textbox.id = "textbox";
textbox.textContent = "Hello, world!";
textbox.style.position = "absolute";
textbox.style.top = "50px";
textbox.style.left = "250px";
textbox.style.width = "200px";
textbox.style.height = "100px";
textbox.style.backgroundColor = "white";
textbox.style.border = "1px solid black";
textbox.style.padding = "10px";
textbox.style.fontSize = "16px";

// Add the textbox to the document
document.body.appendChild(textbox);
textbox.style.display = "none";

const keys = {
  w: { pressed: false },
  a: { pressed: false },
  s: { pressed: false },
  d: { pressed: false },
};

class NPC extends Sprite {
  constructor({position, velocity, image}) {
    super({position, velocity, image});
    this.speed = 5;
    this.velocity = { x: 0, y: 0 };
  }

  update(delta) {
    // Check for collisions with the player
    if (player && this.collidesWith(player)) {
      console.log("Collision detected!");
      // If the NPC collides with the player, move the NPC back to its previous position
      this.position = { ...this.prevPosition };
    } else {
      // Update the position based on the velocity
      this.position.x += this.velocity.x * delta;
      this.position.y += this.velocity.y * delta;

      // Make sure the NPC stays within the canvas
      this.position.x = Math.max(0, Math.min(this.position.x, canvas.width - this.image.width));
      this.position.y = Math.max(0, Math.min(this.position.y, canvas.height - this.image.height));
    }
  }
  
  collidesWith(other) {
    return (
      this.position.x < other.position.x + other.image.width &&
      this.position.x + this.image.width > other.position.x &&
      this.position.y < other.position.y + other.image.height &&
      this.position.y + this.image.height > other.position.y
    );
  }
}



class Player extends Sprite {
  constructor({position, velocity, image, width, height}) {
    super({position, velocity, image});
    this.width = width;
    this.height = height;
    this.speed = 10;
    this.velocity = { x: 0, y: 0 };
    this.prevPosition = {...position}; // store the initial position as previous position
  }


  setVelocity(x, y) {
    this.velocity = { x, y };
  }

  update(delta) {
    // Save the previous position
    this.prevPosition = { ...this.position };

    // Check for collisions with the NPC
    if (npc && this.collidesWith(npc)) {
      console.log("Collision detected!");

      // If the player collides with the NPC, move the player back to their previous position
      this.position = { ...this.prevPosition };
    } else {
      // Update the position based on the velocity
      const nextX = this.position.x + this.velocity.x * delta;
      const nextY = this.position.y + this.velocity.y * delta;

      // Check if the next position will collide with the NPC
      const nextPosition = { x: nextX, y: nextY };
      if (npc && this.collidesWith(npc, nextPosition)) {
        console.log("Collision detected!");
        // If the player will collide with the NPC, don't update the position
      } else {
        // Update the position
        this.position.x = Math.max(0, Math.min(nextX, canvas.width - this.image.width));
        this.position.y = Math.max(0, Math.min(nextY, canvas.height - this.image.height));
      }
    }
  }

  isAdjacentTo(npc) {
    var playerX = this.position.x;
    var playerY = this.position.y;
    var npcX = npc.position.x;
    var npcY = npc.position.y;

    var isAdjacent = false;

    if (Math.abs(playerX - npcX) <= 175 && Math.abs(playerY - npcY) <= 175) {
      isAdjacent = true;
    }

    return isAdjacent;
  }

  collidesWith(other, position = this.position) {
    return (
      position.x < other.position.x + other.image.width &&
      position.x + this.width > other.position.x &&
      position.y < other.position.y + other.image.height &&
      position.y + this.height > other.position.y
    );
  }

  moveLeft() {
    const prevX = this.position.x;
    this.position.x -= 32;
  }

  moveRight() {
    const prevX = this.position.x;
    this.position.x += 32;
  }

  moveUp() {
    const prevY = this.position.y;
    this.position.y -= 32;
  }

  moveDown() {
    const prevY = this.position.y;
    this.position.y += 32;
  }
}




let player;
let isInteracting = false;




const npcImage = new Image();
npcImage.src = './images/npcTEST.png';

const playerImage = new Image();
playerImage.src = './images/playerDown.png';

npcImage.onload = () => {
   npc = new NPC({
    position: {
      x: canvas.width / 8 - (npcImage.width / 4) / 2,
      y: canvas.height / 2 - npcImage.height / 2,
    },
    velocity: { x: 0, y: 0 },
    image: npcImage,
  });
  animate();
};


playerImage.onload = () => {
  player = new Player({
    position: {
      x: canvas.width / 2 - (playerImage.width / 4) / 2,
      y: canvas.height / 2 - playerImage.height / 2,
    },
    velocity: { x: 0, y: 0 },
    image: playerImage,
    width: 32,
    height: 32,
  });
  animate();
};
// Create an instance of NPC
npc = new NPC({
  position: { x: 100, y: 100 },
  velocity: { x: 0, y: 0 },
  image: npcImage // assuming you have loaded an image for the NPC
});

//functions

function update(delta) {
  player.update(delta);
  npc.update(delta);


}

function animate() {
    window.requestAnimationFrame(animate);
  
    background.draw(background);

    if (npc) {
      npc.draw();
    }
  
    if (player) {
      player.update(1 / 60);
      player.draw();

      if (keys.w.pressed) player.moveUp();
      if (keys.a.pressed) player.moveLeft();
      if (keys.s.pressed) player.moveDown();
      if (keys.d.pressed) player.moveRight();
  
      // AABB collision detection
      if (
        player.position.x < npc.position.x + npc.image.width / 4 &&
        player.position.x + player.image.width / 4 > npc.position.x &&
        player.position.y < npc.position.y + npc.image.height / 4 &&
        player.position.y + player.image.height > npc.position.y
      ) {

        console.log("Collision detected!");
      }
    }
  }





//Event listners (movement, button to talk)

let lastkey = ""
document.addEventListener("keydown", event => {
  if (event.code === "KeyW") {
    player.setVelocity(player.velocity.x, -player.speed);
  } else if (event.code === "KeyA") {
    player.setVelocity(-player.speed, player.velocity.y);
  } else if (event.code === "KeyS") {
    player.setVelocity(player.velocity.x, player.speed);
  } else if (event.code === "KeyD") {
    player.setVelocity(player.speed, player.velocity.y);
  }
});

document.addEventListener("keyup", event => {
  if (event.code === "KeyW" || event.code === "KeyS") {
    player.setVelocity(player.velocity.x, 0);
  } else if (event.code === "KeyA" || event.code === "KeyD") {
    player.setVelocity(0, player.velocity.y);
  }
});

document.addEventListener("keydown", function(event) {
  if (event.key === "e") { // check if E key is pressed
    if (player.isAdjacentTo(npc)) {
      textbox.style.display = "block";
          }
}
}
);
document.addEventListener("keyup", function(event) {
  if (event.key === "e") { // check if E key is pressed
    if (player.isAdjacentTo(npc)) {
      textbox.style.display = "none";
          }
}
}
);
