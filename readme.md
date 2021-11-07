<div align="center">
  <img src="./assets/banner.png" />
</div>

# The Doki Doki Literature Club API

[![CI](https://github.com/UltiRequiem/ddlc_api/actions/workflows/ci.yml/badge.svg)](https://github.com/UltiRequiem/ddlc_api/actions/workflows/ci.yml)

A RESTful API based on [Doki Doki Literature Club](https://ddlc.moe), The #1
Psychological Horror Experience.

This API is still in constant development so if you have any idea of a feature
that you would like the api to have, open an issue or make a pull request.

## Endpoints

### `GET /`

> https://ddlcapi.herokuapp.com

Returns an object containing the data of all the characters and poems.

### `GET /characters`

> https://ddlcapi.herokuapp.com/characters

Returns an array of objects with the data of each character.

### `GET /characters/{character}`

> https://ddlcapi.herokuapp.com/characters/natsuki

Returns the data of an specific character.

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

[Team Salvato Intellectual Property Guidelines](http://teamsalvato.com/ip-guidelines).
