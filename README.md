# svg_to_imgur

Author: William O'Leary

Date: Dec 2022

Convert svg to png and upload to imgur for hosting

**--Requires imgur developer credentials--**

Cairo is known be hard to get going.  You may need to install using home brew.

```bash
brew install cairo 
```

## Purpose

I was building a dashboard on Google Data Studio/ Looker Studio and I wanted to use a table row to dynamically display images - pretty things up a bit. The table row doesn't support svg.  

So what are the options?  You can convert a svg to png no problem using a tool but then where do you host the photo?  

The idea of this program is to supply a csv of links to svg urls and have the csv returned to you with columns of urls for png images hosted on imgur - imgur creates mulitple links for difference of uploaded photos.  One photo will yield 6 links.

* Converts a csv of svg links to png links hosted on imgur.
* csv is used as a way to keep links organized. As mentioned above imgur returns 6 links for each upload so it can get tendious or manual to keep them organized.
* csv can be easily be connected and blended in Data Studio/Looker.

## Getting Started

The project is ready to run as is.  In your preferred directory run:

```git clone https://github.com/macraesdirtysocks/sveeegur.git```

## Overview of functionality

Please be aware the imgur api is a little fussy about quick uploads and the timeout period is quite long (20, 30,40 mins). To try and account for this there is a 60 second sleep timer build in for each upload. For example the data I was working with when I wrote this was a csv with 40 links and it still status code 429'd on the very last upload.

* Arguments:
  * client_id - imgur client id
  * client_secret - imgur client secret
  * input_csv - csv with links of svg images
  * svg_cols - columns in input_csv that are svg image links
  * png_images_dir - output directory for png images
  * output_csv - output file path for new csv with png links

## Example Usage

```python
sveeger(
  my_client_id, 
  my_client_secret, 
  "~/Desktop/csv_or_svg_links.csv", 
  ["dog_photos", "cat_phtotos"],
  "~/Desktop/pngs", 
  "~/Desktop/csv_with_png_links.csv")

```
