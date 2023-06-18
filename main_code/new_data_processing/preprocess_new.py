import os
from src.helpers import get_project_dir
from src.preprocessors import preprocess_data_and_get_vocabulary, preprocess_date, preprocess_date_in_data

import warnings
warnings.filterwarnings("ignore")


PROJECT_PATH = get_project_dir()
PATH_TO_READ = os.path.join(PROJECT_PATH, '../../data/raw/separated/new_data/')
PATH_TO_WRITE = os.path.join(PROJECT_PATH, '../../data/preprocessed/new_data/')
PATH_TO_VOCABULARY = os.path.join(PROJECT_PATH, '../../data/vocabulary/new_data/')
kwargs = {'path_to_read': PATH_TO_READ,
          'path_to_write': PATH_TO_WRITE,
          'path_to_vocabulary': PATH_TO_VOCABULARY,
          'chunksize': None}

print('+'+'='*100)
print('| Starting preprocessing step for NEW data')
##############################################################################################
###                              Preprocessing titles                                      ###
print('+'+'-'*60)
print('| Preprocessing NEW titles ...')
preprocess_data_and_get_vocabulary(filename='title.csv', **kwargs)
print('| Done')
##############################################################################################
###                               Preprocessing summaries                                  ###
print('+'+'-'*60)
print('| Preprocessing NEW summaries ...')
preprocess_data_and_get_vocabulary(filename='summary.csv', **kwargs)
print('| Done')
##############################################################################################
###                             Preprocessing basis dataframe                              ###
del kwargs['path_to_vocabulary']
print('+'+'-'*60)
print('| Preprocessing NEW basis data ...')
preprocess_date_in_data(filename='main.csv', **kwargs)
print('| Done')
print('+'+'='*100)


##############################################################################################
###                             Update vocabulary for titles                               ###
"""
TODO
"""
##############################################################################################
###                              Update vocabulary for summaries                           ###
"""
TODO
"""

##############################################################################################
###                             Lemmatizing new titles                                     ###
"""
TODO
"""
##############################################################################################
###                             Lemmatizing new summaries                                  ###
"""
TODO
"""

