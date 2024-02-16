# luxonis-task

Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page. 

## Notes

* scraped prices are lower
* website is not rendered (page rendering alternatives Splash, Playwright)

## How to run

* add `.env` file with following variables:
```
POSTGRES_PASSWORD=
```

* run `docker-compose up`
