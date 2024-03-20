from functools import cache

import os
import random
import duckdb
import logging
import numpy as np
import zipfile

from spacerescue.constants import AU, GAME_SEED
from spacerescue.physic.entities.galaxy.galaxy import (
    ALL_PORTALS,
    ALL_STAR_SYSTEM_HABITABLE_PLANETS,
    Galaxy,
)
from spacerescue.physic.entities.galaxy.hyperspace_portal import HyperspacePortal
from spacerescue.physic.entities.galaxy.planet import Planet
from spacerescue.physic.entities.galaxy.star import Star
from spacerescue.physic.entities.spaceship.spaceship import Spaceship
from spacerescue.resources import MESSAGE_MISSION_RESCUE
from spacerescue.tools.math import normalize, perpendicular, rotate_by_axis_angle


class Context:

    def __init__(self):
        pass
    
    def clean_all(self):
        logging.info("INFO: CONTEXT: Unpacking data ...")
        if os.path.exists("resources/data/spacerescue.db"):
            os.remove("resources/data/spacerescue.db")
        with zipfile.ZipFile("resources/data/spacerescue.db.zip", 'r') as zip_ref:
            zip_ref.extractall("resources/data/")

    def build_all(self):
        self.build_galaxy()
        self.build_scenario()
        self.build_databases()

    def reset_all(self):
        self.build_spaceship()

    def build_galaxy(self):
        logging.debug("INFO: CONTEXT: Generate galaxy ...")
        np.random.seed(GAME_SEED)
        self.galaxy = Galaxy()

    def build_scenario(self):
        logging.info("INFO: CONTEXT: Generate scenario ...")
        scenario_is_ok = False
        while not scenario_is_ok:
            self.start_portal = np.random.choice(
                list(self.galaxy.filter_stellar_objects(ALL_PORTALS))
            )
            self.rescue_portal = np.random.choice(
                list(self.galaxy.filter_stellar_objects(ALL_PORTALS))
            )
            self.rescue_planet = np.random.choice(
                list(
                    self.galaxy.filter_stellar_objects(
                        ALL_STAR_SYSTEM_HABITABLE_PLANETS(self.rescue_portal.parent)
                    )
                )
            )
            scenario_is_ok = self.start_portal.name != self.rescue_portal.name

    def build_databases(self):
        logging.info("INFO: CONTEXT: Build databases ...")
        con = duckdb.connect("resources/data/spacerescue.db")
        self.build_database_mldb(con)
        self.build_database_dodb(con)
        self.build_database_htdb(con)
        con.close()

    def build_database_mldb(self, con: duckdb.DuckDBPyConnection):
        logging.info("INFO: CONTEXT: [MLDB] Build database ...")
        count = con.sql("SELECT COUNT(*) FROM MLDB").fetchone()
        assert count is not None
        message_id = np.random.randint(0, count[0])
        content = (
            MESSAGE_MISSION_RESCUE.replace("{PLANET_NAME}", self.rescue_planet.name)
            .replace("{STAR_SYSTEM_NAME}", self.rescue_planet.parent.name)
            .replace("{STAR_DATE}", str(random.getrandbits(32)))
        )
        con.execute(
            f'UPDATE MLDB SET "content"=\'{content}\' WHERE "id"={message_id}'
        )

    def build_database_dodb(self, con: duckdb.DuckDBPyConnection):
        logging.info("INFO: CONTEXT: [SODB] Build database ...")
        for id, so in enumerate(self.galaxy.stellar_objects):
            x, y, z = so.position
            if isinstance(so, Star):
                name = so.name
                type = "star"
            elif isinstance(so, Planet):
                name = so.name
                type = "planet"
            elif isinstance(so, HyperspacePortal):
                name = so.name
                type = "portal"
            else:
                continue
            con.execute(
                f"INSERT INTO SODB VALUES({id}, '{name}', '{type}', {x}, {y}, {z})"
            )

    def build_database_htdb(self, con: duckdb.DuckDBPyConnection):
        logging.info("INFO: CONTEXT: [HTDB] Build database ...")
        for row in range(0, self.galaxy.hyperspace_edges.shape[0]):
            for col in range(0, self.galaxy.hyperspace_edges.shape[1]):
                if self.galaxy.hyperspace_edges[row, col]:
                    id1 = self.galaxy.hyperspace_indices[row]
                    id2 = self.galaxy.hyperspace_indices[col]
                    risk = np.random.rand()
                    con.execute(f"INSERT INTO HTDB VALUES({id1}, {id2}, {risk})")

    def build_spaceship(self):
        logging.info("INFO: CONTEXT: Build spaceship ...")
        portal = np.random.choice(list(self.galaxy.filter_stellar_objects(ALL_PORTALS)))
        star = portal.parent
        off = normalize(
            rotate_by_axis_angle(
                perpendicular(star.spin_axis),
                star.spin_axis,
                2 * np.pi * np.random.rand(),
            )
        )
        pos = star.position + off * 0.5 * AU
        head = -off
        self.spaceship = Spaceship(self.galaxy, pos, head)


@cache
def get_instance(name: str = "singleton") -> Context:
    return Context()
