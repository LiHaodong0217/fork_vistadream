from pipe.cfgs import load_cfg
from pipe.c2f_recons import Pipeline

cfg = load_cfg(f'pipe/cfgs/basic.yaml')
cfg.scene.input.rgb = '/public/home/cit_haodongli/VistaDream/data/debug/color.png'
vistadream = Pipeline(cfg)
vistadream()#会调用__call__
