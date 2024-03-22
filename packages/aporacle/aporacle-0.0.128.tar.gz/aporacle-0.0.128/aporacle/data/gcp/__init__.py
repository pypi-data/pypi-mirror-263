# [START storage_list_files]
import pandas as pd
from google.cloud import storage
from io import StringIO
from io import BytesIO


# 0. List all buckets.
def list_bucket_names():
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    return [bucket.name for bucket in buckets]


# 1. Create bucket if not exist. Map bucket to feed.
def create_bucket(bucket_name: str):
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    return bucket.name


# 2. List files by feed/bucket.
def list_files_by_feed(feed: str):
    storage_client = storage.Client()
    blobs = list(storage_client.list_blobs(bucket_or_name=feed))
    return [blob.name for blob in blobs]


# 3. Upload file to bucket by feed.
def upload_file_to_bucket(feed: str, file_path: str):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(feed)
    blob = bucket.blob(file_path)
    blob.upload_from_filename(file_path)


# 4. Download file from bucket by symbol name.
def download_file_from_bucket(feed: str, file_path: str):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(feed)
    blob = bucket.blob(file_path)
    blob.download_to_filename(file_path)


# 5. Delete file from bucket by symbol name.
def delete_file_from_bucket(feed: str, file_path: str):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(feed)
    blob = bucket.blob(file_path)
    blob.delete()


# 6. Delete bucket by feed or bucket name.
def delete_bucket(bucket_name: str):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()


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
