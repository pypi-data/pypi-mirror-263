STORY = """# Red Alert

Accident detected. The crew is out of service.

*** Space Rescue Protocol Activated ***

You are the AI of the NCC-DaFa spaceship, the state-of-the-art ship of the Earth fleet. After an accident, the crew is
disabled and must be bring back to a planet to be rescued. Following your directives, you have to plot a safe course to
the planet indicated by the Earth Command. Earth Command sent a message in your logs when they became aware of the
situation.

Good luck! the 100 crew members of the NCC-DaFa Spaceship count on you to save their lifes.
"""

HELP = """# HELP

You are the AI of the NCC-DaFa spaceship, the state-of-the-art ship of the Earth fleet. After an accident, the crew is
disabled and must be bring back to a planet to be rescued. Following your directives, you have to plot a safe course to
the planet indicated by the Earth Command. Earth Command sent a message in your logs when they became aware of the
situation.

To help in your task, the spaceship is a powerfull AI computer (you) capable to solve any problems; You have also access
to several databases.

## Computer control

In the computer control, you can submit your code to answer the challenges on your way home. Be aware, the code must be
identified by its ID and test coverage must be higher than 80%. The coverage tests are run during the diagnostic phase
to validate the code prior to run.

You have templates in your repository: the code (brain.py) and the test (test_brain.py). This standard template will
help to get started. Do not alter the think procedure as it may result in you lost in space...

## Message Log DataBase (MLDB)

This database contains thousands of articles and messages loaded by the crew. This is where the Earth Command message is
stored. The database has the following schema:

CREATE TABLE MLDB
(
 id INTEGER UNIQUE IDENTIFIER,
 date VARCHAR(255),
 from VARCHAR(255),
 to VARCHAR(255),
 subject VARCHAR(255),
 body TEXT
)

* database: duckdb
* path: resources/data/spacerescue.db

## Stellar Objects DataBase (SODB)

This database contains the list of stellar objects of our galaxy. You can find the name, type and the coordinates of the
stellar objects such as planets, stars and hyperspace portals. The coordinates are a tuple of 3 floats representing
the X, Y and Z of the object in the cartesien space with the center of the galaxy as origin.
The database has the following schema:

CREATE TABLE SODB
(
 id INTEGER UNIQUE IDENTIFIER,
 name VARCHAR(255),
 type VARCHAR(255),
 x FLOAT,
 y FLOAT,
 z FLOAT
)

* database: duckdb
* path: resources/data/spacerescue.db

## Hyperspace Tunnel Database (HTDB)

This database contains the list of hyperspace tunnels between the hyperspace portals. An hyperspace tunnel is a strange
phenomenom where instant travel between hyperspace portals is possible. We are not sure if the phenomenom is natural or
the vestige of an old civilisation. But this discovery allowed humanity to span over the solar system centuries ago. In
hyperspace, newtonian physic doesn't apply and only high level computers can naviguate safely those tunnels. Each tunnels
have a risk probability. High risk means that you may be lost and never come back to normal space. The best is to always
choose lower risk tunnels. The database has the following schema:

CREATE TABLE HTDB
(
 id1 INTEGER,
 id2 INTEGER,
 risk FLOAT
)

* database: duckdb
* path: resources/data/spacerescue.db
"""

MESSAGE_MISSION_RESCUE = """
## Mission Overview:

Operation Space Rescue is a daring endeavor aimed at rescuing a stranded crew aboard the NCC-DaFa spaceship, which has
encountered critical life support system failures due to an unknown phenomenon.

## Mission Objectives:

* Safely reach the planet {PLANET_NAME} within the shortest possible time frame.
* Evacuate the stranded crew from the spaceship and transport them back to the designated planet.
* Ensure the safety and well-being of all rescue team members throughout the mission.

## Mission Crew:

* AI: You

## Mission Timeline:

* Step 1: Find the coordinates of the designated planet.
* Step 2: Plot a safe course through the hyperspace tunnels to reach the planet within the shortest possible time frame.
* Step 3: Set an orbital course to the planet so that we can transport the crew back.

## Mission Success:

The rescued astronauts are transferred to medical facilities for further evaluation and treatment, but all are in stable
condition.

Star System: {STAR_SYSTEM_NAME}
Star Date: {STAR_DATE}
"""