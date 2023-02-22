import csv
import shutil
import os
import dotenv

if __name__ == "__main__":
    # Load the .env file
    dotenv.load_dotenv()

    # Setup constants for our .env
    DATASET_IMAGES_PATH: str = os.getenv("DATASET_IMAGES_PATH")
    LABELS_CSV_PATH: str = os.getenv("LABELS_CSV_PATH")
    OUTPUT_TARGET_PATH: str = os.getenv("OUTPUT_TARGET_PATH")

    with open(LABELS_CSV_PATH, "r") as f:
        reader: csv.reader = csv.reader(f)

        next(reader)

        # Iterate through each label row and grab its data
        for row in reader:

            # Image file name
            fileName: str = row[0]

            # Array of class labels of findings
            findings: list[str] = row[1].split("|")

            # Grab the image path
            imagePath: str = f"{DATASET_IMAGES_PATH}\\{fileName}"

            # Loop through each finding, and copy the image into the output directory in the specified class directory
            for finding in findings:
                # Specify the output directory for the finding classification
                OUTPUT_CLASS_PATH: str = f"{OUTPUT_TARGET_PATH}\\{finding}"

                # If the directory doesn't exist, create it
                if not os.path.exists(OUTPUT_CLASS_PATH):
                    os.makedirs(OUTPUT_CLASS_PATH)

                # Copy the image from the dataset, into the specified output directory
                shutil.copy(imagePath, OUTPUT_CLASS_PATH)
