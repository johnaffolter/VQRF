_base_ = './llff_default_lg.py'

expname = 'trex_lg'

data = dict(
    datadir='/bfs/HoloResearch/NeRFData/nerf_llff_data/trex/',
    dataset_type='my_llff',
    ndc=True,
    # width=1008,
    # height=756,
    rand_bkgd=True,
)
