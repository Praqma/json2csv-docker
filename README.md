# json2csv-docker

A simple Docker image of [zeMirco/json2csv](https://github.com/zeMirco/json2csv).

## Usage

The image isn't published anywhere, so you'll have to build it yourself:

- `docker build -t json2csv:0.1.0 .`

The entrypoint is set to `json2csv`, so just run the container with whatever arguments you want.
Remember to mount the directory with your JSON file(s).

Examples:

- `docker run -v $(pwd):/input json2csv:0.1.0  input/some-data.json > some-data.csv`
- `docker run -v $(pwd):/input json2csv:0.1.0  --unwind "orderItems" --flatten-arrays --flatten-objects -i input/some-data.json > some-data.csv`
