import os
import zipfile


def create_cbz_archive(directory_to_archive, output_directory, filename):
    if not os.path.exists(directory_to_archive):
        raise FileNotFoundError(directory_to_archive)

    if not os.path.exists(output_directory):
        raise FileNotFoundError(output_directory)

    # if the file name has any extension other than cbz replace with cbz
    if not filename.endswith('.cbz'):
        filename = filename.split('.')[0] + '.cbz'

    # change to the directory to archive
    os.chdir(directory_to_archive)

    # create a zip file
    with zipfile.ZipFile(os.path.join(output_directory, filename), 'w') as zipf:
        for file in os.listdir():
            if os.path.isfile(file):
                zipf.write(file)


def test():
    source_dir = ''
    destination_dir = ''
    file_name = 'test.cbz'
    create_cbz_archive(source_dir, destination_dir, file_name)


if __name__ == '__main__':
    test()
