# angle-demo
Angle health demo app.

## running
```bash
docker-compose up -d # starts postgres and django containers
docker-compose exec backend python manage.py test post # to evaluate the specification has been met
```
or
https://github.com/JonZudell/angle-demo/actions 
# Backend Project -- Specification

Let's start an e-commerce company! Some of the basic functionalities of an e-commerce website
include allowing vendors to post their products, and let users to search for products that they
want.

Here's what we will need for a backend:

## Implement a `post` route

The `post` route allows vendors to post their products.

### `post` input

The input would be sent via `POST` and looks like:

```json
{
  "posts": [
    {
      "name": "abc",
      "price": 10000,
      "start_date": "01/01/2021"
    },
    {
      "name": "abd",
      "price": 20000,
      "start_date": "01/01/2021"
    }
  ]
}
```

* `name` (`string`): Name for the product, 4-10 characters long. The first letter has to be a
  digit or a letter (`0-9`, `A-Z`, `a-z`). All other letters has to be a digit, a letter, a space,
  or a hyphen (`0-9`, `A-Z`, `a-z`, ` `, `-`).
* `price` (`number`): Price for the product, an integer representing the price in cents. E.g.,
  `10000` means 10000 cents and therefore 100 dollars.
* `start_date` (`string`): Product sale start date, in the form of `MM/DD/YYYY`.

If for any entry, the `name` already exists or `start_date` is before current date, reject the
whole request and do not store any information from this request. Send any error response as you see fit.

### `post` output

The output can be an empty `201` response.

## Implement a `search` route

The `search` route allows users to search existing products.

### `search` input

The input would be sent via `GET` as query parameters.

```text
keyword=ab&min_price=15000&max_price=25000
```

* `keyword` (`string`): Keyword to be searched. All posts whose name has the keyword as a
  substring should be matched. E.g., keyword `ab` should match names `ab`, `abc`, `abd`, and `dab`.
* `min_price` (`number`): Minimum price to be matched (inclusive). This value may be empty, which
  means no price lower bound.
* `max_price` (`number`): Maximum price to be matched (inclusive). This value may be empty, which
  means no price upper bound.

### `search` output

The output would be the posts that match the query.

```json
{
  "posts": [
    {
      "name": "abd",
      "price": 20000,
      "start_date": "01/01/2021"
    }
  ]
}
```

In this case, both `abc` and `abd` matches the keyword parameter, but only `abd` is within the
price range.

## Other considerations

`data_nn.json` includes sample post data for your testing.

This project is expected to be done using Python 3.8/3.9. Feel free to include solutions using
other languages in addition to the Python solution.

Include a `Dockerfile` with your project to avoid any system configuration differences that may
introduce issues. Make sure to include the instructions on how to run your code as necessary into a
text/reStructuredText/Markdown file. Add any external dependencies you need into `requirements.txt`
and do *not* include them in your project.

Feel free to use any data storage solution that can be packaged with your code. You don't have to
include the database itself, if your code can generate the datebase (E.g., Django migrations).

There can be thousands of post entries, so make sure both `post` and `search` is as performant as
you can make it be.
