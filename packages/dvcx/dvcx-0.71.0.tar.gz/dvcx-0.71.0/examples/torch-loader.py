# pip install Pillow torchvision

import torch
from PIL import Image
from torch import nn, optim
from torch.utils.data import DataLoader, IterableDataset
from torchvision import transforms

from dvcx.query import C, DatasetQuery, Object, udf
from dvcx.sql.types import String

STORAGE = "gcs://dvcx-datalakes/dogs-and-cats/"

# Define transformation for data preprocessing
transform = transforms.Compose(
    [
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)


def load_img(buf):
    return Image.open(buf).convert("RGB")


@udf(params=("name",), output={"label": String})
def extract_label(name):
    return (name[:3],)


CLASSES = ["cat", "dog"]


class DvcxDataset(IterableDataset):
    def __init__(self, storage, transform):
        self.storage = storage
        self.transform = transform

    def __iter__(self):
        q = (
            DatasetQuery(self.storage)
            .filter(C.name.glob("*.jpg"))
            .add_signals(extract_label)
        )
        for img, label in q.extract(Object(load_img), "label", cache=True):
            class_idx = CLASSES.index(label)
            yield self.transform(img), class_idx


train_loader = DataLoader(DvcxDataset(STORAGE, transform=transform), batch_size=16)


# Define torch model
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.fc1 = nn.Linear(64 * 8 * 8, 512)
        self.fc2 = nn.Linear(512, len(CLASSES))

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = torch.relu(self.conv3(x))
        x = x.view(-1, 64 * 8 * 8)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


model = CNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
num_epochs = 10
for epoch in range(num_epochs):
    for i, data in enumerate(train_loader):
        inputs, labels = data
        optimizer.zero_grad()

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # Backward pass and optimize
        loss.backward()
        optimizer.step()

        print("[%d, %5d] loss: %.3f" % (epoch + 1, i + 1, loss.item()))

print("Finished Training")
