import pandas as pd

# Sample data for illustration purposes (replace this with your actual data)
data = {
    'sound.files': ['sound1.wav', 'sound2.wav', 'sound3.wav'],
    'selec': [1, 2, 3], # Sample values for selection
    'duration': [10.5, 8.2, 15.1], # Sample values for duration
    'meanfreq': [2.5, 3.1, 4.8], # Sample values for mean frequency
    'sd': [0.7, 0.9, 1.3], # Sample values for standard deviation
    'median': [2.6, 3.2, 4.9], # Sample values for median frequency
    'Q25': [2.1, 2.8, 4.2], # Sample values for first quantile
    'Q75': [3.0, 3.6, 5.5], # Sample values for third quantile
    'IQR': [0.9, 0.8, 1.3], # Sample values for interquantile range
    'skew': [0.15, -0.25, 0.35],  # Sample values for skewness
    'kurt' : [0.25, -0.35, 0.45],  # Sample values for kurtosis
    'sp.ent': [0.75, 0.85, 0.95],  # Sample values for spectral entropy
    'sfm': [0.65, 0.75, 0.85],  # Sample values for spectral flatness measure
    'mode': [2.5, 3.1, 4.8],  # Sample values for mode frequency
    'centroid': [2.5, 3.1, 4.8],  # Sample values for spectral centroid frequency
    'peakf': [2.5, 3.1, 4.8],  # Sample values for frequency with amplitude peaks
    'meanfun': [0.15, 0.25, 0.35],  # Sample values for mean fundamental frequency
    'minfun': [0.15, 0.25, 0.35],  # Sample values for minimum fundamental frequency
    'maxfun': [0.15, 0.25, 0.35],  # Sample values for maximum fundamental frequency
    'meandom': [0.15, 0.25, 0.35],  # Sample values for mean dominant frequency
    'mindom': [0.15, 0.25, 0.35],  # Sample values for minimum dominant frequency
    'maxdom': [0.15, 0.25, 0.35],  # Sample values for maximum dominant frequency
    'dfrange': [0.15, 0.25, 0.35],  # Sample values for dominant frequency range
    'modindx': [0.15, 0.25, 0.35],  # Sample values for modulation index
    # Add other acoustic parameters with their respective data here
}

# Create a pandas DataFrame from the data dictionary
acoustic_data = pd.DataFrame(data)

# Save the DataFrame to a CSV file
output_file_path = 'output/voiceDetails.csv'
acoustic_data.to_csv(output_file_path, index=False)

print(f"CSV file saved to {output_file_path}")




