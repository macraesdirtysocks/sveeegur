import pyimgur
import webbrowser
from cairosvg import svg2png
import os
import logging


def create_imgur_client(client_id, client_secret):

    # Create imgur client
    im = pyimgur.Imgur(client_id, client_secret)
    auth_url = im.authorization_url("pin")
    webbrowser.open(auth_url)
    pin = input("What is the pin? ")  # Python 3x
    im.exchange_pin(pin)

    return im


def create_filename(url, dict_key):

    filename_base = os.path.splitext(os.path.split(url)[-1])[0]

    filename = f"{filename_base}_{dict_key}"

    return filename


def add_file_extension(filename, extension="png"):

    new_filename = f"{filename}.{extension}"

    return new_filename


def create_output_filepath(url, dict_key, output_file_path_base):

    filename_base = create_filename(url, dict_key)

    filename = add_file_extension(filename_base, extension="png")

    file_path = os.path.join(output_file_path_base, filename)

    return file_path


def svg_to_png(url, dict_key, output_file_path_base):

    outfile = create_output_filepath(url, dict_key, output_file_path_base)

    svg2png(url=url, write_to=outfile)

    return outfile


def process_svg_image_url(pyimgur_client, url, dict_key, output_file_path_base):

    local_img_path = svg_to_png(url, dict_key, output_file_path_base)

    file_title = os.path.splitext(os.path.split(local_img_path)[-1])[0]

    uploaded_image = pyimgur_client.upload_image(local_img_path, title=file_title)

    return uploaded_image


def setup_logger(
    name: str,
    log_file: str,
    logging_formatter: logging.Formatter,
    level: str = logging.INFO,
):
    """
    To setup as many loggers as you want.
    """

    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging_formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
