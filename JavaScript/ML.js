let label = "waiting...";

let classifier;
let modelURL = "https://teachablemachine.withgoogle.com/models/20Vd-aLxu/";

function preload() {
  classifier = ml5.soundClassifier(modelURL + "model.json");
}

function setup() {
  createCanvas(640, 520);

  classifyAudio();
}

function classifyAudio() {
  classifier.classify(gotResults);
}

function draw() {
  background(0);
  textAlign(CENTER, CENTER);

  let emoji = "🌲🌳";
  fill(255);
  text("shi");

  if (label == "ForestFire") {
    emoji = "🔥";
  } else if (label == "logging") {
    emoji = "🪵";
  }

  textSize(256);
  text(emoji, width / 2, height / 2);
}

function gotResults(error, results) {
  if (error) {
    console.error(error);
    return;
  }
  label = results[0].label;
}
