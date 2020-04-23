/**
  BY:              Callum Clegg
  TITLE:           Hyperbolic Helicoid
  LAST UPDATED:    Thursday 2nd April 2020
                 
  DESC:            Draws a wireframe hyperbolic helicoid (Java).
*/
// ------------------------------------START----------------------------------------
// ~variables
ArrayList<PVector> points = new ArrayList();

float              u;
float              v;
float              angleX       = 0;
float              angleY       = 0;

final static int   NUM_SHOW     = 3; // No# of hyperbolic helicoids - 1
// ---------------------------------------------------------------------------------
void setup() {
  size       (800, 800, P3D);
  colorMode  (HSB);
  
  for (float u = -TAU; u <= TAU; u += 0.037) {
    for (float v = -1; v <= 1; v += 0.09) // or v += 0.5
    {
      points.add(new PVector( // 1/v also works here.
      hyperX(u, v, 2) * 2,
      hyperY(u, v, 2) * 2,
      hyperZ(u, v   ) * 2
      ));
    }
  }
}
// ---------------------------------------------------------------------------------
void draw() {
  background  (28);  
  showData    ();
}
// ---------------------------------------------------------------------------------
// plots, rotates and colourises hyperbolic helicoid.
void showData() {
 
  noFill         ();
  lights         ();
  translate      (width/2, height/2, -300);
 
  angleX +=     -TAU/800;
  angleY +=      TAU/800;
   
  rotateY        (sin(angleX) * 10);
  rotateX        (sin(angleY)     );
 
  float          hu = 0;
 
  beginShape();  
  for (int j = 1; j < NUM_SHOW; j++ ) {
    for (PVector v : points)
    {
      stroke(hu+=0.1 * (j * 0.1), 180, 170); // colour of object changes as vectors are plotted.
      strokeWeight   (2 * 2/j);
      point // or 'point'
      (
        (400 * v.x) * j/2,
        (400 * v.y) * j/2,
        (200 * v.z) * j/2
      );
      if  (hu > 255) { hu = 0; }
    }
  }
  endShape();  
}
// ---------------------------------------------------------------------------------
// Parametric equations for hyperbolic helicoid.
static final float hyperX(final float u, final float v, final float phi) {
  return (float)
  ((Math.sinh(v) * cos(phi * u))  /  (1 + Math.cosh(u) * Math.cosh(v)));
}

static final float hyperY(final float u, final float v, final float phi) {
  return (float)
  ((Math.sinh(v) * sin(phi * u))  /  (1 + Math.cosh(u) * Math.cosh(v)));
}

static final float hyperZ(final float u, final float v) {
  return (float)
  ((Math.cosh(v) * Math.sinh(u))  /  (1 + Math.cosh(u) * Math.cosh(v/* or 1/v */)));
}
// -------------------------------------END-----------------------------------------
