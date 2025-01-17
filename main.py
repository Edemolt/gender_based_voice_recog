import os
import pickle
from subprocess import run # for running R script

import pandas as pd

import neural_net
import sound_recorder

if __name__ == '__main__':
    while True:
        print('\nMenu')
        print('1. Train Neural Net')
        print('2. Analyse Voice')
        print('3. Exit')
        option = input('Enter Option Number: ')

        if option == '1':
            neural_net.run()
        elif option == '2':
            if not os.path.isfile('trained_neural_net'):  # check if neural_net file exists
                print('\nNeural net not trained. First train the neural net.')
            else:
                sound_recorder.run() # run sound recorder

                print('\nExtracting data from recorded voice...\n')
                run(['Rscript', 'getAttributes.r',
                     os.getcwd()])  # running R script for extracting data from recorded voice

                print('\n\nPreprocessing extracted data...')
                data = pd.read_csv('output/voiceDetails.csv') # read data from csv file
                del data['peakf'], data['sound.files'], data['selec'], data['duration'] # delete unnecessary columns
                dataset = pd.read_csv('voice.csv') # read dataset
                dataset = dataset.iloc[:, :-1] # delete last column
                data = (data - dataset.mean()) / (dataset.max() - dataset.min())  # scale

                trained_neural_net = pickle.load(open('trained_neural_net', 'rb'))  # load trained neural net from file

                print('\nPrediction: \r')
                print('Female' if trained_neural_net.predict(data)[0] == 0 else 'Male')  # print prediction
                break
        elif option == '3':
            print('\nExiting...')
            break
        else:
            print('\nInvalid option. Please try again...')
