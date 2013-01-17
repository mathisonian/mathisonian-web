
ArrayList particles = new ArrayList();

/* @pjs preload="/static/images/huffpost_tech_logo.jpg"; */
/* @pjs transparent="true"; */
PImage img;

PVector attractor;
PVector leftTop, dimension;

// Increase this to add fewer particles.
// Bigger number == less computationally
// intensive
float skipFactor = 3.5;
float widthDiff, heightDiff;

void setup() {
  img = loadImage("/static/images/huffpost_tech_logo.jpg");
  
  float widthFactor = 2;
  float heightFactor = 1.5;

  size(img.width * 2.5, img.height * 2.5, P2D);
  // background(255);
  // image(img, (width - img.width) / 2, (height - img.height) / 2);
  color c;
  /*initialize particles*/
  for(int i = 0; i < img.width; i++) {
    for(int j = 0; j<img.height; j=round(j+skipFactor)) {
      c = img.get(i,j);
      if(red(c) + green(c) + blue(c) < 250 * 3 ) {
          particles.add(new Particle(i, j, c));       
      }
    }
  }
}

void draw() {
  // noStroke();
  // rect(0, 0, width, height);
  background(0,0);
  
  for(Particle particle : particles)
  {
    particle.update();
    particle.show();
  }
  // fill(255);
}

class Particle
{
  PVector location;
  PVector velocity;
  PVector acceleration;
  PVector attractor = new PVector();
  PVector originalLocation;
  PVector previousLocation;
  
  float mouseAttraction;
  float imageAttraction;
  color c;
  
  Particle(int x, int y, color c) {
    originalLocation = new PVector((width - img.width) / 2 + x, (height - img.height) / 2 + y);
    location = new PVector((width - img.width) / 2 + x, (height - img.height) / 2 + y);
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
      attractor.x = mouseX - location.x;
      attractor.y = mouseY - location.y;
      attractor.normalize();
      attractor.mult(mouseAttraction);
      acceleration = attractor.get();
    } else {
      acceleration.x=0;
      acceleration.y=0;
    }
    
    if(!mousePressed && location.x >= 0 && location.x < width && location.y >= 0 && location.y < height) {
      attractor.x = originalLocation.x - location.x;
      attractor.y = originalLocation.y - location.y;
      attractor.normalize();
      attractor.mult(imageAttraction);
      acceleration.add(attractor);      
    }
    velocity.mult(.95);
    
  }
}