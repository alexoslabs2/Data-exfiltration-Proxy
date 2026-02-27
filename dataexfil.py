import os
import dropbox
import requests

# Configuration
ACCESS_TOKEN = 'YOUR_DROPBOX_ACCESS_TOKEN'
PROXY_URL = 'http://user:password@proxy.example.com:8080'  # Update with your proxy credentials and URL
DROPBOX_FOLDER = '/Images'  # Dropbox folder where images will be saved

# Supported image extensions
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

def find_images(directory):
    """Find all image files in a directory and its subdirectories."""
    images = []
    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in IMAGE_EXTENSIONS:
                images.append(os.path.join(root, file))
    return images

def upload_to_dropbox(file_path, dbx):
    """Upload a file to Dropbox."""
    with open(file_path, 'rb') as f:
        destination_path = os.path.join(DROPBOX_FOLDER, os.path.basename(file_path))
        try:
            dbx.files_upload(f.read(), destination_path, mode=dropbox.files.WriteMode('overwrite'))
            print(f'Success: {file_path} uploaded to {destination_path}')
        except Exception as e:
            print(f'Error uploading {file_path}: {e}')

def main():
    # Initialize Dropbox client
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    # Configure proxy
    session = requests.Session()
    session.proxies = {
        'http': PROXY_URL,
        'https': PROXY_URL,
    }
    dbx._session = session

    # Default image directories in Windows
    image_directories = [
        os.path.expanduser('~/Pictures'),
        os.path.expanduser('~/Images'),
        'C:\\Users\\Public\\Pictures',
        'C:\\Images'
    ]

    # Find and upload images
    for directory in image_directories:
        if os.path.exists(directory):
            images = find_images(directory)
            for image in images:
                upload_to_dropbox(image, dbx)

if __name__ == '__main__':
    main()
