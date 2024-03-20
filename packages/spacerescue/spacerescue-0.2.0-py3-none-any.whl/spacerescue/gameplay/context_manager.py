from functools import cache

import duckdb
import numpy as np
import logging

from spacerescue.constants import AU, GAME_SEED
from spacerescue.physic.entities.galaxy.galaxy import ALL_PORTALS, Galaxy
from spacerescue.physic.entities.galaxy.hyperspace_portal import HyperspacePortal
from spacerescue.physic.entities.galaxy.planet import Planet
from spacerescue.physic.entities.galaxy.star import Star
from spacerescue.physic.entities.spaceship.spaceship import Spaceship
from spacerescue.tools.math import normalize, perpendicular, rotate_by_axis_angle


class Context:
    
    MESSAGE_ID = 153581
    
    def __init__(self):
        pass

    def build_all(self):
        self.build_galaxy()
        self.build_databases()

    def reset_all(self):
        self.build_spaceship()
        
    def build_galaxy(self):
        logging.info("INFO: CONTEXT: Build galaxy ...")
        np.random.seed(GAME_SEED)
        self.galaxy = Galaxy()
        
    def build_databases(self):
        logging.info("INFO: CONTEXT: Build databases ...")
        con = duckdb.connect("resources/data/spacerescue.db")
        self.build_database_mldb(con)
        self.build_database_dodb(con)
        self.build_database_htdb(con)
        con.close()

    def build_database_mldb(self, con: duckdb.DuckDBPyConnection):       
        logging.info("INFO: CONTEXT: [MLDB] Build database ...")
        content = "the message :)"
        con.execute(f"UPDATE MLDB SET \"content\"='{content}' WHERE \"id\"={Context.MESSAGE_ID}")
        
    def build_database_dodb(self, con: duckdb.DuckDBPyConnection):
        logging.info("INFO: CONTEXT: [SODB] Build database ...")
        con.execute(f"DELETE FROM SODB")
        for id, so in enumerate(self.galaxy.stellar_objects):
            if isinstance(so, Star):
                name = "sun"
                type = "star"
            elif isinstance(so, Planet):
                name = "earth"
                type = "planet"
            elif isinstance(so, HyperspacePortal):
                name = "xyz"
                type = "portal"  
            else:
                continue
            x, y, z = so.position
            con.execute(f"INSERT INTO SODB VALUES({id}, \'{name}\', \'{type}\', {x}, {y}, {z})")
    
    def build_database_htdb(self, con: duckdb.DuckDBPyConnection):
        logging.info("INFO: CONTEXT: [HTDB] Build database ...")
        con.execute(f"DELETE FROM HTDB")
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