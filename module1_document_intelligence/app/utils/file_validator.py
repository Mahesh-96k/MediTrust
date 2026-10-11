ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


def is_allowed_file(filename):
    """Check whether the uploaded file has an allowed extension."""
    if not filename or "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in ALLOWED_EXTENSIONS


def is_file_size_allowed(file_size):
    """Check whether the file size is within the allowed limit."""
    return file_size <= MAX_FILE_SIZE