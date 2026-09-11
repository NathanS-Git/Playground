IntList sequence;

void setup() {
    size(500,500);
    background(240,240,240);
    sequence = new IntList(1,1,1);
}

void draw() {
    sequence.append(sequence.get(sequence.size()-2)+sequence.get(sequence.size()-3));
    print(sequence);
    delay(1000);
}
