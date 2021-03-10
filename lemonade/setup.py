# AUTOGENERATED! DO NOT EDIT! File to edit: 00_setup.ipynb (unless otherwise specified).

__all__ = ['get_device', 'DATA_STORE', 'LOG_STORE', 'MODEL_STORE', 'EXP_STORE', 'DEVICE', 'PATH_1K', 'PATH_10K',
           'PATH_20K', 'PATH_100K', 'FILENAMES', 'SYNTHEA_DATAGEN_DATES', 'CONDITIONS', 'LABELS',
           'LOG_NUMERICALIZE_EXCEP']

# Cell
from fastai.imports import *

# Cell
def get_device():
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        assert torch.backends.cudnn.enabled == True
        torch.backends.cudnn.benchmark = True #Enable cuDNN auto-tuner - perf benefit for convs
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    return device

# Cell
DATA_STORE  = f'{Path.home()}/code/datasets'
LOG_STORE   = f'{Path.home()}/code/logs/lemonade'
MODEL_STORE = f'{Path.home()}/code/models/lemonade'
EXP_STORE   = f'{Path.home()}/code/experiments/lemonade'

# Cell
DEVICE = get_device()

PATH_1K   = f'{DATA_STORE}/synthea/1K'
PATH_10K  = f'{DATA_STORE}/synthea/10K'
PATH_20K  = f'{DATA_STORE}/synthea/20K'
PATH_100K = f'{DATA_STORE}/synthea/100K'

FILENAMES = ['patients', 'observations', 'allergies', 'careplans', 'medications', 'imaging_studies', 'procedures', 'conditions', 'immunizations']

SYNTHEA_DATAGEN_DATES = dict({'1K':'11-16-2018', '10K':'12-19-2019', '20K':'11-5-2020', '100K':'4-4-2020', '250K':'11-16-2018'})

CONDITIONS = dict({'diabetes':'44054006||START', 'stroke':'230690007||START', 'alzheimers':'26929004||START', 'coronary_heart':'53741008||START'})

LABELS = ['diabetes', 'stroke', 'alzheimers', 'coronaryheart']

LOG_NUMERICALIZE_EXCEP = True