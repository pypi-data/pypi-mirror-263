# [START storage_list_files]
import pandas as pd
from google.cloud import storage
from io import StringIO
from io import BytesIO


# 0. List all buckets.
def list_buckets():
    """Lists all buckets in your GCP project."""
    try:
        storage_client = storage.Client()
        buckets = list(storage_client.list_buckets())
        return [bucket.name for bucket in buckets]

    except Exception as err:
        print(f"Error listing buckets: {err}")


# 1. Create bucket if not exist. Map bucket to feed.
def create_bucket(bucket_name, location=None):
    """Creates a bucket in Google Cloud Storage.

    Args:
      bucket_name: The name of the bucket to create.
      location: The location to store the bucket data (optional). Defaults to None (US multi-region).

    Returns:
      The newly created bucket object, or None on error.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        bucket.create(location=location)
        print(f"Bucket '{bucket_name}' created successfully.")
        return bucket
    except Exception as err:
        print(f"Error creating bucket: {err}")
        return None


def list_bucket_files(bucket_name: str):
    """Lists all files (blobs) within a bucket in Google Cloud Storage.

  Args:
      bucket_name: The name of the bucket to list files from.
  """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs()
        return [blob.name for blob in blobs]

    except Exception as err:
        print(f"Error listing bucket files: {err}")


# 2. List files by feed/bucket.
def list_files_by_feed(feed: str):
    return list_bucket_files(bucket_name=feed)


# 3. Upload file to bucket by feed.
def upload_file_to_bucket(bucket_name: str, source_file_path: str, destination_blob_name: str):
    """Uploads a file to GCP storage.

      Args:
        bucket_name: The name of the bucket to upload the file to.
        source_file_path: The local path of the file to upload.
        destination_blob_name: The name of the file in the bucket (optional).
      """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        if destination_blob_name:
            blob = bucket.blob(destination_blob_name)
        else:
            blob = bucket.blob(source_file_path.split('/')[-1])  # Use filename by default
        blob.upload_from_filename(source_file_path)
        print(f"File uploaded to {bucket_name}/{blob.name}")
    except Exception as err:
        print(f"Error uploading file: {err}")


# 4. Download file from bucket by symbol name.
def download_file_from_bucket(bucket_name: str, object_name: str, local_path: str):
    """Downloads a file from GCP storage and returns the local path.

      Args:
          bucket_name: The name of the bucket containing the file.
          object_name: The name of the file to download.
          local_path: The local path to save the downloaded file.

      Returns:
          The local path of the downloaded file, or None on error.
      """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.download_to_filename(local_path)
        return local_path
    except Exception as err:
        print(f"Error downloading file: {err}")
        return None


# 5. Delete file from bucket by symbol name.
def delete_file_from_bucket(bucket_name: str, object_name: str):
    """Deletes a file (blob) from a bucket in Google Cloud Storage.

      Args:
          bucket_name: The name of the bucket containing the file.
          object_name: The name of the file (blob) to delete.

      Returns:
          True on successful deletion, False otherwise.
      """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.delete()
        print(f"File '{object_name}' deleted from bucket '{bucket_name}'.")
        return True
    except Exception as err:
        print(f"Error deleting file: {err}")
        return False


# 6. Delete bucket by feed or bucket name.
def delete_bucket(bucket_name):
    """Deletes a bucket in Google Cloud Storage.

    Args:
      bucket_name: The name of the bucket to delete.

    Returns:
      True on successful deletion, False otherwise.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        bucket.delete()
        print(f"Bucket '{bucket_name}' deleted successfully.")
        return True
    except Exception as err:
        print(f"Error deleting bucket: {err}")
        return False


# 7. Upload dataframe to GCP
def upload_df_to_gcp(bucket_name: str, symbol: str, df: pd.DataFrame):
    destination_blob_name = f"{symbol}.csv".lower()

    # Convert DataFrame to a CSV string in memory
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)  # Set index=False to exclude the index column

    # Upload the CSV string to GCP bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(csv_buffer.getvalue())


# 8. Download CSV from GCP and return as DataFrame
def download_csv_from_gcp_return_df(bucket_name: str, symbol: str):
    file_path = f"{symbol}.csv".lower()

    # Download the CSV file from GCP bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_path)

    # Download data as a byte stream
    csv_data = blob.download_as_string()

    # Convert byte stream to in-memory file-like object
    csv_buffer = BytesIO(csv_data)

    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_buffer)

    # Return the DataFrame
    return df
