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

<details>
  <summary>Response</summary>

```json
{
  "characters": [
    {
      "name": "yuri",
      "age": 18,
      "born_date": "December 10th",
      "concept_height": "165 cm",
      "gender": "Female",
      "hair_color": "Dark Purple",
      "eye_color": "Light Purple",
      "filename": "yuri.chr",
      "appears": ["Act 1", "Act 2", "Act 4"],
      "voice_actor": null,
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/yuri.png"
    },
    {
      "name": "monika",
      "age": 18,
      "born_date": "September 22nd",
      "concept_height": "160 cm",
      "gender": "Female",
      "hair_color": "Coral Brown",
      "eye_color": "Emerald Green",
      "filename": "monika.chr",
      "appears": ["Act 1", "Act 2", "Act 3", "Act 4"],
      "voice_actor": "Jillian Ashcraft",
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/monika.png"
    },
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
      "voice_actor": null,
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/natsuki.png"
    },
    {
      "name": "sayori",
      "age": 18,
      "born_date": "April 13",
      "concept_height": "157 cm",
      "gender": "Female",
      "hair_color": "Coral Pink",
      "eye_color": "Sky Blue",
      "filename": "sayori.chr",
      "appears": ["Act 1", "Act 4"],
      "voice_actor": null,
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/sayori.png"
    }
  ],
  "poems": "https://ddlcapi.herokuapp.com/poems"
}
```

</details>

### `GET /characters`

> https://ddlcapi.herokuapp.com/characters

Returns an array of objects with the data of each character.

<details>
  <summary>Response</summary>
  
  ```json
  [
      {
         "name":"yuri",
         "age":18,
         "born_date":"December 10th",
         "concept_height":"165 cm",
         "gender":"Female",
         "hair_color":"Dark Purple",
         "eye_color":"Light Purple",
         "filename":"yuri.chr",
         "appears":[
            "Act 1",
            "Act 2",
            "Act 4"
         ],
         "voice_actor":null,
         "illustration":"https://ddlcapi.herokuapp.com/illustrations/yuri.png"
      },
      {
         "name":"monika",
         "age":18,
         "born_date":"September 22nd",
         "concept_height":"160 cm",
         "gender":"Female",
         "hair_color":"Coral Brown",
         "eye_color":"Emerald Green",
         "filename":"monika.chr",
         "appears":[
            "Act 1",
            "Act 2",
            "Act 3",
            "Act 4"
         ],
         "voice_actor":"Jillian Ashcraft",
         "illustration":"https://ddlcapi.herokuapp.com/illustrations/monika.png"
      },
      {
         "name":"natsuki",
         "age":18,
         "born_date":"December 10th",
         "concept_height":"150 cm",
         "gender":"Female",
         "hair_color":"Pastel Pink",
         "eye_color":"Pink",
         "filename":"natsuki.chr",
         "appears":[
            "Act 1",
            "Act 2",
            "Act 4"
         ],
         "voice_actor":null,
         "illustration":"https://ddlcapi.herokuapp.com/illustrations/natsuki.png"
      },
      {
         "name":"sayori",
         "age":18,
         "born_date":"April 13",
         "concept_height":"157 cm",
         "gender":"Female",
         "hair_color":"Coral Pink",
         "eye_color":"Sky Blue",
         "filename":"sayori.chr",
         "appears":[
            "Act 1",
            "Act 4"
         ],
         "voice_actor":null,
         "illustration":"https://ddlcapi.herokuapp.com/illustrations/sayori.png"
      }
   ]
  ```
</details>

### `GET /characters/{character}`

> https://ddlcapi.herokuapp.com/characters/yuri

Returns an object with the data of an specific character.

<details>
  <summary>Response</summary>
  
  ```json
  {
    "name": "yuri",
    "age": 18,
    "born_date": "December 10th",
    "concept_height": "165 cm",
    "gender": "Female",
    "hair_color": "Dark Purple",
    "eye_color": "Light Purple",
    "filename": "yuri.chr",
    "appears": ["Act 1", "Act 2", "Act 4"],
    "voice_actor": null,
    "illustration": "https://ddlcapi.herokuapp.com/illustrations/yuri.png"
  }
  ```
</details>

If you pass a character that doesn't exist you will receive:

> https://ddlcapi.herokuapp.com/characters/lol

```json
{ "detail": "Character \"lol\" not found." }
```

### `GET /illustrations`

> https://ddlcapi.herokuapp.com/illustrations

An object, key is the character name and the value is a link with the illustration.

<details>
  <summary>Response</summary>
  
  ```json
  {
   "yuri": "https://ddlcapi.herokuapp.com/illustrations/yuri.png",
   "natsuki": "https://ddlcapi.herokuapp.com/illustrations/natsuki.png",
   "sayori": "https://ddlcapi.herokuapp.com/illustrations/sayori.png",
   "monika": "https://ddlcapi.herokuapp.com/illustrations/monika.png"
  }
  ```
</details>

### `GET /illustrations/{character}.png`

> https://ddlcapi.herokuapp.com/illustrations/natsuki.png

The illustration of `{character}`.

<details>
  <summary>Response</summary>
  
  ![Natsuki Image](https://ddlcapi.herokuapp.com/illustrations/natsuki.png)
</details>

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
