# GLBuilds

__glbuilds-2024-11-01__ is a dataset of 1.7 million build jobs collected from 10 popular open-source GitLab projects using the CI Build Digital Twin (CBDT) framework.

|        __Project__       | __#stars__ | __prog. languages__ | __#commits__ | __#jobs__ |
|:------------------------:|:----------:|:-------------------:|-------------:|:---------:|
| inkscape/inkscape        |      3,408 | C++, C              |        15.3k |   201,206 |
| CalcProgrammer1/OpenRGB  |      2,975 | C++, C              |         3.9k |    81,316 |
| gitlab-org/gitlab-runner |      2,379 | Go                  |         5.7k |   422,720 |
| F-Droid/Client           |      2,294 | Java, Kotlin        |         2.3k |    11,962 |
| veloren/veloren          |      2,169 | Rust                |         5.1k |    54,484 |
| baserow/baserow          |      1,999 | Python, JS          |        14.6k |   299,900 |
| AuroraOSS/AuroraStore    |      1,834 | Kotlin              |         1.4k |     3,313 |
| graphviz/graphviz        |      1,306 | C, C++              |         6.7k |   414,559 |
| NickBusey/HomelabOS      |      1,198 | Jinja, Go           |         2.3k |     4,637 |
| wireshark/wireshark      |      1,128 | C, C++              |        14.6k |   200,038 |
| Total                    |          - | -                   |        72.3k | 1,694,135 |

## Usage

We release this dataset to encourage implementations of CBDTs using our framework and Machine Learning for __real-time predictions__ and __continual learning of various build process performance metrics__. Other use cases include building __data-centric what-if analysis__ and __prescriptive ML-based CBDT services__.

Unzip the `glbuilds-2024-11-01.sql.zip` file which contains the 25GB `.sql` dump file of the CBDT Data Store (PostgreSQL) as of November 1, 2024.

```bash
unzip glbuilds-2024-11-01.sql.zip
```

## CBDT Data Store

While data can be restored in any PostgreSQL instance and dumped as a `.csv` file for example, the  following instructions show how to load the `.sql` dump file into the CBDT Data Store.

### Requirements

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [pgAdmin](https://www.pgadmin.org/) (Optional)

### Getting Started

Start only the CBDT data store service

```bash
cp .env.example .env
```

```bash
docker-compose up -d datastore
```

Restore data.

```bash
cat glbuilds-2024-11-01.sql | ./scripts/restore.sh
```

It might tqOpen pgAdmin to start querying the database. We provide examples of SQL queries in the `queries` directory.

# CBDT Framework

The `docker-compose.yaml` file shows the technical configuration of the five services available in the CBDT framework:

* __build-monitor__
* __build-pulse__
* __build-data-subscriber__
* __cbdt-datastore__ (PostgreSQL)
* __cbdt-message-broker__ (RabbitMQ)

Source code and container images of __`build-monitor`__, __`build-pulse`__, and  __`build-data-subscriber`__ will be made publicly available upon acceptance of the paper.
