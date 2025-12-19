import hashlib
import os


def get_filename_hash(file_name: str, hash_algorithm='sha256', file_extension=""):
    """
    Function to calculate the hash value based on the file name using a given hash algorithm (default is SHA-256).

    :param file_name: The file name (including path if needed).
    :param hash_algorithm: The hash algorithm to use ('sha256', 'md5', etc.)
    :return: The hash value of the file name.
    """
    hash_func = hashlib.new(hash_algorithm)

    hash_func.update(file_name.encode('utf-8'))
    file_extension = os.path.splitext(file_name)[1]

    hex_digest = hash_func.hexdigest()
    return (f"{hex_digest}{file_extension}", hex_digest)