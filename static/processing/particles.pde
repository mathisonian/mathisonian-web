
ArrayList particles = new ArrayList();

PImage img = new PImage();

PVector attractor;
PVector leftTop, dimension;

// Increase this to add fewer particles.
// Bigger number == less computationally
// intensive
float skipFactor = 2;

void setup() {
  img = loadImage("http://mathisonian-web.s3.amazonaws.com/images/Hacker_Emblem.png");
  size(img.width, img.height, P2D);
  background(255);
  image(img, 0,0);
  color c;
  /*initialize particles*/
  for(int i = 0; i < width; i=round(i+skipFactor)) {
    for(int j = 0; j<height; j=round(j+skipFactor)) {
      c = img.get(i,j);
      if(red(c) + green(c) + blue(c) < 250 * 3 ) {
          particles.add(new Particle(i, j, c));       
      }
    }
  }
}

void draw() {
  noStroke();
  rect(0, 0, width, height);
  
  for(Particle particle : particles)
  {
    particle.update();
    particle.show();
  }
  fill(255);
}

class Particle
{
  PVector location;
  PVector velocity;
  PVector acceleration;
  PVector attractor;
  PVector originalLocation;
  PVector previousLocation;
  
  float mouseAttraction;
  float imageAttraction;
  color c;
  
  Particle(int x, int y, color c) {
    originalLocation = new PVector(x,y);
    location = new PVector(x,y);
    velocity = new PVector(random(-0.2, 0.2),random(-0.2, 0.2));
    acceleration = new PVector(random(-0.2, 0.2),random(-0.2, 0.2));
    mouseAttraction = random(0.6, 0.9);
    imageAttraction = random(0.9, 1.1);
    this.c = c;
  }
  
  void show()
  {
    stroke(c, 75);
    line(previousLocation.x, previousLocation.y, location.x, location.y);
  }
  
  void update()
  {
    /*bounce back on hitting the border*/
    if(location.x >= width || location.x < 0) {
      velocity.x = -velocity.x;
    }
    if(location.y >= height || location.y < 0) {
      velocity.y = -velocity.y;
    }
      
    previousLocation = location.get();
    velocity.add(acceleration);
    location.add(velocity);
    
    /*ignores all attractors and friction when mouse pressed*/
    if(mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < width) {
      attractor = PVector.sub(new PVector(mouseX, mouseY), location);
      attractor.normalize();
      attractor.mult(mouseAttraction);
      acceleration = attractor.get();
    } else {
      acceleration.x=0;
      acceleration.y=0;
    }
    
    if(!mousePressed && location.x >= 0 && location.x < width && location.y >= 0 && location.y < height) {
      attractor = PVector.sub(originalLocation, location);
      attractor.normalize();
      attractor.mult(imageAttraction);
      acceleration.add(attractor);      
    }
    velocity.mult(.95);
    
  }
}