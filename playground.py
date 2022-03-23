import torch

a = torch.tensor([True, True, True, False])
b = torch.tensor([True, False, True, False])
print(torch.mul(a.long(), b.long()))