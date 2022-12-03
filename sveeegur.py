import csv
from time import sleep
from sveeegur.src.utils import process_svg_image_url, create_imgur_client
from sveeegur.settings import IMAGE_LINKS


def sveeegur(
    client_id: str,
    client_secret: str,
    input_csv: str,
    svg_cols: list[str],
    png_images_dir: str,
    output_csv: str,
):

    # Create an imgur client.
    im = create_imgur_client(client_id, client_secret)

    # Read in csv with links.  This reads the CSV in a a list of dicts.
    with open(input_csv, "r") as f:
        dict_reader = csv.DictReader(f)
        data = list(dict_reader)

    # CSV cols containing svg images
    svg_url_cols = svg_cols

    # Loop over your ist of dictionaries and operate on each SVG image column declared in svg_url_cols
    for item in data:

        # id column of csv file ie team name, customer number or whatever entity the urls belong to.
        # This is only used for logging.  If you want to keep track of what has been uploaded.
        # For logging uncomment line 49 and 85.
        # id_col = item[""]

        for col in svg_url_cols:

            dict_key = col  # for column naming and subsetting

            url = item[dict_key]  # url of image

            uploaded_image = process_svg_image_url(
                pyimgur_client=im,
                url=url,
                dict_key=dict_key,
                output_file_path_base=png_images_dir,
            )  # See uploaded_image_sample.json for example.
            # imagur return contains many links or different shape and size.

            image_links = {
                k: v for k, v in uploaded_image.__dict__.items() if k in IMAGE_LINKS
            }  # Get links image links from uploaded images.

            link_dict = {}

            # Create new dict keys from image_links keys and dict_key.
            # CSV file with flag column -> "link_small_square_flag"
            # See uploaded_image_sample.json for example of links returned
            for link in image_links:

                link_dict.update({f"{link}_{dict_key}": image_links[link]})

            # Add new link k,v back to original data dictionary.
            item.update(link_dict)

        # logger.info(f"{team} logos uploaded to imgur") # Uncomment for logging

        print("quick nap for 60 seconds")

        # Imgur server seems fussy about fast uploads.  Slow and steady upload.
        sleep(60)

    # Write new data out to csv file.
    with open(output_csv, "w", newline="") as csvfile:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow(i)

    return None
