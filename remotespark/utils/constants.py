# Copyright (c) 2015  aggftw@gmail.com
# Distributed under the terms of the Modified BSD License.


CONFIG_JSON = "config.json"

SESSION_KIND_SPARK = "spark"
SESSION_KIND_PYSPARK = "pyspark"
SESSION_KIND_SPARKR = "sparkr"
SESSION_KINDS_SUPPORTED = [SESSION_KIND_SPARK, SESSION_KIND_PYSPARK, SESSION_KIND_SPARKR]

SESSION_CREATION_START_EVENT = "notebookSessionCreationStart"
SESSION_CREATION_END_EVENT = "notebookSessionCreationEnd"

CONTEXT_NAME_SPARK = "spark"
CONTEXT_NAME_SQL = "sql"

LANG_SCALA = "scala"
LANG_PYTHON = "python"
LANG_R = "r"
LANGS_SUPPORTED = [LANG_SCALA, LANG_PYTHON, LANG_R]

LONG_RANDOM_VARIABLE_NAME = "_yQeKOYBsFgLWWGWZJu3y"

MAGICS_LOGGER_NAME = "magicsLogger"

IDLE_SESSION_STATUS = "idle"
ERROR_SESSION_STATUS = "error"
DEAD_SESSION_STATUS = "dead"
NOT_STARTED_SESSION_STATUS = "not_started"
STARTING_SESSION_STATUS = "starting"
BUSY_SESSION_STATUS = "busy"

POSSIBLE_SESSION_STATUS = [NOT_STARTED_SESSION_STATUS, IDLE_SESSION_STATUS, STARTING_SESSION_STATUS,
                           BUSY_SESSION_STATUS, ERROR_SESSION_STATUS, DEAD_SESSION_STATUS]
FINAL_STATUS = [DEAD_SESSION_STATUS, ERROR_SESSION_STATUS]

DELETE_SESSION_ACTION = "delete"
START_SESSION_ACTION = "start"
DO_NOTHING_ACTION = "nothing"
