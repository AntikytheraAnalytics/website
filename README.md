# Application 

The website is a Flask application, primarily to support Jinja templating. 

It includes copies of:

* Bootstrap, modified and compiled for some of our branding.
* Typed.js for the landing page. 

# Assets

The code assets mentioned above are served out of the static folder of the
Flask application. 

Image assets are currently manually produced. They are resized to a reasonable
size (max 1920px width), and saved as 50% jpgs. If the file is `picture.jpg`, 
we calculate the shasum of the image, then append it to the file name as 
`picture_shasum.jpg`. This allows us to update images without waiting on the
Cloudfront distribution. 

These assets should be uploaded to the `antikytherastaticassets` S3 bucket, 
which organizes assets first by web property and then asset type. 

# Zone

We have registered `antikytheragroup.com`. The DNS zone is managed by Route 53
on AWS. 

This zone includes TXT and MX records to allow Google services to use the 
domain. 

There is a CNAME from `static.antikytheragroup.com` to a Cloudfront 
distribution. This distribution serves assets out of the 
`antikytherastaticassets` S3 bucket, and is public. 
