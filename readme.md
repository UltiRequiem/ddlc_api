<div align="center">
  <img src="./assets/banner.png" />
</div>

# DDLC API

A RESTful API based on the [Doki Doki Literature Club](https://ddlc.moe) Game,
The #1 Psychological Horror Experience.

## Endpoints

### `GET /`

> https://ddlcapi.herokuapp.com

```json
{
  "characters": "https://ddlcapi.herokuapp.com/characters",
  "poems": "https://ddlcapi.herokuapp.com/poems",
  "acts": "https://ddlcapi.herokuapp.com/acts"
}
```

### `GET /characters`

> https://ddlcapi.herokuapp.com/characters

```json
[
  {
    "name": "monika",
    "age": 18,
    "born_date": "september 22nd",
    "concept_height": "160 cm",
    "gender": "Female",
    "hair_color": "Coral Brown",
    "eye_color": "Emerald Green",
    "filename": "monika.chr",
    "appears": ["Act 1", "Act 2", "Act 3", "Act 4"]
  }
]
```

### `GET /characters/{character}`

> https://ddlcapi.herokuapp.com/characters/monika

```json
{
  "name": "monika",
  "age": 18,
  "born_date": "september 22nd",
  "concept_height": "160 cm",
  "gender": "Female",
  "hair_color": "Coral Brown",
  "eye_color": "Emerald Green",
  "filename": "monika.chr",
  "appears": ["Act 1", "Act 2", "Act 3", "Act 4"]
}
```

## Development / Production

1. Install [Poetry](https://python-poetry.org)

2. Create a virtual environment

```sh
poetry shell
```

3. Install the dependencies

```sh
poetry install
```

4. Start the process

- Production

```sh
uvicorn ddlc:app
```

- Development

```sh
ENV=dev uvicorn ddlc:app --reload
```

## License

This project is licensed under the [MIT License](./license).
