import torch
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

def show_images(dataset, class_names, rows=3, cols=3):
    fig = plt.figure(figsize=(9, 9))
    for i in range(1, rows * cols + 1):
        idx = torch.randint(0, len(dataset), size=[1]).item()
        image, label = dataset[idx]
        fig.add_subplot(rows, cols, i)
        plt.imshow(image.squeeze(), cmap="gray")
        plt.title(class_names[label])
        plt.axis(False)

def dataloader(train_dataset, test_dataset, batch_size):
    return (
        DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True), 
        DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False),
        train_dataset.classes
    )