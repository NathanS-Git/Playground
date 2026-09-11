import torch
from torch import nn
from PIL import Image

device = torch.device("cuda") if torch.cuda.is_available else torch.device("cpu")

class ImageApproximator(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(2, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 100),
            nn.ReLU(),
            nn.Linear(100, 3),
            nn.Tanh()
        )

    def forward(self, input):
        return self.network(input)


if (__name__ == "__main__"):
    approximator = ImageApproximator().to(device)

    image = Image.open("Nature.png")

    optimizer = torch.optim.AdamW(approximator.parameters(), lr=0.001)

    width, height = image.size
    print(width,height)
    
    expected = torch.tensor([image.getpixel((x,y))[:3] for x in range(width) for y in range(height)], dtype=torch.float32, device=device)/127.5-1.0
    for epoch in range(2000):
        output_image = Image.new(mode="RGB", size=(width,height))
        
        estimated = approximator(torch.tensor([(x,y) for x in range(width) for y in range(height)], dtype=torch.float32, device=device)/127.5-1.0)

        for x in range(width):
            for y in range(height):
                pixel_values = (estimated[x*width+y] + 1.0)*127.5
                output_image.putpixel((x,y),tuple(torch.round(pixel_values).int().tolist()))

        output_image.save(f"Test_{epoch}.png")

        loss = torch.nn.functional.mse_loss(estimated, expected)
        print(f"loss: {loss.item()}\tepoch: {epoch}")
        #breakpoint()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()




            
            




