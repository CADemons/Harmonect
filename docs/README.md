# Documentation Generation using MKDocs
Although we could've chosen the route for annotation generated docs, I felt that writing markdown docs may be more beneficial in terms of cleanliness, accessibility, organization, etc. I also felt that MKDocs had a format that was attractive looking. 

## Getting started
1. Make sure you have installed all packages listed in `./requirements.txt`. Two namely packages include `mkdocs` and `mkdocs-material`. These are ideal for proper documentation generation.
2. In the root of the project, there is a file doted: `mkdocs.yml`. You must add a page there like so:
```yaml
pages:
- ['index.md', 'Index']
- ['<md file>', 'Title']
```
3. Once you have added the pages, you must do the following in **the root of the project**:
```shell
$ git checkout master
$ mkdocs gh-deploy -c -m "Generated docs"
```