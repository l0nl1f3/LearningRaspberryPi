import torch.nn as nn
import torch.nn.functional as F
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.hidden = nn.Linear(3, 5)
        self.out = nn.Linear(5, 4)
def forward(self, x):
    x = F.relu(self.hidden(x))
    x = self.out(x)
    return x
net=Net()
print(net)
