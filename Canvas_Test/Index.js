const canvas = document.querySelector("canvas");
const c = canvas.getContext("2d")

canvas.width = 512
canvas.height = 480

c.fillStyle = "white"   //Color of the canvas
c.fillRect(0, 0, canvas.width, canvas.height) //This creates the interactable canvas where the game will run

const image = new Image()   //Creating the background
image.src = "./images/background.png"   //Create html image in javascript 

const playerImage = new Image()
playerImage.src = './images/playerDown.png'

class Sprite {
    constructor({position, velocity, image}) {
        this.position = position
        this.image = image
    }

    draw() {
        c.drawImage(this.image, this.position.x, this.position.y)
    }
}

const background = new Sprite({position: {
    x: 0,
    y: 0
    },
    image: image
})

const keys = {
    w: {
        pressed: false
    },
    a: {
        pressed: false
    },
    s: {
        pressed: false
    },
    d: {
        pressed: false
    }
}

function animate() {
    window.requestAnimationFrame(animate)
    background.draw()
    c.drawImage(
        playerImage,        //Crop the Image
        0,
        0,
        playerImage.width /4,
        playerImage.height,
        canvas.width / 2 - (playerImage.width / 4) / 2,      //Center the player on screen
        canvas.height / 2 - playerImage.height / 2,    //Define the offset 
        playerImage.width /4,
        playerImage.height,
    )

    if (keys.w.pressed && lastkey === "w")    background.position.y += 3
    else if (keys.a.pressed && lastkey === "a")    background.position.x += 3
    else if (keys.s.pressed && lastkey === "s")    background.position.y -= 3
    else if (keys.d.pressed && lastkey === "d")    background.position.x -= 3
}
animate()

let lastkey = ""
window.addEventListener("keydown", (e) => { //Create a key reader
    switch (e.key){
        case "w":
            keys.w.pressed =true
            lastkey = "w"
            break
        case "a":
            keys.a.pressed =true
            lastkey = "a"
            break
        case "s":
            keys.s.pressed =true
            lastkey = "s"
            break
        case "d":
            keys.d.pressed =true
            lastkey = "d"
            break        
    }
})

window.addEventListener("keyup", (e) => { //Create a key releaser
    switch (e.key){
        case "w":
            keys.w.pressed =false
            break
        case "a":
            keys.a.pressed =false
            break
        case "s":
            keys.s.pressed =false
            break
        case "d":
            keys.d.pressed =false
            break        
    }
})

