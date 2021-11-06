<div align="center">
  <img src="./assets/banner.png" />
</div>

# DDLC API

A RESTful API based on the [Doki Doki Literature Club](https://ddlc.moe) Game,
The #1 Psychological Horror Experience.

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
