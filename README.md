# snack-scrapy
Snack scraping miniquiz with Scrapy

If anyone is/was/will be interested in using Scrapy I put together today's miniquiz using it.

```bash
pip install scrapy
```
or
```bash
conda install scrapy
```
```bash
cd ./snack-scrapy
scrapy crawl crawl -s MONGO_HOST=127.0.0.1 -s MONGO_PORT=27017 -s MONGO_DB=snacker -s MONGO_COLLECTION=snacks
```

DISCALIMER: THERE ARE BETTER SCRAPY TUTORIALS ON THE INTERNETS
