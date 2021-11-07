<div align="center">
  <img src="./assets/banner.png" />
</div>

# DDLC API

A RESTful API based on the [Doki Doki Literature Club](https://ddlc.moe) Game,
The #1 Psychological Horror Experience.

## Endpoints

### `GET /`

> https://ddlcapi.herokuapp.com

Returns an object containing all the available endpoints.

```json
{
  "characters": "https://ddlcapi.herokuapp.com/characters",
  "poems": "https://ddlcapi.herokuapp.com/poems",
  "acts": "https://ddlcapi.herokuapp.com/acts"
}
```

### `GET /characters`

> https://ddlcapi.herokuapp.com/characters

Returns an array of objects with the data of each character.

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

It has the data of all the characters, I don't put it here all,
because the readme would be huge.

### `GET /characters/{character}`

> https://ddlcapi.herokuapp.com/characters/natsuki

Returns the data of an specific character.

```json
{
  "name": "natsuki",
  "age": 18,
  "born_date": "December 10th",
  "concept_height": "150 cm",
  "gender": "Female",
  "hair_color": "Pastel Pink",
  "eye_color": "Pink",
  "filename": "natsuki.chr",
  "appears": ["Act 1", "Act 2", "Act 4"],
  "voice_actor": null
}
```

If you pass a character that doesn't exist you will receive:

> https://ddlcapi.herokuapp.com/characters/lol

```json
{ "detail": "Character \"lol\" not found." }
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

This API does not serve official DDLC or DDLC Plus assets,
and throughout the project only a [modified version of the promotion
banner](./assets/banner.png) (I just trimmed it a little because it was too big),
is used for the readme.

[Team Salvato IP Guidelines](http://teamsalvato.com/ip-guidelines).
