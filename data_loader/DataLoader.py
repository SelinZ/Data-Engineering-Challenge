"""
A loader to get data from an Excel file, remove duplicates, 
set right types, and load to the database. 
"""
import mariadb  
import logging  
import os  
import pandas as pd

LOGGER_NAME = "data_loader"

class DataLoader:
    """
    A loader that extract data from Excel file and 
    save the data in MariaDB.
    """
    def __init__(self):
        """
        Initialises the Dataloader.
        """
        self._logger = logging.getLogger(LOGGER_NAME)
        
        # Set up logging configuration 
        logging.basicConfig(level=logging.INFO) 
        
        # Get ENV VAR parameters for MariaDB using os 
        self.db_host = os.getenv('MARIADB_HOST', 'mariadb') 
        self.db_user = os.getenv('MARIADB_USER', 'dataloader') 
        self.db_password = os.getenv('MARIADB_PASSWORD', 'a-insights') 
        self.db_name = os.getenv('MARIADB_DATABASE', 'crawler_dev') 

    def load_and_clean_data(self, file_path: str):
        """
        Loads data from an Excel file, removes duplicates.   
        file_path (str): Path to the Excel file.
        Returns:pd.DataFrame: Cleaned DataFrame ready for database insertion.
        """
        # Step 1: Loads the Excel file into a DataFrame
        self._logger.info(f"Starting to load Excel file.")
        try:
            df = pd.read_excel(file_path)
            self._logger.info(f"Data successfully loaded from: {file_path}")
        except Exception as e:
            self._logger.error(f"Error loading file {file_path}: {e}")
            return None
    
        # Step 2: Removes duplicates
        initial_count = len(df)
        df = df.drop_duplicates()
        self._logger.info(f"Removed {initial_count - len(df)} duplicate rows.") 
        #10 duplicate rows removed.

        # Step 3: Ensures proper data types
        try:
            # Convert 'ARRIVAL DATE' to datetime 
            df['ARRIVAL DATE'] = pd.to_datetime(df['ARRIVAL DATE'], errors='coerce')
            df['ARRIVAL DATE'] = df['ARRIVAL DATE'].dt.strftime('%Y-%m-%d %H:%M:%S')       
            df['EXPORTER ADDRESS'] = df['EXPORTER ADDRESS'].astype(str)

            self._logger.info("Data types successfully converted.")
            
        except Exception as e:
            self._logger.error(f"Error converting data types: {e}")
        return df

    #Function to insert DataFrame data into the MariaDB table

    def insert_data(self, df: pd.DataFrame):    
        """
        Inserts DataFrame data into the MariaDB table `trade_records`.
        df (pd.DataFrame): DataFrame to be inserted into MariaDB.
        """
        db_config = {
            'host': self.db_host,
            'user': self.db_user,
            'password': self.db_password,
            'database': self.db_name
        }
        cursor = None  # Initialize cursor
        connection = None  # Initialize connection
        try:
            # Creating a connection to the MariaDB instance
            connection = mariadb.connect(**db_config)
            cursor = connection.cursor()

            # Insert each row from the DataFrame into the trade_records table
            for index, row in df.iterrows():
                # Adjusted column names to match the table's schema
                query = """
                    INSERT INTO trade_records (
                   `NO`, `ARRIVAL_DATE`, `HS_CODE`, `HS_CODE_DESCRIPTION`, 
                   `IMPORTER_ADDRESS`, `IMPORTER_COUNTRY`, `TEL`, `EMAIL`, 
                   `WEB`, `EXPORTER_ADDRESS`, `COUNTRY_OF_ORIGIN`, `IMPORT_VALUE`, 
                   `CURRENCY`, `NET_WEIGHT`, `NET_WEIGHT_UNIT`, `GROSS_WEIGHT`, 
                   `GROSS_WEIGHT_UNIT`, `QUANTITY`, `QUANTITY_UNIT`, `PRODUCT_DETAILS`,
                   `NUMBER_OF_PACKAGES`, `PACKAGES_UNIT`, `PLACE_OF_DELIVERY`, 
                   `MANUFACTURING_COMPANY`, `VOLUME`) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(query, tuple(row))  # Uses row values for insertion

            # Commit the transaction
            connection.commit()
            self._logger.info("Data inserted successfully into MariaDB.")

        except Exception as e:
            self._logger.error(f"Error inserting data into MariaDB: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()        


    def main(self):
        """
        Main function to execute the data loading, cleaning and insertion into database process.
        """
        # Path to your Excel file
        file_path = './data_loader/example-data.xlsx'

        # Load and clean data
        df = self.load_and_clean_data(file_path)
        
        if df is not None:
            # Insert data into MariaDB if the DataFrame is valid
            self.insert_data(df)    


# Run the main function
if __name__ == '__main__':
    # Initialize the DataLoader and start the process
    loader = DataLoader()
    loader.main()