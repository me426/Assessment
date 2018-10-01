# Assessment

Task 1: Docker and docker-compose

Create a docker-compose configuration which launches a Mediawiki instance using MariaDB
as a database.

## Baseline requirements

The following requirements should be met:

● When launched, the Mediawiki instance is available at http://localhost:8000/ .

● A README.md file is provided in Markdown format which discusses how to start the
instance and get to the point where the first edit can be made.

● The configuration uses volumes for user-uploads and the MariaDB database storage
so that the wiki contents are preserved when the services are stopped. (Note: it is OK
for the volume contents not to survive a “docker-compose down” but they should
survive a “docker-compose stop”.)

● The docker-compose.yml, README.md and any other associated files are published
in a git repository on GitHub.
Further requirements

The following requirements would be met by a fuller solution:

● The docker-compose.yml file has a LocalSettings.php in the same directory which is
automatically mounted into the Mediawiki container so that the installation step is
not required.

● The instance has uploads enabled.

● There is a SQL dump of the post-installation contents of the DB in a file named
initdb.sql and instructions are provided on how to restore the DB. This dump creates
an admin user with the name “Admin” and password “supersecret”.

● The code is licensed under a MIT license or other Open Source license of your
choice.

### Prerequisites

You will need docker running on your computer.

### Installing

1. Download all the files in the repository to a directory. 
2. Open a terminal window and navigate to the directory where the files are located. 
3. Run 
```
docker-compose up
```
## Getting Started

1. Navigate to localhost:8000
2. To create a page, append http://localhost:8000/index.php/ with your desired wiki entry. 

For example http://localhost:8000/index.php/hello_world

3. Click on create this page

4. Enter all the information you require on the wiki page and click save to finish.

## Built using

* [Mariadb](https://mariadb.org/) - The SQL database used
* [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) - Media Wiki

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
