import torch
import numpy as np
from torch import nn
from PIL import Image

device = torch.device("cuda") if torch.cuda.is_available else torch.device("cpu")

class ImageApproximatorFourier(nn.Module):
    def __init__(self, extra_dims):
        super().__init__()
        self.network = nn.Sequential(
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
            nn.Linear(256, 3),
            nn.Tanh()
        )

    def forward(self, input):
        return self.network(input)


if (__name__ == "__main__"):
    approximator = ImageApproximatorFourier(extra_dims=4).to(device)

    image = Image.open("Nature.png")

    optimizer = torch.optim.AdamW(approximator.parameters(), lr=0.001)

    width, height = image.size
    print(width,height)

    gaussian = torch.randn((2,128), dtype=torch.float32, device=device) * 10.0    
    expected = torch.tensor([image.getpixel((x,y))[:3] for x in range(width) for y in range(height)], dtype=torch.float32, device=device)/127.5-1.0
    for epoch in range(2000):
        output_image = Image.new(mode="RGB", size=(width,height))
        
        pixel_coords = torch.tensor([(x,y) for x in range(width) for y in range(height)], dtype=torch.float32, device=device)/127.5-1.0
        encoded_input = torch.zeros((width*height, 256), dtype=torch.float32, device=device) 
        for i in range(height*width):
            encoded_input[i] = torch.cat((torch.cos(2*torch.pi*(pixel_coords[i,:] @ gaussian)),torch.sin(2*torch.pi*(pixel_coords[i,:] @ gaussian))))
        estimated = approximator(encoded_input)

        #estimated = approximator(torch.tensor([(x/127.5-1.0,y/127.5-1.0,np.sin(x/127.5-1.0),np.cos(x/127.5-1.0),np.sin(2*np.pi*(x/127.5-1.0)),np.cos(2*np.pi*(x/127.5-1.0)),np.sin(y/127.5-1.0), np.cos(y/127.5-1.0), np.sin(2*np.pi*(y/127.5-1.0)), np.cos(2*np.pi*(y/127.5-1.0))) for x in range(width) for y in range(height)], dtype=torch.float32, device=device))

        for x in range(width):
            for y in range(height):
                pixel_values = (estimated[x*width+y] + 1.0)*127.5
                output_image.putpixel((x,y), tuple(torch.round(pixel_values).int().tolist()))

        output_image.save(f"generated_images/Gauss_10_{epoch}.png")

        loss = torch.nn.functional.mse_loss(estimated, expected) * 0.5
        print(f"loss: {loss.item()}\tepoch: {epoch}")
        #breakpoint()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()




            
            




