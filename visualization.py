import torch
from ops.utils import save_ply
scene = torch.load(f'/public/home/cit_haodongli/VistaDream/data/sd_readingroom/scene.pth')
save_ply(scene,'gf.ply')