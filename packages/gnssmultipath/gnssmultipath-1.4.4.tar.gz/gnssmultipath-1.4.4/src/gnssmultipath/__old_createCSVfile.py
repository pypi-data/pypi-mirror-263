import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import sys

sys.path.append(r"C:\Users\perhe\OneDrive\Documents\Python_skript\GNSS_repo\src")
from gnssmultipath import GNSS_MultipathAnalysis, PickleHandler

class createCSVfile:
    def __init__(self, analysisResults, output_dir, column_delimiter=';'):
        self.analysisResults = analysisResults
        self.output_dir = output_dir
        self.column_delimiter = column_delimiter
        self.time_stamps = self.analysisResults["ExtraOutputInfo"]["time_epochs_utc_time"]
        self.mp_data_lst = ["PRN; UTCtime; Elevation; Azimuth"]
        self.GNSSsystemCode2Fullname = {'G': 'GPS', 'R': 'GLONASS', 'E': 'Galileo', 'C': 'BeiDou'}
        self.GNSS_Name2Code = {v: k for k, v in self.GNSSsystemCode2Fullname.items()}
        self.results_dict = self.build_results_dict()


    def flatten_result_array(self, arr):
        """
        Flatten a numpy array to 1D
        """
        flatten_array = arr[:, 1:].T.ravel().tolist()
        return flatten_array

    def build_results_dict(self):
        results_dict = {}
        GNSS_systems = list(self.analysisResults["Sat_position"].keys())
        
        for sys in GNSS_systems:
            sys_name = self.GNSSsystemCode2Fullname[sys]
            results_dict[sys_name] = {"Elevation": [], "Azimuth": []}

        # Build up result dict 
        for sys in GNSS_systems:
            curr_sys = self.analysisResults["Sat_position"][sys]
            sys_name = self.GNSSsystemCode2Fullname[sys]
            results_dict[sys_name]["Azimuth"] = curr_sys["azimuth"]
            results_dict[sys_name]["Elevation"] = curr_sys["elevation"]

            SNR_dict = self.analysisResults[sys_name].get("SNR", None)
            if SNR_dict is not None:
                for signal_code, snr_array in SNR_dict.items():
                    snr_array[snr_array == 0] = np.nan # convert null to np.nan
                    signal_header = f"SNR_{signal_code}"
                    self.mp_data_lst.append(signal_header)
                    # Append SNR data to results_dict
                    results_dict[sys_name][signal_header] = SNR_dict[signal_code]
        
        return results_dict

    def write_results_to_csv(self):
        for sys_name, sys_data in self.results_dict.items():
            # Extract data into arrays
            sys_code = self.GNSS_Name2Code[sys_name]
            timestamps = self.time_stamps * sys_data["Elevation"][:, 1:].shape[1]
            prns = list(range(1, sys_data["Azimuth"].shape[1]))
            prns = [f"{sys_code}{prn:02d}" for prn in prns]
            prn_repeated = list(np.repeat(prns, sys_data["Azimuth"].shape[0]))
            
            # Flatten numpy array to 1D
            az = self.flatten_result_array(np.round(sys_data["Azimuth"], 2))
            el = self.flatten_result_array(np.round(sys_data["Elevation"], 2))

            # Create a DataFrame for the current system
            df = pd.DataFrame({
                "PRN": prn_repeated,
                "UTCtime": timestamps,
                "Azimuth": az,
                "Elevation": el
            })

            # Add SNR columns to the DataFrame
            if any(key.startswith("SNR") for key in sys_data.keys()):
                snr_headers = [header for header in sys_data.keys() if header.startswith("SNR_")]
                for i, header in enumerate(snr_headers):
                    df[header] = self.flatten_result_array(sys_data[header])

            # Remove rows where all values except PRN and time are np.nan
            df.dropna(subset=df.columns[3:], how='all', inplace=True)
            # Write DataFrame to CSV
            output_file = os.path.join(self.output_dir, f"{sys_name}_results.csv")
            print(f'INFO: The result CSV file {output_file} has been written')
            df.to_csv(output_file, index=False, sep=self.column_delimiter)


if __name__ =="__main__":
    # analysisResults = PickleHandler.read_zstd_pickle(r"C:\Users\perhe\Desktop\GitHub\analysisResults.pkl")
    analysisResults = PickleHandler.read_zstd_pickle(r"C:\Users\perhe\Desktop\CSV_export\analysisResults.pkl")
    outputDir = r"C:\Users\perhe\Desktop\CSV_export\TEST"
    createCSV = createCSVfile(analysisResults, outputDir)
    createCSV.write_results_to_csv()
